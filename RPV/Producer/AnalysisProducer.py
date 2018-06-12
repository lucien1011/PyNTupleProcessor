from Core.Module import Module
import numpy

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
 
        k1 = numpy.sqrt(numpy.square(numpy.sqrt(numpy.square(event.jets[0].pt)+numpy.square(event.jets[0].mass))+numpy.sqrt(numpy.square(event.leps[0].pt)+numpy.square(event.leps[0].mass))) - numpy.square(event.jets[0].pt-event.leps[0].pt))
        k2 = numpy.sqrt(numpy.square(numpy.sqrt(numpy.square(event.jets[1].pt)+numpy.square(event.jets[1].mass))+numpy.sqrt(numpy.square(event.leps[1].pt)+numpy.square(event.leps[1].mass))) - numpy.square(event.jets[1].pt-event.leps[1].pt))
        k3 = numpy.sqrt(numpy.square(numpy.sqrt(numpy.square(event.jets[0].pt)+numpy.square(event.jets[0].mass))+numpy.sqrt(numpy.square(event.leps[1].pt)+numpy.square(event.leps[1].mass))) - numpy.square(event.jets[0].pt-event.leps[1].pt))
        k4 = numpy.sqrt(numpy.square(numpy.sqrt(numpy.square(event.jets[1].pt)+numpy.square(event.jets[1].mass))+numpy.sqrt(numpy.square(event.leps[0].pt)+numpy.square(event.leps[0].mass))) - numpy.square(event.jets[1].pt-event.leps[0].pt))
        
        if k1 >= k2:
           event.m0_bl[0] = k1
           event.m1_bl[0] = k2
        else:
            event.m0_bl[0] = k2
            event.m1_bl[0] = k1

        if k3 >= k4:
           event.m0_bl[1] = k3
           event.m1_bl[1] = k4
        else:
            event.m0_bl[1] = k4
            event.m1_bl[1] = k3

        temp1 = (event.m0_bl[0] - event.m1_bl[0])/(event.m0_bl[0] + event.m1_bl[0])
        temp2 = (event.m0_bl[1] - event.m1_bl[1])/(event.m0_bl[1] + event.m1_bl[1])

        if temp1 < temp2:
           event.m_asym_bl = temp1
        else:
            event.m_asym_bl = temp2













        return True
