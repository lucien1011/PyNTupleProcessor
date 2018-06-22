from Core.Module import Module
import numpy
import math

class AnalysisProducer(Module):
    def analyze(self,event):
        event.muons = [p for p in event.MediumMuons if p.pt > 40]
        event.muons.sort(key=lambda x: x.pt,reverse=True)

        event.eles = [p for p in event.MediumElectrons if p.pt > 40]
        event.eles.sort(key=lambda x: x.pt,reverse=True)
        
        event.leps = event.muons + event.eles
        event.leps.sort(key=lambda x: x.pt,reverse=True)
        event.nLep40 = len(event.leps)

        event.jets = [p for p in event.LooseJets if p.pt > 40]
        event.jets.sort(key=lambda x: x.pt,reverse=True)
        event.nJet40 = len(event.jets)

        event.ht40 = 0.
        for ps in [event.jets,event.leps]:
            for p in ps:
                event.ht40 += p.pt
        
        if event.nLep40 >= 2:
            vecSum = event.leps[0].p4() + event.leps[1].p4()
            event.mll = vecSum.M()
        else:
            event.mll = None

        if len(event.jets) >= 2 and len(event.leps) >= 2: 
            event.m_ct = [numpy.sqrt(numpy.square(numpy.sqrt(numpy.square(event.jets[0].pt)+numpy.square(event.jets[0].mass))+numpy.sqrt(numpy.square(event.jets[1].pt)+numpy.square(event.jets[1].mass))) - numpy.square(event.jets[0].pt-event.jets[1].pt))]
            
            vecsum1 = event.leps[0].p4() + event.jets[0].p4()
            l1 = vecsum1.M()
            vecsum2 = event.leps[1].p4() + event.jets[1].p4()
            l2 = vecsum2.M()
            vecsum3 = event.leps[1].p4() + event.jets[0].p4()
            l3 = vecsum3.M()
            vecsum4 = event.leps[0].p4() + event.jets[1].p4()
            l4 = vecsum4.M()

            if l1 >= l2 and l3 >= l4:
               event.m0_bl = [l1,l3]
               event.m1_bl = [l2,l4]
            elif l1 >= l2 and l3 < l4:
                event.m0_bl = [l1,l4]
                event.m1_bl = [l2,l3]
            elif l1 < l2 and l3 >= l4:
                event.m0_bl = [l2,l3]
                event.m1_bl = [l1,l4]
            elif l1 < l2 and l3 < l4:
                event.m0_bl = [l2,l4]
                event.m1_bl = [l1,l3]

            temp1 = (event.m0_bl[0] - event.m1_bl[0])/(event.m0_bl[0] + event.m1_bl[0])
            temp2 = (event.m0_bl[1] - event.m1_bl[1])/(event.m0_bl[1] + event.m1_bl[1])

            if temp1 < temp2:
               event.m_asym_bl = [temp1]
               event.m0_bl = [event.m0_bl[0]]
               event.m1_bl = [event.m1_bl[0]]
            else:
                event.m_asym_bl = [temp2]
                event.m0_bl = [event.m0_bl[1]]
	        event.m1_bl = [event.m1_bl[1]]
        else:
            event.m_ct = -1
            event.m0_b1 = -1
            event.m1_b1 = -1

        for j in event.jets:
            muEnergy = event.Muon_pt[j.muonIdx1] + event.Muon_pt[j.muonIdx2]
            j.muEF = muEnergy/(j.pt*(1-j.rawFactor))
       
        if len(event.jets) >= 2 and len(event.leps) >= 2:
           dphi = [abs(event.jets[0].phi- event.leps[0].phi), abs(event.jets[0].phi- event.leps[1].phi), abs(event.jets[1].phi- event.leps[0].phi), abs(event.jets[1].phi- event.leps[1].phi)]
           
           for i in range(0,3):
	       if dphi[i] > 180:
	          dphi[i] = 360 - dphi[i]
               dphi[i] = math.pi*dphi[i]/180

           deta = [abs(event.jets[0].eta- event.leps[0].eta), abs(event.jets[0].eta- event.leps[1].eta), abs(event.jets[1].eta- event.leps[0].eta), abs(event.jets[1].eta- event.leps[1].eta)]

           dR = [0,0,0,0]    
 
           for i in range(0,3):
               dR[i] = numpy.sqrt(numpy.square(dphi[i]) + numpy.square(deta[i]))

           event.dR_jets_leps = 0

           for i in range(0,3):
	       temp = dR[i]
	       if event.dR_jets_leps == 0 or event.dR_jets_leps > temp:
	          event.dR_jets_leps = temp

        return True
