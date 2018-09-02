from Core.Sequence import Sequence

from RA5.Weighter.XSWeighter import XSWeighter
from RA5.LeptonJetRecleaner.EventProducer import LeptonJetProducer 
from RA5.Skimmer.BaselineSkimmer import BaselineSkimmer
from RA5.Skimmer.METSkimmer import METSkimmer
from RA5.Skimmer.LLHtSkimmer import LLHtSkimmer
from RA5.Producer.CategoryProducer import CategoryProducer
from RA5.Producer.NJet40Producer import NJet40Producer

lepCats = ["HH","HL","LL"]

leptonJetProducer       = LeptonJetProducer("LeptonJetProducer","Run2016")
xsWeighter              = XSWeighter("XSWeighter")
baselineSkimmer         = BaselineSkimmer("BaselineSkimmer")
metSkimmer              = METSkimmer("METSkimmer")
llHtSkimmer             = LLHtSkimmer("LLHtSkimmer")
categoryProducer        = CategoryProducer("CategoryProducer")
nJet40Producer           = NJet40Producer("NJet40Producer")

sr_sequence = Sequence()
sr_sequence.add(leptonJetProducer)
#sr_sequence.add(baselineSkimmer)
sr_sequence.add(metSkimmer)
sr_sequence.add(nJet40Producer)
sr_sequence.add(categoryProducer)
sr_sequence.add(llHtSkimmer)
sr_sequence.add(xsWeighter)

rpv_sequence = Sequence()
#rpv_sequence.add(baselineSkimmer)
#rpv_sequence.add(metSkimmer)
rpv_sequence.add(nJet40Producer)
rpv_sequence.add(categoryProducer)
rpv_sequence.add(llHtSkimmer)
rpv_sequence.add(xsWeighter)
