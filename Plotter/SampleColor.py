import ROOT

# Sample colours 
sampleColorDict = { 
                # SUSY 
                "T_tch":ROOT.kAzure-2,
                "TBar_tWch":ROOT.kAzure-2,
                "TToLeptons_sch":ROOT.kAzure-2,
                "T_tWch":ROOT.kAzure-2,
                "SingleTop":ROOT.kAzure-2,

                "TT_Powheg":ROOT.kAzure-4,
                "TT_pow":ROOT.kAzure-4,
                "DYJetsToLL_M50_LO":ROOT.kSpring+2,
                "DYJetsToLL_M50_NLO":ROOT.kSpring+2,
                "TTJets":ROOT.kAzure-4,

                "DYJetsToLL_M50":ROOT.kSpring+2,
                "DYJetsToLL_M10to50":ROOT.kSpring+2,
                "DYJets":ROOT.kSpring+2,

                "WZTo3LNu":ROOT.kViolet-1,
                "ZGTo2LG":ROOT.kViolet-1,
                "Diboson":ROOT.kViolet-1,

                "WJetsToLNu":ROOT.kSpring+4,
                "WJets":ROOT.kSpring+4,

                "ttWJets":ROOT.kSpring+6,
                "ttZJets":ROOT.kSpring+6,
                "TTV":ROOT.kSpring+6,

                "WWZ":ROOT.kBlue,
                "WZZ":ROOT.kBlue,
                "ZZZ":ROOT.kBlue,
                "WWW_4f":ROOT.kBlue,
                "LQToBL_mLQ500":ROOT.kRed,
                
                #RA5
                "DYJetsToLL_M10to50_LO":ROOT.kSpring+2,
                "DYJetsToLL_M50_LO_ext":ROOT.kSpring+2,
                "TGJets":ROOT.kAzure-2,
                "TTGJets":ROOT.kAzure-2,
                "TTHnobb_pow":ROOT.kAzure-4,
                "TTWToLNu_ext":ROOT.kAzure-4,
                "TTZToLLNuNu":ROOT.kSpring+6,
                "TTZToLLNuNu_m1to10":ROOT.kSpring+6,
                "VHToNonbb":ROOT.kSpring+4,
                "WGToLNuG":ROOT.kBlue,
                "WJetsToLNu_LO":ROOT.kBlue,
                "WWDoubleTo2L":ROOT.kBlue,
                "WZTo3LNu":ROOT.kBlue,
                "Non-prompt": ROOT.kGray, 
                "WZ": ROOT.kOrange-2,
                "ttVorH": ROOT.kGreen+2,    
                "ttW": ROOT.kBlue+2,
                "gamma+X": ROOT.kViolet+10,
                "WW": ROOT.kOrange+8,
                "Minor": ROOT.kPink+6,
                "QCD": ROOT.kOrange+4,
                "TTWW": ROOT.kRed+4,
                "SMS-T1qqqqL_mGluino1000": ROOT.kRed,
                "SMS-T1qqqqL_1000": ROOT.kRed,
                "SMS-T1qqqqL_1500": ROOT.kRed+1,
                "SMS-T1qqqqL_2000": ROOT.kRed+2,
                "SMS-T1qqqqL_2500": ROOT.kRed+3,
                "SMS-T1tbs_mGluino1000": ROOT.kBlue+2,
                "SMS-T1tbs_mGluino1500": ROOT.kBlue+3,
                "SMS-T1tbs_1000": ROOT.kBlue+2,
                "SMS-T1tbs_1500": ROOT.kBlue+3,

                # Dark Z
                #"ggH": ROOT.kAzure+1,
                "Higgs": ROOT.kAzure-2,
                "ggH": ROOT.kAzure-2,
                "VBF": ROOT.kSpring+2,
                "ZH": ROOT.kSpring+2,
                "WHplus": ROOT.kSpring+4,
                "WHminus": ROOT.kSpring+4,
                "WH": ROOT.kSpring+4,
                "ZH": ROOT.kSpring+4,
                #"ZPlusX": ROOT.kYellow-2,
                "ZPlusX": ROOT.kGreen,
                "qqZZ": ROOT.kBlue+2,
                "ZZ": ROOT.kBlue+2,
                #"qqZZ": ROOT.kRed,
                "ggZZ": ROOT.kBlue,
                "WWZ": ROOT.kViolet, 
                "ttZ": ROOT.kSpring+4, 
                #"ggZZTo4L": ROOT.kBlue-5,
                "ggZZTo4L": ROOT.kBlue,
                "qqZZTo4L": ROOT.kBlue+2,
                "HZZd_M4": ROOT.kRed,
                "HZZd_M7": ROOT.kRed+1,
                "HZZd_M10": ROOT.kRed+2,
                "HZZd_M15": ROOT.kRed+3,
                "HZZd_M20": ROOT.kOrange+4,
                "HZZd_M25": ROOT.kOrange+5,
                "HZZd_M30": ROOT.kOrange+6,
                "HZZd_M35": ROOT.kOrange+7,
                "DarkSUSY_mH_125_mN1_10_mGammaD_8p5_cT_0": ROOT.kRed,
                "HToZdZd_MZD4": ROOT.kViolet-5,
                "HToZdZd_MZD5": ROOT.kViolet-3,
                "HToZdZd_MZD6": ROOT.kViolet-1,
                "HToZdZd_MZD7": ROOT.kViolet+1,
                "HToZdZd_MZD8": ROOT.kViolet+3,
                "HToZdZd_MZD9": ROOT.kViolet+5,
                "HToZdZd_MZD10": ROOT.kViolet+7,
                "HToZdZd_MZD15": ROOT.kViolet+9,
                "HToZdZd_MZD20": ROOT.kViolet-3,
                "HToZdZd_MZD25": ROOT.kViolet-3,
                "HToZdZd_MZD30": ROOT.kOrange-5,
                "HToZdZd_MZD35": ROOT.kOrange-3,
                "HToZdZd_MZD40": ROOT.kOrange-1,
                "HToZdZd_MZD45": ROOT.kOrange+1,
                "HToZdZd_MZD50": ROOT.kOrange+3,
                "HToZdZd_MZD55": ROOT.kOrange+5,
                "HToZdZd_MZD60": ROOT.kOrange+7,
                "HToZdZd_M4": ROOT.kViolet-5,
                "HToZdZd_M5": ROOT.kViolet-3,
                "HToZdZd_M6": ROOT.kViolet-1,
                "HToZdZd_M7": ROOT.kViolet+1,
                "HToZdZd_M8": ROOT.kViolet+3,
                "HToZdZd_M9": ROOT.kViolet+5,
                "HToZdZd_M10": ROOT.kViolet+7,
                "HToZdZd_M15": ROOT.kViolet+9,
                "HToZdZd_M20": ROOT.kViolet-3,
                "HToZdZd_M25": ROOT.kViolet-3,
                "HToZdZd_M30": ROOT.kOrange-5,
                "HToZdZd_M35": ROOT.kOrange-3,
                "HToZdZd_M40": ROOT.kOrange-1,
                "HToZdZd_M45": ROOT.kOrange+1,
                "HToZdZd_M50": ROOT.kOrange+3,
                "HToZdZd_M55": ROOT.kOrange+5,
                "HToZdZd_M60": ROOT.kOrange+7,
                "PredCR": ROOT.kRed,
                "WFC_Reducible": ROOT.kGreen,
                "WFC_Irreducible": ROOT.kBlue,
                "ppZZd4l_M4": ROOT.kTeal,
                "ppZZd4l_M5": ROOT.kTeal+1,
                #"ppZZd4l_M15": ROOT.kTeal+2,
                #"ppZZd4l_M30": ROOT.kTeal+4,
                "ppZZd4l_M15": ROOT.kOrange+2,
                "ppZZd4l_M30": ROOT.kRed,
                
                # HZZ4l 
                "WrongFC_Reducible": ROOT.kGreen,
                "WrongFC_Irreducible": ROOT.kBlue,

                #Zprime
                "zpToMuMu_M5": ROOT.kOrange+1,
                "zpToMuMu_M10": ROOT.kOrange+2,
                "zpToMuMu_M15": ROOT.kOrange+3,
                "zpToMuMu_M20": ROOT.kOrange+4,
                "zpToMuMu_M30": ROOT.kOrange+5,
                "zpToMuMu_M40": ROOT.kOrange+6,
                "zpToMuMu_M50": ROOT.kOrange+7,
                "zpToMuMu_M60": ROOT.kOrange+8,
                "zpToMuMu_M70": ROOT.kOrange+9,
                "WmTo3munu_ZpM45": ROOT.kRed,
                "WpTo3munu_ZpM45": ROOT.kGreen,
                "WmTo3munu_ZpM15": ROOT.kOrange,
                "WpTo3munu_ZpM15": ROOT.kBlue,
                "WZTo3LNu_memCR": ROOT.kGreen,
                "DYJetsToLL_M50_memCR": ROOT.kViolet,
                "DYJetsToLL_M10To50_memCR": ROOT.kBlue,
                "TTJets_memCR": ROOT.kRed,
                "TTJets_fromT": ROOT.kOrange,
                "TTJets_notfromT": ROOT.kBlue,
}
