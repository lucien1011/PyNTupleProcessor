"""
Author: Kin Ho Lo
A new PlotEndModule specifically for the stupid, needlessly complicated CMS publication and plotting recommendations.
"""
import os,ROOT,math,array

from Core.EndModule import EndModule
from Core.BaseObject import BaseObject
from Core.Utils.printFunc import pyPrint

from Utils.tdrstyle import setTDRStyle
from Utils.CMS_lumi import CMS_lumi
from Plotter.SampleColor import sampleColorDict

from Plotter.PlotEndModule import PlotEndModule

ROOT.gROOT.SetBatch(ROOT.kTRUE)

bkdgErrBarColor = 3004

class PaperPlotEndModule(PlotEndModule):
    def drawPlot(self,collector,plot,outputDir,switch):
        if plot.plotSetting.tdr_style:
            setTDRStyle()
            ROOT.gStyle.SetLabelSize(0.018,"XYZ")
            ROOT.gStyle.SetTitleSize(0.035,"XYZ")
        self.makedirs(outputDir)
        self.drawDataMCPlot(collector,plot,outputDir,switch)

    def makeTGraph(self,hist):
        x_points = []
        ex_points = []
        y_points = []
        ely_points = []
        ehy_points = []
        for ibin in range(1,hist.GetNbinsX()+1):
            x = hist.GetXaxis().GetBinCenter(ibin)
            if x < 4.0 or (x > 8.5 and x < 11.0): continue
            x_points.append(hist.GetXaxis().GetBinCenter(ibin))
            ex_points.append(0.)
            y_points.append(hist.GetBinContent(ibin))
            ely_points.append(hist.GetBinErrorLow(ibin))
            ehy_points.append(hist.GetBinErrorUp(ibin))
        xs = array.array("d",x_points)
        exs = array.array("d",ex_points)
        ys = array.array("d",y_points)
        elys = array.array("d",ely_points)
        ehys = array.array("d",ehy_points)
        g = ROOT.TGraphAsymmErrors(len(x_points),xs,ys,exs,exs,elys,ehys)
        return g

    def drawDataMCPlot(self,collector,plot,outputDir,switch):
        c = ROOT.TCanvas("c_"+plot.key, "c_"+plot.key,0,0, 650, 750)

        axisLabel = self.getAxisTitle(plot)

        if collector.dataSamples:
            ROOT.gSystem.Load(os.environ["BASE_PATH"]+"/Plotter/makePoissonHist_cc.so")
            dataHist,dataCount,dataCountErr = self.stackData(collector,plot)
            dataGraph = self.makeTGraph(dataHist)
            self.setDataHistStyle(dataGraph)

        if collector.bkgSamples:
            histList,stack,smCount,smCountErrSq,total,bkdgErr = self.stackMC(collector,plot,switch,histToScale=dataHist if self.scaleToData else None)
            stack.SetTitle("")
            if self.customSMCountFunc:
                customSMCount = self.customSMCountFunc(collector,plot)
            else:
                customSMCount = None

        if collector.signalSamples:
            sigHistList = self.makeSignalHist(collector,plot)
        else:
            sigHistList = []

        if collector.bkgSamples:
            bkgMax = stack.GetMaximum()
        else:
            bkgMax = 0.

        if collector.dataSamples:
            dataMax = dataHist.GetMaximum()
        else:
            dataMax = 0.
        
        if collector.signalSamples:
            sigMax = max([hist.GetMaximum() for hist,sample,sigCount in sigHistList])
        else:
            sigMax = 0.

        maximum = max([bkgMax,dataMax,sigMax])

        c.SetBottomMargin(0.0)
        ROOT.gStyle.SetErrorX(0)
        if not plot.plotSetting.skip_data_mc_ratio:
            upperPad = ROOT.TPad("upperPad", "upperPad", .001, 0.25, .995, .995)
            lowerPad = ROOT.TPad("lowerPad", "lowerPad", .001, .001, .995, .32)

            upperPad.Draw()
            lowerPad.Draw()

            lowerPad.cd()
            lowerPad.SetGridy(1)
            ROOT.gPad.SetBottomMargin(0.24)

            _,bkdgErrRatio,line = self.makeRatioPlot(dataHist,total,bkdgErr)
            ratio = self.makeRatioTGraph(dataHist,total,bkdgErr)

            self.setRatioHistStyle(bkdgErrRatio,axisLabel,plot,)
            ratio.GetYaxis().SetRangeUser(0.0,max([ratio.GetPointY(i) for i in range(1,ratio.GetN()+1)])*1.5) 
            bkdgErrRatio.GetYaxis().SetRangeUser(0.0,max([ratio.GetPointY(i) for i in range(1,ratio.GetN()+1)])*1.5)
            if plot.plotSetting.ratio_range:
                ratio.GetYaxis().SetRangeUser(*plot.plotSetting.ratio_range)
                bkdgErrRatio.GetYaxis().SetRangeUser(*plot.plotSetting.ratio_range)
            bkdgErrRatio.SetMarkerSize(0)
            bkdgErrRatio.Draw("e2")
            ratio.Draw("sameP")
            line.Draw()

            upperPad.cd()
        else:
            upperPad = c
            ROOT.gPad.SetBottomMargin(0.10)

        leg = self.makeLegend1D(histList,bkdgErr,smCount,switch,data=dataHist,dataCount=dataCount,histListSignal=sigHistList,smCountErr=math.sqrt(smCountErrSq),skipError=plot.plotSetting.skip_leg_err,leg_pos_list=plot.plotSetting.leg_pos,leg_text_size=plot.plotSetting.leg_text_size,)

        upperPad.SetLogy(0)
        stack.SetMaximum(maximum*plot.plotSetting.linear_max_factor)
        dataHist.SetMaximum(maximum*plot.plotSetting.linear_max_factor)

        stack.Draw('hist')
        self.setStackAxisTitle(stack,axisLabel,plot)
        stack.GetXaxis().SetLabelSize(plot.plotSetting.stack_x_label_size)
        stack.GetXaxis().SetTitleOffset(1.00)
        stack.GetYaxis().SetLabelSize(0.05)
        stack.Draw('hist')
        for hist,sample,sigCount in sigHistList:
            hist.Draw('samehist')

        leg.Draw()

        if smCount > 0.0 and dataCount > 0.:
            scaleFactor = dataCount*1.0/smCount
            scaleFactorErr = scaleFactor*math.sqrt(1/dataCount + smCountErrSq/smCount**2)
        else:
            pyPrint("Warning, smCount or dataCount is zero :"+plot.key)
            scaleFactor    = 0.0
            scaleFactorErr = 0.0

        n1 = ROOT.TLatex()
        n1.SetNDC()
        n1.SetTextFont(42)
        n1.SetTextSize(0.05);
        if not self.skipSF:
            n1.DrawLatex(0.11, 0.92, "Data/MC = %.2f #pm %.2f" % (scaleFactor,scaleFactorErr))
        if plot.plotSetting.cms_lumi != None:
            plot.plotSetting.cms_lumi(upperPad,plot.plotSetting.cms_lumi_number,0)

        #dataHist.DrawCopy('sameE')
        dataGraph.Draw('sameP')
        bkdgErr.Draw("samee2")

        if plot.plotSetting.custom_latex_list:
            for latex_setting in plot.plotSetting.custom_latex_list:
                latex_setting.latex = ROOT.TLatex()
                latex_setting.latex.SetTextSize(latex_setting.text_size)
                latex_setting.latex.DrawLatex(latex_setting.x_pos,latex_setting.y_pos,latex_setting.text)

        ROOT.gPad.RedrawAxis()
        ROOT.gPad.RedrawAxis("G")
        
        c.SaveAs(outputDir+plot.key+".png")
        c.SaveAs(outputDir+plot.key+".pdf")

        upperPad.SetLogy(1)
        stack.SetMaximum(maximum*plot.plotSetting.log_max_factor)
        stack.SetMinimum(plot.plotSetting.log_min)
        stack.Draw('hist')
        for hist,sample,sigCount in sigHistList:
            hist.Draw('samehist')
        dataHist.Draw("sameE")
        leg.Draw('same')
        bkdgErr.Draw("samee2")
        n1.DrawLatex(0.11, 0.92, "Data/MC = %.2f #pm %.2f" % (scaleFactor,scaleFactorErr))
        ROOT.gPad.RedrawAxis()
        ROOT.gPad.RedrawAxis("G")

        c.SaveAs(outputDir+plot.key+"_log.png")
        c.SaveAs(outputDir+plot.key+"_log.pdf")
