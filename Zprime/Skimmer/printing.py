from __future__ import division
from Core.Module import Module
import numpy

class printing(Module):
    def __init__(self,name,cutflow="Zprime-SR"):
        super(printing,self).__init__(name)
        self.cutflow = cutflow

    def analyze(self,event):
        if self.cutflow == "Zprime-SR":
            print "---event---"
            for i in range(0,int(event.GENlep_id.size())):
                if abs(event.GENlep_id[i]) == 13:
                    print event.GENlep_MomId[i]
            #if event.mass4l[0] < 80. or event.mass4l[0] > 100.: return False
            #if event.mass4l[0] < 100.: return False
            #if event.mass4l[0] > 120.: return False
            #if event.mass4l[0] < 118. or event.mass4l[0] > 130.: return False
            #if event.massZ1[0] < 12. or event.massZ1[0] > 120.: return False
            #if event.massZ2[0] < 1. or event.massZ2[0] > 120.: return False
            #if "ZPlusX" not in self.dataset.name and not event.passedFullSelection[0]: return False
            #if event.nZXCRFailedLeptons[0] != 1: return False
            #if event.nZXCRFailedLeptons[0] != 2: return False
            return True
        return False
