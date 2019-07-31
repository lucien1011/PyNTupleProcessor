import ROOT,glob,os

inputDir = "/eos/uscms/store/user/lpcljm/FWLJMET102X_1lep2017_052219/ST_s-channel_top_leptonDecays_13TeV-PSweights_powheg-pythia/singleLep2017/190527_201559/000*/"

sumw = 0.
for d in glob.glob(inputDir):
    for f in os.listdir(d):
        if ".root" not in f: continue
        inputFile = ROOT.TFile.Open(os.path.join(d,f),"READ")
        #hist = inputFile.Get("ljmet/MultiLepSelector/nEvents")
        hist = inputFile.Get("mcweightanalyzer/weightHist")
        sumw += hist.GetBinContent(hist.GetXaxis().FindBin(1))
        print d,f,[hist.GetBinContent(i) for i in range(1,hist.GetNbinsX()+1)],sumw
        inputFile.Close()
print sumw
