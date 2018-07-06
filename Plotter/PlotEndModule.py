from Core.EndModule import EndModule

import os,ROOT,math

from SampleColor import sampleColorDict

ROOT.gROOT.SetBatch(ROOT.kTRUE)

class PlotEndModule(EndModule):
    def __init__(self,outputDir,plots,ratio_switch=False):
        self.outputDir = outputDir
        self.plots = plots
        self.switch = ratio_switch

    def __call__(self,collector):
        for plot in self.plots:
            self.drawPlot(collector,plot,self.outputDir,self.switch)

    def drawPlot(self,collector,plot,outputDir,switch):
        if plot.dim == 1:
            self.makedirs(outputDir)
            self.draw1DPlot(collector,plot,outputDir,switch)
        else:
            print "Skipping plot "+plot.key+" as TH"+str(plot.dim)+" is not supported at the moment"

    @staticmethod
    def makedirs(outputDir):
        if not os.path.exists(os.path.abspath(outputDir)):
            os.makedirs(os.path.abspath(outputDir))

    def sortHistList(self,histList):
        histList.sort(key=lambda l: l[2], reverse=False)

    def stackData(self,collector,plot):

        for isample,sample in enumerate(collector.dataSamples):
            h = collector.getObj(sample,plot.rootSetting[1])
            if not isample: 
                data = h.Clone("data")
            else: 
                data.Add(h)

        self.shiftLastBin(data)

        if plot.plotSetting.divideByBinWidth:
            self.divideByBinWidth(data)

        data.SetLineWidth(2)
        data.SetLineColor(1)
        data.SetMarkerStyle(8)
        data.SetTitle("")

        return data

    def divideByBinWidth(self,hist):
        for iBin in range(1,hist.GetNbinsX()+1):
            binC = hist.GetBinContent(iBin)
            binE = hist.GetBinError(iBin)
            binW = hist.GetBinWidth(iBin)
            hist.SetBinContent(iBin,binC/binW)
            hist.SetBinError(iBin,binE/binW)

    def stackMC(self,collector,plot,switch):
        stack = ROOT.THStack(plot.key+'_stack',plot.key+'_stack')

        smCount      = 0.0
        smCountErrSq = 0.0
        histList     = []
        #totalsum = ROOT.TH1D()

        for isample,sample in enumerate(collector.mcSamples if not collector.mergeSamples else collector.mergeSamples):
            if collector.sampleDict[sample].isSignal: continue
            h = collector.getObj(sample,plot.rootSetting[1])
            if sample in sampleColorDict:
                h.SetFillColor(sampleColorDict[sample])
            else:
                h.SetFillColor(ROOT.kViolet)
            self.shiftLastBin(h)
            smCountErrTmp = ROOT.Double(0.)
            smCount += h.IntegralAndError(0,h.GetNbinsX()+1,smCountErrTmp)
            smCountErrSq += smCountErrTmp**2
            histList.append([h,sample,h.Integral(0,h.GetNbinsX()+1)])
            if switch:
                if not isample:
                    totalsum = h.Clone("totalsum_"+plot.key)
                else:
                    totalsum.Add(h)

        self.sortHistList(histList)

        if plot.plotSetting.divideByBinWidth:
            for hist,sample,_ in histList:
                self.divideByBinWidth(hist)

        for h,sample,_ in histList:
            if switch: h.Divide(totalsum)
            stack.Add(h) 

        total = stack.GetStack().Last().Clone("total_"+plot.key)
        total.SetFillColor(ROOT.kYellow)
        total.SetLineColor(ROOT.kRed)
        bkdgErr = stack.GetStack().Last().Clone("totalErr_"+plot.key)
        bkdgErr.SetMarkerStyle(1)
        bkdgErr.SetLineColor(1)
        bkdgErr.SetLineWidth(3)
        bkdgErr.SetFillColor(13)
        bkdgErr.SetFillStyle(3001)

        return histList,stack,smCount,smCountErrSq,total,bkdgErr

    def makeSignalHist(self,collector,plot):
        histList = []
        for sample in collector.signalSamples:
            h = collector.getObj(sample,plot.rootSetting[1])
            if sample in sampleColorDict:
                h.SetFillColor(sampleColorDict[sample])
            else:
                h.SetFillColor(ROOT.kViolet)
            self.shiftLastBin(h)
            sigCount = h.Integral(0,h.GetNbinsX()+1) 
            h.SetLineStyle(9)
            h.SetLineWidth(5)
            h.SetLineColor(sampleColorDict[sample])
            h.SetFillColorAlpha(ROOT.kRed,0.)
            histList.append([h,sample,sigCount])

        if plot.plotSetting.divideByBinWidth:
            for hist,sample,sigCount in histList:
                self.divideByBinWidth(hist)

        return histList


    def makeLegend(self,histList,bkdgErr,smCount,switch=False,histListSignal=None,data=None):
        leg = ROOT.TLegend(0.63,0.58,0.89,0.87)
        leg.SetBorderSize(0)
        leg.SetFillColor(0)
        leg.SetTextSize(0.02)
        if data:
            legLabel = "Data"
            legLabel += ": {0}".format(int(data.Integral(0,data.GetNbinsX()+1)))
            leg.AddEntry(data, legLabel , "p")
        # if not self._normToData and data:
            # if not self._normToData: leg.AddEntry(data, "Data: {0}".format(int(data.Integral(0,data.GetNbinsX()+1))), "p")
        legLabel = "SM total"
        if switch:
            legLabel += ": 100%"
        else:
            legLabel += ": "+str(math.ceil(smCount*10)/10)
        if bkdgErr:
            leg.AddEntry(bkdgErr, legLabel, "fl") 
        
        for hCount in reversed(histList):
            legLabel = hCount[1]
            if switch:
	       legLabel += ": "+str(math.ceil(math.ceil(hCount[2]*10)/math.ceil(smCount*10)*100000)/1000)+"%"
            else:         
                legLabel += ": "+str(math.ceil(hCount[2]*10)/10)
            leg.AddEntry(hCount[0], legLabel, "f")

        for hist,sample,sigCount in histListSignal:
            legLabel = sample
            legLabel += ": "+str(math.ceil(sigCount*10)/10)
            leg.AddEntry(hist,legLabel,"f")
	
        return leg

    def getAxisTitle(self,plot):
        if plot.plotSetting.x_axis_title:
            return plot.plotSetting.x_axis_title 
        elif plot.key in plot.plotSetting.defaultLabelDict:
            return plot.plotSetting.defaultLabelDict[plot.key]
        else:
            return plot.key 

    def draw1DPlot(self,collector,plot,outputDir,switch):
        c = ROOT.TCanvas("c_"+plot.key, "c_"+plot.key,0,0, 650, 750)

        axisLabel = self.getAxisTitle(plot)

        if not collector.mcSamples and not collector.dataSamples:
            raise RuntimeError, "Nothing to be drown"

        if collector.dataSamples and switch:
            raise RuntimeError, "Cannot run incorporate data samples and background ratio at the same time"

        if collector.dataSamples:
            dataHist = self.stackData(collector,plot)

        if collector.bkgSamples:
            histList,stack,smCount,smCountErrSq,total,bkdgErr = self.stackMC(collector,plot,switch)
            stack.SetTitle("")
            # stack.GetYaxis().SetTitleSize(0.05)
        
        if collector.dataSamples and collector.bkgSamples:
            maximum = max(stack.GetMaximum(),dataHist.GetMaximum())
        elif collector.bkgSamples:
            maximum = stack.GetMaximum()
        elif collector.dataSamples:
            maximum = dataHist.GetMaximum()

        if collector.bkgSamples and not collector.dataSamples:
            stack.Draw('hist')
            self.setStackAxisTitle(stack,axisLabel,plot)

            sigHistList = self.makeSignalHist(collector,plot)

            leg = self.makeLegend(histList,bkdgErr,smCount,switch,histListSignal=sigHistList)
 
            c.SetLogy(0)
            stack.SetMaximum(maximum*1.5)
            stack.SetMinimum(0.)
            stack.Draw('hist')
            for hist,sample,sigCount in sigHistList:
                hist.Draw('samehist')
            #if collector.dataSamples:
            #    dataHist.Draw("samep")
            leg.Draw('same')
            # Draw CMS, lumi and preliminary if specified
            #self.drawLabels(pSetPair[0].lumi)
            bkdgErr.Draw("samee2")
            c.SaveAs(outputDir+"/"+plot.key+".png")
            c.SaveAs(outputDir+"/"+plot.key+".pdf")

            if not switch:
                c.SetLogy(1)
                stack.SetMaximum(maximum*5)
                stack.SetMinimum(0.1)
                stack.Draw('hist')
                for hist,sample,sigCount in sigHistList:
                    hist.Draw('samehist')
                if collector.dataSamples:
                    dataHist.Draw("samep")
                leg.Draw('same')
                # Draw CMS, lumi and preliminary if specified
                #self.drawLabels(pSetPair[0].lumi)
                bkdgErr.Draw("samee2")

                c.SaveAs(outputDir+"/"+plot.key+"_log.png")
                c.SaveAs(outputDir+"/"+plot.key+"_log.pdf")
        elif collector.bkgSamples and collector.dataSamples:
            c.SetBottomMargin(0.0)
            upperPad = ROOT.TPad("upperPad", "upperPad", .001, 0.25, .995, .995)
            lowerPad = ROOT.TPad("lowerPad", "lowerPad", .001, .001, .995, .325)
            upperPad.Draw()
            lowerPad.Draw()
            
            lowerPad.cd()
            lowerPad.SetGridy(1)
            ROOT.gPad.SetBottomMargin(0.24)
        
            ratio,bkdgErrRatio,line = self.makeRatioPlot(dataHist,total,bkdgErr)
            ratio.SetStats(0)
            ratio.Draw()
            bkdgErrRatio.Draw("samee2")

            ratio.GetYaxis().SetRangeUser(0.5,1.5)
            #ratio.GetYaxis().SetRangeUser(0.0,2.0)
            ratio.GetYaxis().SetLabelSize(0.075)
            ratio.GetXaxis().SetLabelSize(0.075)
            ratio.GetYaxis().SetTitle("Data/MC")
            ratio.GetYaxis().SetTitleSize(0.10)
            ratio.GetXaxis().SetTitleSize(0.10)
            ratio.GetXaxis().SetTitleOffset(0.90)
            ratio.GetYaxis().SetTitleOffset(0.50)
            ratio.GetXaxis().SetTitle(axisLabel)

            bkdgErrRatio.SetMarkerStyle(1)
            bkdgErrRatio.SetLineColor(1)
            bkdgErrRatio.SetFillColor(13)
            bkdgErrRatio.SetFillStyle(3001)

            ratio.DrawCopy()
            bkdgErrRatio.DrawCopy("samee2") 
            line.Draw()

            upperPad.cd()
            
            leg = self.makeLegend(histList,bkdgErr,smCount,switch,data=dataHist)
            
            upperPad.SetLogy(0)
            stack.SetMaximum(maximum*1.5)
            dataHist.SetMaximum(maximum*1.5)

            stack.Draw('hist')
            stack.GetXaxis().SetTitleOffset(0.55)
            self.setStackAxisTitle(stack,axisLabel,plot)
            stack.Draw('hist')
            leg.Draw()
            
            if smCount > 0.0:
                scaleFactor = dataHist.GetEntries()*1.0/smCount
                scaleFactorErr = scaleFactor*math.sqrt(1/dataHist.GetEntries() + smCountErrSq/smCount**2)
            else:
                scaleFactor    = 0.0
                scaleFactorErr = 0.0

            n1 = ROOT.TLatex()
            n1.SetNDC()
            n1.SetTextFont(42)
            n1.SetTextSize(0.05);
            n1.DrawLatex(0.11, 0.92, "Data/MC = %.2f #pm %.2f" % (scaleFactor,scaleFactorErr))

            dataHist.DrawCopy('samep')
            bkdgErr.Draw("samee2")

            # c.cd()
            
            c.SaveAs(outputDir+"/"+plot.key+".png")
            c.SaveAs(outputDir+"/"+plot.key+".pdf")

            upperPad.SetLogy(1)
            stack.SetMaximum(maximum*5)
            stack.SetMinimum(0.1)
            stack.Draw('hist')
            dataHist.Draw("samep")
            leg.Draw('same')
            # Draw CMS, lumi and preliminary if specified
            #self.drawLabels(pSetPair[0].lumi)
            bkdgErr.Draw("samee2")
            n1.DrawLatex(0.11, 0.92, "Data/MC = %.2f #pm %.2f" % (scaleFactor,scaleFactorErr))

            c.SaveAs(outputDir+"/"+plot.key+"_log.png")
            c.SaveAs(outputDir+"/"+plot.key+"_log.pdf")

        elif collector.signalSamples and not collector.bkgSamples:

            sigHistList = self.makeSignalHist(collector,plot)

            leg = self.makeLegend([],None,0.,False,histListSignal=sigHistList)
 
            c.SetLogy(0)
            for hist,sample,sigCount in sigHistList:
                hist.Draw('samehist')
            #if collector.dataSamples:
            #    dataHist.Draw("samep")
            leg.Draw('same')
            # Draw CMS, lumi and preliminary if specified
            #self.drawLabels(pSetPair[0].lumi)
            c.SaveAs(outputDir+"/"+plot.key+".png")
            c.SaveAs(outputDir+"/"+plot.key+".pdf")

    def setStackAxisTitle(self,stack,axisLabel,plot):
        stack.GetXaxis().SetTitle(axisLabel)
        title = "Events / %.2f " % (stack.GetXaxis().GetBinWidth(2)) if plot.plotSetting.divideByBinWidth else "Events / GeV "
        stack.GetYaxis().SetTitle(title)

    def makeRatioPlot(self,data,total,bkdgErr):

        ratio = data.Clone("ratio")
        ratio.Divide(total)

        bkdgErrRatio = ratio.Clone("ratioerr")
        for i in range(1, bkdgErrRatio.GetNbinsX()+1): 
            binC = bkdgErr.GetBinContent(i)
            binE = bkdgErr.GetBinError(i)
            bkdgErrRatio.SetBinContent(i,1)
            if binC>0.: bkdgErrRatio.SetBinError(i,1*binE/binC)
            else      : bkdgErrRatio.SetBinError(i,0.)

        line = ROOT.TLine(60,1,400,1)
        line = ROOT.TLine(ratio.GetXaxis().GetBinLowEdge(1) ,1,ratio.GetXaxis().GetBinUpEdge(ratio.GetXaxis().GetNbins()),1)
        line.SetLineColor(2)
        line.SetLineWidth(2)

        return ratio,bkdgErrRatio,line

    def shiftLastBin(self,h):
        # FirstBin = h.GetXaxis().GetFirst()
        LastBin = h.GetXaxis().GetLast()
        for bin in range( LastBin + 1, LastBin + 2 ):
            h.SetBinContent( LastBin, h.GetBinContent( LastBin ) + h.GetBinContent( bin ) )
            h.SetBinError( LastBin, math.sqrt( math.pow( h.GetBinError( LastBin ), 2 ) + math.pow( h.GetBinError( bin ), 2 ) ) )
            h.SetBinContent( LastBin + 1, 0. )
            h.SetBinError( LastBin + 1, 0. )
            pass
        return                
