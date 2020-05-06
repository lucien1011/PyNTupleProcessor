from Core.Sequence import Sequence

from Zprime.Skimmer.AnalysisSkimmer import AnalysisSkimmer
from Zprime.Producer.VariableProducer import VariableProducer
from DarkZ.Weighter.DataMCWeighter import DataMCWeighter
from DarkZ.Weighter.NLOWeighter import NLOWeighter
from Zprime.Skimmer.FinalstateSkimmer import FinalstateSkimmer
from Zprime.Weighter.FakeRateWeighter import FakeRateWeighter

from NanoAOD.Weighter.XSWeighter import XSWeighter # Stealing module from NanoAOD framework

SRSkimmer               = AnalysisSkimmer("SRSkimmer")
finalstateSkimmer       = FinalstateSkimmer("FinalstateSkimmer")

dataMCWeighter          = DataMCWeighter("DataMCWeighter")
nloWeighter             = NLOWeighter("NLOWeighter")
xsWeighter              = XSWeighter("XSWeighter")
varProducer             = VariableProducer("VariableProducer")
fakerateWeighter        = FakeRateWeighter("FakeRateWeighter")

signal_sequence = Sequence()
signal_sequence.add(SRSkimmer)
signal_sequence.add(xsWeighter)
signal_sequence.add(dataMCWeighter)
signal_sequence.add(nloWeighter)
signal_sequence.add(varProducer)
#signal_sequence.add(fakerateWeighter)

fr_sequence = Sequence()
fr_sequence.add(SRSkimmer)
fr_sequence.add(finalstateSkimmer)
fr_sequence.add(xsWeighter)
fr_sequence.add(dataMCWeighter)
fr_sequence.add(nloWeighter)
fr_sequence.add(varProducer)
