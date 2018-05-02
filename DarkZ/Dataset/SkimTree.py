from Core.Component import Component

skimTreeDir = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180425/SkimTree_v1/"

ggZZ_cmp = Component(
        skimTreeDir,
        "ggZZ",
        inUFTier2 = False,
        keyword = "GluGluToContinToZZTo4mu", 
        )
ggZZ_cmp.sumw = 662635.000000

qqZZ_cmp = Component(
        skimTreeDir,
        "qqZZ",
        inUFTier2 = False,
        keyword = "ZZTo4L", 
        )
qqZZ_cmp.sumw = 91818480.000000 + 6757228.000000

ggHZZd_M20_cmp = Component(
        skimTreeDir,
        "ggHZZd_M20",
        inUFTier2 = False,
        keyword = "ZD_UpTo0j_MZD20_Eps1e-2", 
        )
ggHZZd_M20_cmp.sumw = 67050.0 
ggHZZd_M20_cmp.xs = 4.823e+1*5e-5 

bkg_cmps = [
        ggZZ_cmp,
        qqZZ_cmp,
        ]

sig_cmps = [
        ggHZZd_M20_cmp
        ]
