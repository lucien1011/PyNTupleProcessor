from Core.Sequence import Sequence

from Zprime.Skimmer.AnalysisSkimmer import AnalysisSkimmer
from Zprime.Producer.VariableProducer import VariableProducer
from DarkZ.Weighter.DataMCWeighter import DataMCWeighter
from DarkZ.Weighter.NLOWeighter import NLOWeighter
from DarkZ.Weighter.FakeRateWeighter import FakeRateWeighter

from NanoAOD.Weighter.XSWeighter import XSWeighter # Stealing module from NanoAOD framework

SRSkimmer               = AnalysisSkimmer("SRSkimmer")
m4lcrSkimmer               = AnalysisSkimmer("m4lcrSkimmer","Zprime-m4lCR")

dataMCWeighter          = DataMCWeighter("DataMCWeighter")
nloWeighter             = NLOWeighter("NLOWeighter")
xsWeighter              = XSWeighter("XSWeighter")
varProducer             = VariableProducer("VariableProducer")
fakeRateWeighter        = FakeRateWeighter("FakeRateWeighter")

signal_sequence = Sequence()
signal_sequence.add(SRSkimmer)
signal_sequence.add(xsWeighter)
signal_sequence.add(dataMCWeighter)
signal_sequence.add(nloWeighter)
signal_sequence.add(varProducer)

m4lcr_sequence = Sequence()
m4lcr_sequence.add(m4lcrSkimmer)
m4lcr_sequence.add(xsWeighter)
m4lcr_sequence.add(dataMCWeighter)
m4lcr_sequence.add(nloWeighter)
m4lcr_sequence.add(varProducer)
m4lcr_sequence.add(fakeRateWeighter)
