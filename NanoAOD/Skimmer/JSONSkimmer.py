import json, os, ROOT
from os import environ

from Utils.LumiList import LumiList

from Core.Module import Module


# *********************************************************************************************
# *                                           JSONSkimmer                                     *
# *                                                                                           *
# *                                                                                           *
# * Apply a json filter, and creates an RLTInfo TTree.                                        *
# * See PhysicsTools.HeppyCore.utils.RLTInfo for more information                             *
# *                                                                                           *
# *    The path of the json file to be used is set as a component attribute.                  *
# *                                                                                           *
# *    The process function returns:                                                          *
# *      - True if                                                                            *
# *         - the component is MC or                                                          *
# *         - if the run/lumi pair is in the JSON file                                        *
# *         - if the json file was not set for this component                                 *
# *      - False if the component is MC                                                       *
# *          and if the run/lumi pair is not in the JSON file.                                *
# *                                                                                           *
# *********************************************************************************************

class JSONSkimmer(Module):
    def __init__(self, name):
        super(JSONSkimmer, self).__init__(name)
        pass

    def begin(self):
        if self.dataset.isData:
            if self.dataset.json is None:
                raise ValueError('component {cname} is not MC, and contains no JSON file. Either remove the JSONSkimmer from the sequence or set the "json" attribute of this component'.format(cname=self.dataset.name))
            self.lumiList = LumiList(os.path.expandvars(self.dataset.json))
        else:
            self.lumiList = None
            pass
        #self.rltInfo = RLTInfo()
        pass
       
    def analyze(self,event):
        if self.dataset.isMC:
            return True
        if self.lumiList is None:
            return True
        if self.lumiList.contains(event.run[0],event.luminosityBlock[0]):
            return True
        else:
            return False
