import ROOT
from Core.Module import Module
import os,array,numpy
from Utils.DeltaR import deltaR

class Lepeff(Module):

    def __init__(self,name):
        super(Lepeff,self).__init__(name)
                        
    def begin(self):
        pt_bins = numpy.array([5,10,15,20,30,50,70,100,150,200], dtype='float64')
        eta_bins = numpy.array([-2.4,-1.42,0,1.42,2.4], dtype='float64')
        if "LepeffNum" not in self.writer.objs:
            #self.writer.book("LepeffNum","TH2D","LepeffNum","",9,pt_bins,4,eta_bins)
            self.writer.book("LepeffNum_pt","TH1D","LepeffNum_pt","",9,pt_bins)
            self.writer.book("LepeffNum_eta","TH1D","LepeffNum_eta","",20,-2.5,2.5)
            self.writer.book("LepeffNum_dr","TH1D","LepeffNum_dr","",20,0.,5)
            #self.writer.book("LepeffNum_pt_barrel","TH1D","LepeffNum_pt_barrel","",9,pt_bins)
            #self.writer.book("LepeffNum_eta_barrel","TH1D","LepeffNum_eta_barrel","",9,pt_bins)
            #self.writer.book("LepeffNum_dr_barrel","TH1D","LepeffNum_dr_barrel","",9,pt_bins)
        if "LepeffDem" not in self.writer.objs:
            #self.writer.book("LepeffDem","TH2D","LepeffDem","",9,pt_bins,4,eta_bins)
            self.writer.book("LepeffDem_pt","TH1D","LepeffDem_pt","",9,pt_bins)
            self.writer.book("LepeffDem_eta","TH1D","LepeffDem_eta","",20,-2.5,2.5)
            self.writer.book("LepeffDem_dr","TH1D","LepeffDem_dr","",20,0.,5)
            #self.writer.book("LepeffDem_pt_barrel","TH1D","LepeffDem_pt_barrel","",9,pt_bins)
            #self.writer.book("LepeffDem_eta_barrel","TH1D","LepeffDem_eta_barrel","",9,pt_bins)
            #self.writer.book("LepeffDem_dr_barrel","TH1D","LepeffDem_dr_barrel","",9,pt_bins)
        if "LepacptNum" not in self.writer.objs:
            self.writer.book("LepacptNum","TH1D","LepacptNum","",9,pt_bins)
        if "LepacptDem" not in self.writer.objs:
            self.writer.book("LepacptDem","TH1D","LepacptDem","",9,pt_bins)
        if "EventeffNum" not in self.writer.objs:
            self.writer.book("EventeffNum","TH1D","EventeffNum","",1,-1.0,1.0)
        if "EventeffDem" not in self.writer.objs:
            self.writer.book("EventeffDem","TH1D","EventeffDem","",1,-1.0,1.0)
        if "testEventNum" not in self.writer.objs:
            self.writer.book("testEventNum","TH1D","testEventNum","",1,-1.0,1.0)
        if "testEventDem" not in self.writer.objs:
            self.writer.book("testEventDem","TH1D","testEventDem","",1,-1.0,1.0)

        if "MomId_GENlep" not in self.writer.objs:
            self.writer.book("MomId_GENlep","TH1D","MomId_GENlep","",35,-5.0,30.)
        if "nGENlep_vs_nRECOlep" not in self.writer.objs:
            self.writer.book("nGENlep_vs_nRECOlep","TH2D","nGENlep_vs_nRECOlep","",10,0,10,10,0,10)
        if "nGENlep_vs_nRECOlep_ZZprime" not in self.writer.objs:
            self.writer.book("nGENlep_vs_nRECOlep_ZZprime","TH2D","nGENlep_vs_nRECOlep_ZZprime","",10,0,10,10,0,10)
        #if "CTageffNum" not in self.writer.objs:
        #self.writer.book("CTageffNum","TH2D","CTageffNum","",10,0.,200.,10,-2.4,2.4)
            #self.writer.book("CTageffNum","TH2D","CTageffNum","",9,pt_bins,4,eta_bins)
        #if "CTageffDem" not in self.writer.objs:
        #self.writer.book("CTageffDem","TH2D","CTageffDem","",10,0.,200.,10,-2.4,2.4)
            #self.writer.book("CTageffDem","TH2D","CTageffDem","",9,pt_bins,4,eta_bins)
        #if "LTageffNum" not in self.writer.objs:
        #self.writer.book("LTageffNum","TH2D","LTageffNum","",10,0.,200.,10,-2.4,2.4)
            #self.writer.book("LTageffNum","TH2D","LTageffNum","",9,pt_bins,4,eta_bins)
        #if "LTageffDem" not in self.writer.objs:
        #self.writer.book("LTageffDem","TH2D","LTageffDem","",10,0.,200.,10,-2.4,2.4)
            #self.writer.book("LTageffDem","TH2D","LTageffDem","",9,pt_bins,4,eta_bins)

    def analyze(self, event):
        if self.dataset.isData: return True
        dr = 0.3
        lepid = -1
        genlepid = -1
        event.deltaRGENrecolep = []
        event.deltaRGENclosestlep = []
        lepnumber = []
        recolepnumber = []
        numbool = False
        dembool = False

        #Plots for number of GENlep vs number of RECO lep
        tempgenlepnumber = 0
        temprecolepnumber = 0
        tempgenlepnumberfromzzprime = 0
        temprecolepnumberfromzzprime = 0
        for i in range(0,int(event.GENlep_id.size())):
            if event.GENlep_pt[i] > 5.0 and abs(event.GENlep_eta[i]) < 2.4 and abs(event.GENlep_id[i]) == 13:
                tempgenlepnumber += 1
                if event.GENlep_MomId[i] == 23 or event.GENlep_MomId[i] == 999888:
                    tempgenlepnumberfromzzprime += 1
        for i in range(0,int(event.lep_pt.size())):
            if event.lep_pt[i] > 5.0 and abs(event.lep_eta[i]) < 2.4 and abs(event.lep_matchedR03_PdgId[i]) == 13:
                temprecolepnumber += 1
                if event.lep_matchedR03_MomId[i] == 23 or event.lep_matchedR03_MomId[i] == 999888:
                    temprecolepnumberfromzzprime += 1
        self.writer.objs["nGENlep_vs_nRECOlep"].Fill(tempgenlepnumber,temprecolepnumber,event.weight)
        self.writer.objs["nGENlep_vs_nRECOlep_ZZprime"].Fill(tempgenlepnumberfromzzprime,temprecolepnumberfromzzprime,event.weight)

        #MomId of GEN lepton
        for i in range(0,int(event.GENlep_id.size())):
            if event.GENlep_MomId[i] == 999888 and abs(event.GENlep_id[i]) == 13:
                self.writer.objs["MomId_GENlep"].Fill(0,event.weight)
            else:
                self.writer.objs["MomId_GENlep"].Fill(event.GENlep_MomId[i],event.weight)

        #delta R of GEN lepton to the closest other muon
        for i in range(0,int(event.GENlep_id.size())):
            event.deltaRGENclosestlep.append(-1)
        for i in range(0,int(event.GENlep_id.size())):
            dr = 10
            if abs(event.GENlep_id[i]) == 13:
                for j in range(0,int(event.GENlep_id.size())):
                    if abs(event.GENlep_id[j]) == 13:
                        temp = deltaR(event.GENlep_eta[i],event.GENlep_phi[i],event.GENlep_eta[j],event.GENlep_phi[j])
                        if temp < dr and i != j :
                            dr = temp
                if dr < 10:
                    #event.deltaRGENclosestlep.append(dr)
                    event.deltaRGENclosestlep[i] = dr
                else:
                    #event.deltaRGENclosestlep.append(-1)
                    event.deltaRGENclosestlep[i] = -1

        #Acceptance of sample
        for i in range(0,int(event.GENlep_id.size())):
            if abs(event.GENlep_id[i]) == 13:
                self.writer.objs["LepacptDem"].Fill(event.GENlep_pt[i],event.weight)
                if event.GENlep_pt[i] > 5.0 and abs(event.GENlep_eta[i]) < 2.4:
                    self.writer.objs["LepacptNum"].Fill(event.GENlep_pt[i],event.weight)

        #event cumulative efficiency 
        for i in range(0,int(event.GENlep_id.size())):
            if event.GENlep_MomId[i] == 23 or event.GENlep_MomId[i] == 999888 and abs(event.GENlep_id[i]) == 13:
                if event.GENlep_pt[i] > 5.0 and abs(event.GENlep_eta[i]) < 2.4:
                    lepnumber.append(i)

        #test for percentage of events with less than 4 lepton
        self.writer.objs["testEventDem"].Fill(0,event.weight)
        if len(lepnumber) < 4:
            self.writer.objs["testEventNum"].Fill(0,event.weight)
        if len(lepnumber) > 0:
            dembool = True
            if self.dataset.name not in ["zpToMuMu_M5_0" , "zpToMuMu_M1_0" , "zpToMuMu_M2_0" , "zpToMuMu_M3_0" , "zpToMuMu_M4_0"]:
                for i in lepnumber:
                    dr = 0.3
                    lepid = -1
                    genlepid = -1
                    for j in range(0,int(event.lep_pt.size())):
                        if abs(event.lep_matchedR03_PdgId[j]) == 13:
                            temp = deltaR(event.GENlep_eta[i],event.GENlep_phi[i],event.lep_eta[j],event.lep_phi[j])
                            if temp < 0.3 and temp < dr:
                                dr = temp
                                lepid = j
                                genlepid = i
                    if dr != 0.3 and lepid != -1 and genlepid != -1:
                        if event.lep_tightId[lepid] and event.lep_RelIsoNoFSR[lepid] < 0.35:
                            recolepnumber.append(lepid)
                if len(recolepnumber) == 4:
                    numbool = True
                if dembool == True:
                    self.writer.objs["EventeffDem"].Fill(0,event.weight)
                if numbool == True:
                    self.writer.objs["EventeffNum"].Fill(0,event.weight)

            elif self.dataset.name in ["zpToMuMu_M5_0" , "zpToMuMu_M1_0" , "zpToMuMu_M2_0" , "zpToMuMu_M3_0" , "zpToMuMu_M4_0"]:
                for i in lepnumber:
                    dr = 0.3
                    lepid = -1
                    genlepid = -1
                    for j in range(0,int(event.lep_pt.size())):
                        if abs(event.lep_matchedR03_PdgId[j]) == 13:
                            temp = deltaR(event.GENlep_eta[i],event.GENlep_phi[i],event.lep_eta[j],event.lep_phi[j])
                            if temp < 0.2 and temp < dr:
                                dr = temp
                                lepid = j
                                genlepid = i
                    if dr != 0.3 and lepid != -1 and genlepid != -1:
                        if event.lep_tightId[lepid] and event.lep_RelIsoNoFSR[lepid] < 0.35:
                            recolepnumber.append(lepid)
                if len(recolepnumber) == 4:
                    numbool = True
                if dembool == True:
                    self.writer.objs["EventeffDem"].Fill(0,event.weight)
                if numbool == True:
                    self.writer.objs["EventeffNum"].Fill(0,event.weight)
        
        """
        #lepton full efficiency
        if self.dataset.name not in ["zpToMuMu_M5_0" , "zpToMuMu_M1_0" , "zpToMuMu_M2_0" , "zpToMuMu_M3_0" , "zpToMuMu_M4_0"]:
            for i in range(0,int(event.GENlep_id.size())):
                if event.GENlep_MomId[i] == 23 or event.GENlep_MomId[i] == 999888:
                    if event.GENlep_pt[i] > 5.0 and abs(event.GENlep_eta[i]) < 2.4:
                        dr = 0.3
                        lepid = -1
                        genlepid = -1
                        self.writer.objs["LepeffDem_pt"].Fill(event.GENlep_pt[i],event.weight)
                        self.writer.objs["LepeffDem_eta"].Fill(event.GENlep_eta[i],event.weight)
                        self.writer.objs["LepeffDem_dr"].Fill(event.deltaRGENclosestlep[i],event.weight)
                        for j in range(0,int(event.lep_pt.size())):
                            temp = deltaR(event.GENlep_eta[i],event.GENlep_phi[i],event.lep_eta[j],event.lep_phi[j])
                            if temp < 0.3 and temp < dr:
                                dr = temp
                                lepid = j
                                genlepid = i
                        if dr != 0.3 and lepid != -1 and genlepid != -1:
                            if  event.lep_tightId[lepid] and event.lep_RelIsoNoFSR[lepid] < 0.35:
                                self.writer.objs["LepeffNum_pt"].Fill(event.GENlep_pt[i],event.weight)
                                self.writer.objs["LepeffNum_eta"].Fill(event.GENlep_eta[i],event.weight)
                                self.writer.objs["LepeffNum_dr"].Fill(event.deltaRGENclosestlep[i],event.weight)

        elif self.dataset.name in ["zpToMuMu_M5_0" , "zpToMuMu_M1_0" , "zpToMuMu_M2_0" , "zpToMuMu_M3_0" , "zpToMuMu_M4_0"]:
            for i in range(0,int(event.GENlep_id.size())):
                if event.GENlep_MomId[i] == 23 or event.GENlep_MomId[i] == 999888:
                    if event.GENlep_pt[i] > 5.0 and abs(event.GENlep_eta[i]) < 2.4:
                        dr = 0.3
                        lepid = -1
                        genlepid = -1
                        self.writer.objs["LepeffDem_pt"].Fill(event.GENlep_pt[i],event.weight)
                        self.writer.objs["LepeffDem_eta"].Fill(event.GENlep_eta[i],event.weight)
                        self.writer.objs["LepeffDem_dr"].Fill(event.deltaRGENclosestlep[i],event.weight)
                        for j in range(0,int(event.lep_pt.size())):
                            temp = deltaR(event.GENlep_eta[i],event.GENlep_phi[i],event.lep_eta[j],event.lep_phi[j])
                            if temp < 0.2 and temp < dr:
                                dr = temp
                                lepid = j
                                genlepid = i
                        if dr != 0.3 and lepid != -1 and genlepid != -1:
                            if event.lep_tightId[lepid] and event.lep_RelIsoNoFSR[lepid] < 0.35:
                                self.writer.objs["LepeffNum_pt"].Fill(event.GENlep_pt[i],event.weight)
                                self.writer.objs["LepeffNum_eta"].Fill(event.GENlep_eta[i],event.weight)
                                self.writer.objs["LepeffNum_dr"].Fill(event.deltaRGENclosestlep[i],event.weight)
        """

        #lepton full efficiency for events have four lepton from Z/Zprime
        if len(lepnumber) == 4:
            if self.dataset.name not in ["zpToMuMu_M5_0" , "zpToMuMu_M1_0" , "zpToMuMu_M2_0" , "zpToMuMu_M3_0" , "zpToMuMu_M4_0"]:
                for i in lepnumber:
                    if event.GENlep_MomId[i] == 23 or event.GENlep_MomId[i] == 999888:
                        if event.GENlep_pt[i] > 5.0 and abs(event.GENlep_eta[i]) < 2.4:
                            dr = 0.3
                            lepid = -1
                            genlepid = -1
                            self.writer.objs["LepeffDem_pt"].Fill(event.GENlep_pt[i],event.weight)
                            self.writer.objs["LepeffDem_eta"].Fill(event.GENlep_eta[i],event.weight)
                            self.writer.objs["LepeffDem_dr"].Fill(event.deltaRGENclosestlep[i],event.weight)
                            for j in range(0,int(event.lep_pt.size())):
                                if abs(event.lep_matchedR03_PdgId[j]) == 13:
                                    temp = deltaR(event.GENlep_eta[i],event.GENlep_phi[i],event.lep_eta[j],event.lep_phi[j])
                                    if temp < 0.3 and temp < dr:
                                        dr = temp
                                        lepid = j
                                        genlepid = i
                            if dr != 0.3 and lepid != -1 and genlepid != -1:
                                if  event.lep_tightId[lepid] and event.lep_RelIsoNoFSR[lepid] < 0.35:
                                    self.writer.objs["LepeffNum_pt"].Fill(event.GENlep_pt[i],event.weight)
                                    self.writer.objs["LepeffNum_eta"].Fill(event.GENlep_eta[i],event.weight)
                                    self.writer.objs["LepeffNum_dr"].Fill(event.deltaRGENclosestlep[i],event.weight)

            elif self.dataset.name in ["zpToMuMu_M5_0" , "zpToMuMu_M1_0" , "zpToMuMu_M2_0" , "zpToMuMu_M3_0" , "zpToMuMu_M4_0"]:
                for i in lepnumber:
                    if event.GENlep_MomId[i] == 23 or event.GENlep_MomId[i] == 999888:
                        if event.GENlep_pt[i] > 5.0 and abs(event.GENlep_eta[i]) < 2.4:
                            dr = 0.3
                            lepid = -1
                            genlepid = -1
                            self.writer.objs["LepeffDem_pt"].Fill(event.GENlep_pt[i],event.weight)
                            self.writer.objs["LepeffDem_eta"].Fill(event.GENlep_eta[i],event.weight)
                            self.writer.objs["LepeffDem_dr"].Fill(event.deltaRGENclosestlep[i],event.weight)
                            for j in range(0,int(event.lep_pt.size())):
                                if abs(event.lep_matchedR03_PdgId[j]) == 13:
                                    temp = deltaR(event.GENlep_eta[i],event.GENlep_phi[i],event.lep_eta[j],event.lep_phi[j])
                                    if temp < 0.2 and temp < dr:
                                        dr = temp
                                        lepid = j
                                        genlepid = i
                            if dr != 0.3 and lepid != -1 and genlepid != -1:
                                if event.lep_tightId[lepid] and event.lep_RelIsoNoFSR[lepid] < 0.35:
                                    self.writer.objs["LepeffNum_pt"].Fill(event.GENlep_pt[i],event.weight)
                                    self.writer.objs["LepeffNum_eta"].Fill(event.GENlep_eta[i],event.weight)
                                    self.writer.objs["LepeffNum_dr"].Fill(event.deltaRGENclosestlep[i],event.weight)

        #for i in range (0,4):
            #if abs(event.lep_matchedR03_PdgId[event.lep_Hindex[i]]) == 13:
                #self.writer.objs["LepeffDem"].Fill(event.lep_pt[event.lep_Hindex[i]],event.lep_eta[event.lep_Hindex[i]],event.weight)
                #if event.lep_tightId[event.lep_Hindex[i]] and event.lep_RelIsoNoFSR[event.lep_Hindex[i]] < 0.35:
                    #self.writer.objs["LepeffNum"].Fill(event.lep_pt[event.lep_Hindex[i]],event.lep_eta[event.lep_Hindex[i]],event.weight)

            #if abs(jet.hadronFlavour) == 4:
                #self.writer.objs["CTageffDem"].Fill(jet.pt,jet.eta,event.weight)
                #if jet.btagCSVV2 > 0.8484:
                    #self.writer.objs["CTageffNum"].Fill(jet.pt,jet.eta,event.weight)

            #if abs(jet.hadronFlavour) == 0:
                #self.writer.objs["LTageffDem"].Fill(jet.pt,jet.eta,event.weight)
                #if jet.btagCSVV2 > 0.8484:
                    #self.writer.objs["LTageffNum"].Fill(jet.pt,jet.eta,event.weight)

        #delta R between GEN lepton and matched RECO lepton
        for i in range(0,int(event.GENlep_id.size())):
            dr = 1
            for j in range(0,int(event.lep_pt.size())):
                temp = deltaR(event.GENlep_eta[i],event.GENlep_phi[i],event.lep_eta[j],event.lep_phi[j])
                if temp < dr:
                    dr = temp
            if dr < 1:
                event.deltaRGENrecolep.append(dr)
        
        return True
