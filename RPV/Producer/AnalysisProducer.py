from Core.Module import Module
import numpy

class AnalysisProducer(Module):
    def analyze(self,event):#, mo_bl, m1_bl, m_asym_bl):
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
        else:
            event.m_asym_bl = [temp2]
        #event.m_asym_bl = 100*event.m_asym_bl







        return True
