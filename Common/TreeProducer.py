from Core.Module import Module
from collections import OrderedDict as odict
from array import array

class PyTree:
    def __init__(self,tree):
        self.tree = tree
        self._branches = {} ## must be the last line
    def branch(self,name,type,n=1,lenVar=None):
        arr = array(type.lower(), n*[0 if type in 'iI' else 0.]) 
        self._branches[name] = arr
        if n == 1:
            self.tree.Branch(name, arr, name+"/"+type.upper())
        else:
            if lenVar != None:
                self.tree.Branch(name, arr, "%s[%s]/%s" % (name,lenVar,type.upper()))
            else:
                self.tree.Branch(name, arr, "%s[%d]/%s" % (name,n,type.upper()))
    def __setattr__(self,name,val):
        if hasattr(self,'_branches'):
            arr = self._branches[name]
            if len(arr) == 1:
                arr[0] = val
            else:
                for i,v in enumerate(val):
                    if i >= len(arr): break
                    arr[i]  = v
        else:
            self.__dict__[name] = val
    def Fill(self):
        self.tree.Fill()

    def Write(self):
        self.tree.Write()

    def AutoSave(self):
        self.tree.AutoSave()

class TreeProducer(Module):
    """Outputs skimmed and/or slimmed tree to a root file.""" 

    def __init__( self, name,
            listOfBranchesToKeep=[],
            verbose=False, 
            branchesToAdd=[] ) :

        super(TreeProducer,self).__init__(name)
        self.branches               = None
        self.listOfBranchesToKeep   = listOfBranchesToKeep
        self.output                 = None
        self.clone                  = None
        self.verbose                = verbose
        self.branchesToAdd          = branchesToAdd

    def beginEvents(self,events) :
        tree     = events.tree
        if not self.listOfBranchesToKeep:
            branches = [ br.GetName() for br in tree.GetListOfBranches() ]
        else:
            branches = [ br.GetName() for br in tree.GetListOfBranches() if br.GetName() in self.listOfBranchesToKeep ]
        self.branches = odict()
        for branch in branches :
            try :
                self.branches[branch] = getattr(events,branch)
            except :
                print "Problem accessing branch '{:s}'".format(branch)

        self.clone      = PyTree(tree.CloneTree(0))
        
        self.branchArrayDict = {}
        for branchToAdd in self.branchesToAdd:
            self.clone.branch(*branchToAdd.getInit())
            #self.branchArrayDict[branchToAdd.eventAttrStr] = branchToAdd.getNewArray()
            #self.clone.Branch(branchToAdd.branchName,self.branchArrayDict[branchToAdd.eventAttrStr],branchToAdd.typeStr)

        tree.CopyAddresses(self.clone.tree)

    def analyze(self,event) :

        if self.verbose :
            for name,branch in self.branches.items() :
                print name,[x for x in branch]

        for branchToAdd in self.branchesToAdd:
            setattr(self.clone,branchToAdd.branchName,branchToAdd.getValue(event))
            #self.branchArrayDict[branchToAdd.eventAttrStr] = branchToAdd.getValue(event)
        
        self.clone.Fill()

        return True


    def end(self) :
        self.clone.Write()
        self.clone.AutoSave()
