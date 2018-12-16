from Core.Sequence import Sequence

from RA5.Weighter.XSWeighter import XSWeighter
from RA5.LeptonJetRecleaner.EventProducer import LeptonJetProducer 
from RA5.Skimmer.BaselineSkimmer import BaselineSkimmer
from RA5.Skimmer.tightlooseCRSkimmer import tightlooseCRSkimmer
from RA5.Skimmer.SyncSkimmer import SyncSkimmer
from RA5.Skimmer.METSkimmer import METSkimmer
from RA5.Skimmer.LLHtSkimmer import LLHtSkimmer
from RA5.Skimmer.HLTSkimmer import HLTSkimmer
from RA5.Skimmer.RPVSkimmer import RPVSkimmer
from RA5.Producer.CategoryProducer import CategoryProducer,LeptonCatProducer
from RA5.Producer.NJet40Producer import NJet40Producer
from RA5.Producer.LeptonProducer import LeptonProducer
from RA5.Producer.JetProducer import JetProducer

from NanoAOD.Skimmer.METFilter import METFilter

from RA5.Weighter.HLTWeighter import HLTWeighter

lepCats = ["HH","HL","LL"]

xsWeighter              = XSWeighter("XSWeighter")

baselineSkimmer         = BaselineSkimmer("BaselineSkimmer")
tightlooseCRSkimmer     = tightlooseCRSkimmer("tightlooseCRSkimmer")
syncSkimmer             = SyncSkimmer("SyncSkimmer")
metSkimmer              = METSkimmer("METSkimmer")
llHtSkimmer             = LLHtSkimmer("LLHtSkimmer")
hltSkimmer              = HLTSkimmer("HLTSkimmer",emulation=True)
rpvSkimmer              = RPVSkimmer("RPVSkimmer")
metFilter               = METFilter("METFilter",flags=[
        "Flag_HBHENoiseFilter",
        "Flag_HBHENoiseIsoFilter",
        "Flag_EcalDeadCellTriggerPrimitiveFilter",
        "Flag_goodVertices",
        "Flag_eeBadScFilter",
        # Reconstruction filters:
        #"Flag_muonBadTrackFilter",
        #"Flag_chargedHadronTrackResolutionFilter",
        "Flag_badChargedHadronFilter",
        "Flag_globalTightHalo2016Filter",
        # Moriond17 bad muons (temporary recipe from https://hypernews.cern.ch/HyperNews/CMS/get/physics-validation/2786.html)
        #"Flag_badMuonMoriond2017",
        #"Flag_badCloneMuonMoriond2017",
    ])

leptonJetProducer       = LeptonJetProducer("LeptonJetProducer","Run2016")
leptonCatProducer       = LeptonCatProducer("LeptonCatProducer")
nJet40Producer          = NJet40Producer("NJet40Producer")
leptonProducer          = LeptonProducer("LeptonProducer")
jetProducer             = JetProducer("JetProducer")

hltWeighter             = HLTWeighter("HLTWeighter")

sr_sequence = Sequence()
sr_sequence.add(metSkimmer)
sr_sequence.add(leptonProducer)
sr_sequence.add(jetProducer)
sr_sequence.add(baselineSkimmer)
sr_sequence.add(leptonCatProducer)
sr_sequence.add(llHtSkimmer)
sr_sequence.add(hltSkimmer)
sr_sequence.add(xsWeighter)

rpv_sequence = Sequence()
rpv_sequence.add(leptonProducer)
rpv_sequence.add(jetProducer)
rpv_sequence.add(metFilter)
rpv_sequence.add(baselineSkimmer)
rpv_sequence.add(leptonCatProducer)
rpv_sequence.add(llHtSkimmer)
rpv_sequence.add(hltSkimmer)
rpv_sequence.add(rpvSkimmer)
rpv_sequence.add(xsWeighter)
rpv_sequence.add(hltWeighter)

tightlooseCR_sequence = Sequence()
tightlooseCR_sequence.add(leptonProducer)
tightlooseCR_sequence.add(jetProducer)
tightlooseCR_sequence.add(metFilter)
tightlooseCR_sequence.add(tightlooseCRSkimmer)
#tightlooseCR_sequence.add(leptonCatProducer)
#tightlooseCR_sequence.add(llHtSkimmer)
#tightlooseCR_sequence.add(baselineSkimmer)
#tightlooseCR_sequence.add(hltSkimmer)
tightlooseCR_sequence.add(rpvSkimmer)
tightlooseCR_sequence.add(xsWeighter)
#tightlooseCR_sequence.add(hltWeighter)


sync_sequence = Sequence()
sync_sequence.add(leptonProducer)
sync_sequence.add(jetProducer)
#sr_sequence.add(leptonCatProducer)
sync_sequence.add(syncSkimmer)
#sr_sequence.add(llHtSkimmer)

