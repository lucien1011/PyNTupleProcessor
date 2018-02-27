# Lucien Lo <lucienlo@cern.ch>

##____________________________________________________________________________||
import os

##____________________________________________________________________________||
class FileInfo(object):
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path).replace(".root","")

    def uberftp_path(self):
        return "root://cmsio2.rc.ufl.edu/"+self.path.replace("/cms/data","")

