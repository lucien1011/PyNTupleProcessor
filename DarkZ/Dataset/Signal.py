
from Core.NanoAODResult.Component import Component

gensim_component = Component(
        "/cms/data/store/user/klo/DarkPhoton_Moriond17_GEN-SIM/v2/ZD_UpTo0j_MZD20_Eps1e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-GEN-SIM/180403_154314/0000/",
        "DarkZTo4l_v1",
        inUFTier2 = True,
        exclude = "inLHE",
        )

miniaod_component = Component(
        "/cms/data/store/user/klo/DarkPhoton_Moriond17_MINIAODSIM/v3/ZD_UpTo0j_MZD20_Eps1e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-MINIAODSIM/180417_165913/0000/",
        "DarkZTo4l_v1",
        inUFTier2 = True,
        )
