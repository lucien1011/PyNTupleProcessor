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
            self.draw1DPlot(collector,plot,outputDir,switch)
        else:
            print "Skipping plot "+plot.key+" as TH"+str(plot.dim)+" is not supported at the moment"

    @staticmethod
    def makedirs(outputDir):
        if not os.path.exists(os.path.abspath(outputDir)):
            os.makedirs(os.path.abspath(outputDir))

    def sortHistList(self,histList):
        histList.sort(key=lambda l: l[2], reverse=False)

    def stackMC(self,collector,plot,switch):
        stack = ROOT.THStack(plot.key+'_stack',plot.key+'_stack')

        smCount      = 0.0
        smCountErrSq = 0.0
        histList     = []
        totalsum = ROOT.TH1D()

        for isample,sample in enumerate(collector.mcSamples):
            h = collector.getObj(sample,plot.rootSetting[1])
            h.SetFillColor(sampleColorDict[sample])
            self.shiftLastBin(h)
	    if isample == 0 and switch:
	       totalsum = h.Clone("totalsum")
            smCountErrTmp = ROOT.Double(0.)
            smCount += h.IntegralAndError(0,h.GetNbinsX()+1,smCountErrTmp)
            smCountErrSq += smCountErrTmp**2
            histList.append([h,sample,h.Integral(0,h.GetNbinsX()+1)])
            if isample != 0 and switch:
               totalsum.Add(h)

        self.sortHistList(histList)

        if plot.plotSetting.divideByBinWidth:
            for hist,sample,_ in histList:
                for iBin in range(1,hist.GetNbinsX()+1):
                    binC = hist.GetBinContent(iBin)
                    binE = hist.GetBinError(iBin)
                    binW = hist.GetBinWidth(iBin)
                    hist.SetBinContent(iBin,binC/binW)
                    hist.SetBinError(iBin,binE/binW)

        if switch:
	   for h,sample,_ in histList:
               h.Divide(totalsum)
               stack.Add(h) 
        else:
	    for h,sample,_ in histList:
		stack.Add(h)

        return histList,stack,smCount,smCountErrSq

    def makeLegend(self,histList,bkdgErr,smCount,switch=False,histListSignal=None,data=None):
        leg = ROOT.TLegend(0.63,0.58,0.89,0.87)
        leg.SetBorderSize(0)
        leg.SetFillColor(0)
        leg.SetTextSize(0.02)
        if data:
            legLabel = "Data"
            if self.addYields: legLabel += ": {0}".format(int(data.Integral(0,data.GetNbinsX()+1)))
            leg.AddEntry(data, legLabel , "p")
        # if not self._normToData and data:
            # if not self._normToData: leg.AddEntry(data, "Data: {0}".format(int(data.Integral(0,data.GetNbinsX()+1))), "p")
        legLabel = "SM total"
        if switch:
	   legLabel += ": 100%"
	else:
            legLabel += ": "+str(math.ceil(smCount*10)/10)
        leg.AddEntry(bkdgErr, legLabel, "fl") 
        
        for hCount in reversed(histList):
            legLabel = hCount[1]
            if switch:
	       legLabel += ": "+str(math.ceil(math.ceil(hCount[2]*10)/math.ceil(smCount*10)*100000)/1000)+"%"
            else:         
                legLabel += ": "+str(math.ceil(hCount[2]*10)/10)
            leg.AddEntry(hCount[0], legLabel, "f")
	
        return leg

    def getAxisTitle(self,plot):
        if plot.plotSetting.x_axis_title:
            return plot.plotSetting.x_axis_title 
        elif plot.key in plot.plotSetting.defaultLabelDict:
            return plot.plotSetting.defaultLabelDict[plot.key]
        else:
            return plot.key 

    def draw1DPlot(self,collector,plot,outputDir,switch):
        #c = ROOT.TCanvas("c", "c",0,0, 650, 750)
        c = ROOT.TCanvas()
        histList,stack,smCount,smCountErrSq = self.stackMC(collector,plot,switch)
        
        total = stack.GetStack().Last().Clone("total")
        total.SetFillColor(ROOT.kYellow)
        total.SetLineColor(ROOT.kRed)
        bkdgErr = stack.GetStack().Last().Clone("total")
        bkdgErr.SetMarkerStyle(1)
        bkdgErr.SetLineColor(1)
        bkdgErr.SetLineWidth(3)
        bkdgErr.SetFillColor(13)
        bkdgErr.SetFillStyle(3001)

        leg = self.makeLegend(histList,bkdgErr,smCount,switch)

        axisLabel = self.getAxisTitle(plot)

        stack.SetTitle("")
        stack.Draw('hist')
        # stack.GetYaxis().SetTitleSize(0.05)
        stack.GetXaxis().SetTitle(axisLabel)
        title = "Events / %.2f " % (stack.GetXaxis().GetBinWidth(2)) if plot.plotSetting.divideByBinWidth else "Events / GeV "
        stack.GetYaxis().SetTitle(title)
        # stack.GetXaxis().SetTitleOffset(0.55)
        
        c.SetLogy(0)
        stack.SetMaximum(stack.GetMaximum()*1.5)
        stack.SetMinimum(0.)
        #stack.Draw('hist')
        leg.Draw('same')
        # Draw CMS, lumi and preliminary if specified
        #self.drawLabels(pSetPair[0].lumi)
        bkdgErr.Draw("samee2")
	#print total, histList, stack, smCount, bkdgErr
        c.SaveAs(outputDir+"/"+plot.key+".png")
        c.SaveAs(outputDir+"/"+plot.key+".pdf")

        if not switch:
           c.SetLogy(1)
           stack.SetMaximum(stack.GetMaximum()*5)
           stack.SetMinimum(0.1)
           stack.Draw('hist')
           leg.Draw('same')
           # Draw CMS, lumi and preliminary if specified
           #self.drawLabels(pSetPair[0].lumi)
           bkdgErr.Draw("samee2")
           c.SaveAs(outputDir+"/"+plot.key+"_log.png")
           c.SaveAs(outputDir+"/"+plot.key+"_log.pdf")

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
