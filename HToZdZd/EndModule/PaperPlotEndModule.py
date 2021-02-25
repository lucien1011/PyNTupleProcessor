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

        sigHistList.sort(key=lambda x: float(x[1].split()[6]))

        if collector.bkgSamples:
            bkgMax = stack.GetMaximum()
        else:
            bkgMax = 0.

        if collector.dataSamples:
            dataMax = dataHist.GetMaximum()
        else:
            dataMax = 0.
        
        if collector.signalSamples:
            sigMax = max([hist.GetMaximum() for hist,sample,sigCount,error in sigHistList])
        else:
            sigMax = 0.

        maximum = max([bkgMax,dataMax,sigMax])

        c.SetBottomMargin(0.0)
        ROOT.gStyle.SetErrorX(0)
        upperPad = c
        ROOT.gPad.SetBottomMargin(0.10)

        leg = self.makeLegend1D(histList,bkdgErr,smCount,switch,data=dataHist,dataCount=dataCount,histListSignal=sigHistList,smCountErr=math.sqrt(smCountErrSq),skipError=plot.plotSetting.skip_leg_err,leg_pos_list=plot.plotSetting.leg_pos,leg_text_size=plot.plotSetting.leg_text_size,sort_sig_func=lambda x: float(x[1].split()[6]),skip_total=False,)

        upperPad.SetLogy(0)
        stack.SetMaximum(maximum*plot.plotSetting.linear_max_factor)
        dataHist.SetMaximum(maximum*plot.plotSetting.linear_max_factor)

        stack.Draw('hist')
        self.setStackAxisTitle(stack,axisLabel,plot)
        stack.GetXaxis().SetLabelSize(plot.plotSetting.stack_x_label_size)
        stack.GetXaxis().SetTitleOffset(1.20)
        stack.GetYaxis().SetLabelSize(0.05)
        stack.Draw('hist')
        bkdgErrGraph = self.makeTGraph(bkdgErr,force_x_axis_err=True)
        for errHist in [bkdgErrGraph,bkdgErr,]:
            errHist.SetMarkerStyle(1)
            errHist.SetLineWidth(1)
            errHist.SetFillColor(13)
            errHist.SetFillStyle(bkdgErrBarColor)
            errHist.SetFillStyle(3002)
            #errHist.SetFillColorAlpha(ROOT.kBlack,1)
        bkdgErrGraph.Draw("sameE2")
        for hist,sample,sigCount,error in sigHistList:
            hist.Draw('samehist')

        leg.Draw()

        if plot.plotSetting.cms_lumi != None:
            plot.plotSetting.cms_lumi(upperPad,plot.plotSetting.cms_lumi_number,0)
        
        #dataHist.DrawCopy('sameE')
        dataGraph.Draw('sameP')
        bkdgErr.Draw("samee2")

        if plot.plotSetting.custom_latex_list:
            for latex_setting in plot.plotSetting.custom_latex_list:
                latex_setting.latex = ROOT.TLatex()
                latex_setting.latex.SetTextSize(latex_setting.text_size)
                latex_setting.latex.DrawLatex(
                        latex_setting.x_pos,
                        maximum*latex_setting.y_rel_pos*plot.plotSetting.linear_max_factor,
                        latex_setting.text,
                        )

        ROOT.gPad.RedrawAxis()
        ROOT.gPad.RedrawAxis("G")
        
        c.SaveAs(outputDir+plot.key+".png")
        c.SaveAs(outputDir+plot.key+".pdf")
