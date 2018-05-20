from Core.Module import Module
from collections import OrderedDict as odict
import ROOT as r
import os
import glob
import shutil
from array import array

class TreeProducer(Module):
    """Outputs skimmed and/or slimmed tree to a root file.""" 

    def __init__( self, name,
            filename="skim",
            keep=["keep *",],
            verbose=False ) :

        super(TreeProducer,self).__init__(name)
        self.filename = filename
        self.branches = None
        self.keep     = keep
        self.output   = None
        self.clone    = None
        self.verbose  = verbose

    def __str__( self ) :
        '''A useful printout'''

        str = "\n"
        str += " Output file: {:s},".format(self.filename)
        str += " Verbose: {:s}".format("True" if self.verbose else "False")
        return str


    def beginEvents(self,events) :
        tree     = events.tree
        #branches = [ br.GetName() for br in tree.GetListOfBranches() ]
        #self.branches = odict()
        #for branch in branches :
        #    try :
        #        self.branches[branch] = getattr(self.dataset.events,branch)
        #    except :
        #        print "Problem accessing branch '{:s}'".format(branch)

        self.clone      = tree.CloneTree(0)

        # ----------------------------------------
        # Add additional data to trees
        # ----------------------------------------
        #self.weight              = array( 'f', [ 1. ] )
        #self.nWTagged            = array( 'd', [ -1 ] )
        #self.clone.Branch("w",                   self.weight,             "w/F")
        #self.clone.Branch("nWTagged",            self.nWTagged,           "nWTagged/D")       

        tree.CopyAddresses(self.clone)

    def analyze(self,event) :

        #if self.verbose :
        #    for name,branch in self.branches.items() :
        #        print name,[x for x in branch]
        #        pass
        #    pass

        # ----------------------------------------
        # Store additional data
        # ----------------------------------------
        # Store event weight - CAUTION: This is the weight at the time of skimming and may change with new corrections!
        #self.weight[0]           = event.weight
        #if getattr(event, "nX", None) != None:
        #    self.nWTagged[0]            = getattr(event, 'nWTagged', 0.)[0]
        #else:
        #    self.nWTagged[0]            = 0.
        
        self.clone.Fill()

        return True


    def end(self) :
        self.clone.Write()
        self.clone.AutoSave()
