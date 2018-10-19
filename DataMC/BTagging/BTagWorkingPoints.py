
# ====================================================================================================================================================
# Copied from Heppy: https://github.com/CMSRA1/cmg-cmssw-private/blob/RA1-CMGTools-from-CMSSW_7_2_3/PhysicsTools/Heppy/python/physicsobjects/Jet.py
# ====================================================================================================================================================

BTagWorkingPoints = {
        "TCHEL": ("trackCountingHighEffBJetTags", 1.7),
        "TCHEM": ("trackCountingHighEffBJetTags", 3.3),
        "TCHPT": ("trackCountingHighPurBJetTags", 3.41),
        "JPL": ("jetProbabilityBJetTags", 0.275),
        "JPM": ("jetProbabilityBJetTags", 0.545),
        "JPT": ("jetProbabilityBJetTags", 0.790),
        "CSVL": ("combinedSecondaryVertexBJetTags", 0.244),
        "CSVM": ("combinedSecondaryVertexBJetTags", 0.679),
        "CSVT": ("combinedSecondaryVertexBJetTags", 0.898),
        "CSVv2IVFL": ("combinedInclusiveSecondaryVertexV2BJetTags", 0.5426),
        "CSVv2IVFM": ("combinedInclusiveSecondaryVertexV2BJetTags", 0.8484),
        "CSVv2IVFT": ("combinedInclusiveSecondaryVertexV2BJetTags", 0.9535),
        "CMVAL": ("combinedMVABJetTags", 0.630), # for same b-jet efficiency of CSVv2IVFL on ttbar MC, jet pt > 30
        "CMVAM": ("combinedMVABJetTags", 0.732), # for same b-jet efficiency of CSVv2IVFM on ttbar MC, jet pt > 30
        "CMVAT": ("combinedMVABJetTags", 0.813), # for same b-jet efficiency of CSVv2IVFT on ttbar MC, jet pt > 30
        "DeepCSVL": ("DeepCSV",0.2219), # taken from https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation80XReReco#Supported_Algorithms_and_Operati
        "DeepCSVM": ("DeepCSV",0.6324),
        "DeepCSVT": ("DeepCSV",0.8958),
        }

def WorkingPoints(name):
    return {cut: BTagWorkingPoints[name+cut][1] for cut in ["L","M","T"]   }
