from Core.Sequence import Sequence

from HZZ4l.Skimmer.WrongFCSkimmer import WrongFCSkimmer
from DarkZ.Weighter.DataMCWeighter import DataMCWeighter
from DarkZ.Weighter.NLOWeighter import NLOWeighter
from HZZ4l.Weighter.FakeRateWeighter import FakeRateWeighter

from NanoAOD.Weighter.XSWeighter import XSWeighter # Stealing module from NanoAOD framework

WrongFCSkimmer_SR       = WrongFCSkimmer("WrongFC-SR",cutflow="SR")
WrongFCSkimmer_CR       = WrongFCSkimmer("WrongFC-CR",cutflow="CR")
WrongFCSkimmer_3P1F     = WrongFCSkimmer("WrongFC-CR",cutflow="3P1F")

dataMCWeighter          = DataMCWeighter("DataMCWeighter")
nloWeighter             = NLOWeighter("NLOWeighter")
xsWeighter              = XSWeighter("XSWeighter")
fakeRateWeighter        = FakeRateWeighter("FakeRateWeighter")

wrongFC_sr_sequence = Sequence()
wrongFC_sr_sequence.add(WrongFCSkimmer_SR)
wrongFC_sr_sequence.add(xsWeighter)
wrongFC_sr_sequence.add(dataMCWeighter)
wrongFC_sr_sequence.add(fakeRateWeighter)

wrongFC_cr_sequence = Sequence()
wrongFC_cr_sequence.add(WrongFCSkimmer_CR)
wrongFC_cr_sequence.add(xsWeighter)
wrongFC_cr_sequence.add(dataMCWeighter)
wrongFC_cr_sequence.add(fakeRateWeighter)

wrongFC_3p1f_sequence = Sequence()
wrongFC_3p1f_sequence.add(WrongFCSkimmer_3P1F)
wrongFC_3p1f_sequence.add(xsWeighter)
wrongFC_3p1f_sequence.add(dataMCWeighter)
wrongFC_3p1f_sequence.add(fakeRateWeighter)
