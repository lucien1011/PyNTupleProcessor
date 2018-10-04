from Core.Sequence import Sequence

from RA5.Weighter.XSWeighter import XSWeighter
from RA5.LeptonJetRecleaner.EventProducer import LeptonJetProducer 
from RA5.Skimmer.BaselineSkimmer import BaselineSkimmer
from RA5.Skimmer.TightLooseSkimmer import TightLooseSkimmer
from RA5.Skimmer.GammaCRSkimmer import GammaCRSkimmer,GammaCRTreeSkimmer
from RA5.Skimmer.SyncSkimmer import SyncSkimmer
from RA5.Skimmer.METSkimmer import METSkimmer
from RA5.Skimmer.LLHtSkimmer import LLHtSkimmer
from RA5.Skimmer.HLTSkimmer import HLTSkimmer
from RA5.Skimmer.RPVSkimmer import RPVSkimmer
from RA5.Producer.CategoryProducer import CategoryProducer,LeptonCatProducer
from RA5.Producer.NJet40Producer import NJet40Producer
from RA5.Producer.LeptonProducer import LeptonProducer
from RA5.Producer.JetProducer import JetProducer
from RA5.Producer.PhotonProducer import PhotonProducer
from RA5.Producer.SRProducer import SRProducer
from RA5.Producer.VariableProducer import VariableProducer

from NanoAOD.Skimmer.METFilter import METFilter

from RA5.Weighter.HLTWeighter import HLTWeighter

lepCats = ["HH","HL","LL"]

xsWeighter              = XSWeighter("XSWeighter")

baselineSkimmer         = BaselineSkimmer("BaselineSkimmer")
tightLooseSkimmer       = TightLooseSkimmer("TightLooseSkimmer")
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
gammaCRSkimmer          = GammaCRSkimmer("GammaCRSkimmer")
gammaCRTreeSkimmer      = GammaCRTreeSkimmer("GammaCRSkimmer")

leptonJetProducer       = LeptonJetProducer("LeptonJetProducer","Run2016")
#leptonCatProducer       = LeptonCatProducer("CategoryProducer")
leptonCatProducer       = SRProducer("CategoryProducer")
nJet40Producer          = NJet40Producer("NJet40Producer")
leptonProducer          = LeptonProducer("LeptonProducer")
jetProducer             = JetProducer("JetProducer")
phoProducer             = PhotonProducer("PhotonProducer")
variableProducer        = VariableProducer("VariableProducer")

hltWeighter             = HLTWeighter("HLTWeighter")
tightLooseHLTWeighter   = HLTWeighter("HLTWeighter",cutflow="TightLoose")

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

tl_sr_sequence = Sequence()
tl_sr_sequence.add(metFilter)
tl_sr_sequence.add(metSkimmer)
tl_sr_sequence.add(leptonProducer)
tl_sr_sequence.add(jetProducer)
tl_sr_sequence.add(tightLooseSkimmer)
tl_sr_sequence.add(hltSkimmer)
tl_sr_sequence.add(xsWeighter)
tl_sr_sequence.add(tightLooseHLTWeighter)

tl_rpv_sequence = Sequence()
tl_rpv_sequence.add(metFilter)
tl_rpv_sequence.add(leptonProducer)
tl_rpv_sequence.add(jetProducer)
tl_rpv_sequence.add(tightLooseSkimmer)
tl_rpv_sequence.add(hltSkimmer)
tl_rpv_sequence.add(xsWeighter)
tl_rpv_sequence.add(tightLooseHLTWeighter)
tl_rpv_sequence.add(variableProducer)

tl_rpv_skim_sequence = Sequence()
tl_rpv_skim_sequence.add(metFilter)
tl_rpv_skim_sequence.add(leptonProducer)
tl_rpv_skim_sequence.add(jetProducer)
tl_rpv_skim_sequence.add(tightLooseSkimmer)
#tl_rpv_skim_sequence.add(hltSkimmer)

gamma_cr_skim_sequence = Sequence()
gamma_cr_skim_sequence.add(metFilter)
gamma_cr_skim_sequence.add(leptonProducer)
gamma_cr_skim_sequence.add(jetProducer)
gamma_cr_skim_sequence.add(phoProducer)
gamma_cr_skim_sequence.add(gammaCRTreeSkimmer)

sync_sequence = Sequence()
sync_sequence.add(leptonProducer)
sync_sequence.add(jetProducer)
#sr_sequence.add(leptonCatProducer)
sync_sequence.add(syncSkimmer)
#sr_sequence.add(llHtSkimmer)

