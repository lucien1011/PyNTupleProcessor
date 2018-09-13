from Core.Sequence import Sequence

from RA5.Weighter.XSWeighter import XSWeighter
from RA5.LeptonJetRecleaner.EventProducer import LeptonJetProducer 
from RA5.Skimmer.BaselineSkimmer import BaselineSkimmer
from RA5.Skimmer.SyncSkimmer import SyncSkimmer
from RA5.Skimmer.METSkimmer import METSkimmer
from RA5.Skimmer.LLHtSkimmer import LLHtSkimmer
from RA5.Skimmer.HLTSkimmer import HLTSkimmer
from RA5.Producer.CategoryProducer import CategoryProducer,LeptonCatProducer
from RA5.Producer.NJet40Producer import NJet40Producer
from RA5.Producer.LeptonProducer import LeptonProducer
from RA5.Producer.JetProducer import JetProducer

lepCats = ["HH","HL","LL"]

xsWeighter              = XSWeighter("XSWeighter")

baselineSkimmer         = BaselineSkimmer("BaselineSkimmer")
syncSkimmer             = SyncSkimmer("SyncSkimmer")
metSkimmer              = METSkimmer("METSkimmer")
llHtSkimmer             = LLHtSkimmer("LLHtSkimmer")
hltSkimmer              = HLTSkimmer("HLTSkimmer",emulation=True)

leptonJetProducer       = LeptonJetProducer("LeptonJetProducer","Run2016")
leptonCatProducer       = LeptonCatProducer("CategoryProducer")
nJet40Producer          = NJet40Producer("NJet40Producer")
leptonProducer          = LeptonProducer("LeptonProducer")
jetProducer             = JetProducer("JetProducer")

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
rpv_sequence.add(baselineSkimmer)
rpv_sequence.add(leptonCatProducer)
rpv_sequence.add(llHtSkimmer)
rpv_sequence.add(hltSkimmer)
rpv_sequence.add(xsWeighter)

sync_sequence = Sequence()
sync_sequence.add(leptonProducer)
sync_sequence.add(jetProducer)
#sr_sequence.add(leptonCatProducer)
sync_sequence.add(syncSkimmer)
#sr_sequence.add(llHtSkimmer)

