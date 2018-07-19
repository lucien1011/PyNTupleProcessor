import ROOT,pprint,sys

inputFile = ROOT.TFile(sys.argv[1],"READ")
tree = inputFile.Get("tree")
branches = [br.GetName() for br in tree.GetListOfBranches()]
pprint.pprint(branches)
