from Core.Sequence import Sequence

from DarkZ.Skimmer.AnalysisSkimmer import AnalysisSkimmer
from DarkZ.Skimmer.BlindSkimmer import BlindSkimmer
from DarkZ.Weighter.DataMCWeighter import DataMCWeighter
from DarkZ.Weighter.NLOWeighter import NLOWeighter
from DarkZ.Weighter.FakeRateWeighter import FakeRateWeighter
from DarkZ.Producer.VariableProducer import VariableProducer

from NanoAOD.Weighter.XSWeighter import XSWeighter # Stealing module from NanoAOD framework

darkPhotonSRSkimmer     = AnalysisSkimmer("DarkPhotonSRSkimmer")
darkPhotonCRSkimmer     = AnalysisSkimmer("DarkPhotonCRSkimmer",cutflow="DarkPhoton-ZXCR")
darkPhoton3P1FSkimmer   = AnalysisSkimmer("DarkPhoton3P1FSkimmer",cutflow="DarkPhoton-3P1F")
higgsSRSkimmer          = AnalysisSkimmer("HiggsSRSkimmer",cutflow="Higgs-SR")
higgsCRSkimmer          = AnalysisSkimmer("HiggsCRSkimmer",cutflow="Higgs-ZXCR")
higgs3P1FSkimmer        = AnalysisSkimmer("Higgs3P1FSkimmer",cutflow="Higgs-3P1F")
m4lSBSkimmer            = AnalysisSkimmer("m4lSBSkimmer",cutflow="Higgs-m4lSB")
m4lNarrowSkimmer        = AnalysisSkimmer("m4lNarrowSkimmer",cutflow="Higgs-m4lNarrowWindow")
darkPhotonM4lSBSkimmer  = AnalysisSkimmer("m4lNarrowSkimmer",cutflow="DarkPhoton-m4lSB")
darkPhotonCRV2Skimmer   = AnalysisSkimmer("DarkPhoton-ZXCR-v2",cutflow="DarkPhoton-ZXCR-v2")
upsilonCRSkimmer        = AnalysisSkimmer("UpsilonCRSkimmer",cutflow="Upsilon-CR")
WrongFCSkimmer          = AnalysisSkimmer("UpsilonCRSkimmer",cutflow="WrongFC-SR")

dataMCWeighter          = DataMCWeighter("DataMCWeighter")
nloWeighter             = NLOWeighter("NLOWeighter")
xsWeighter              = XSWeighter("XSWeighter")
bliSkimmer              = BlindSkimmer("BlindSkimmer")
fakeRateWeighter        = FakeRateWeighter("FakeRateWeighter")
fakeRateWeighter_map    = FakeRateWeighter("FakeRateWeighter","make_map")

variableProducer        = VariableProducer("VariableProducer")

darkphoton_signal_sequence = Sequence()
darkphoton_signal_sequence.add(darkPhotonSRSkimmer)
darkphoton_signal_sequence.add(variableProducer)

zx_map_sequence = Sequence()
zx_map_sequence.add(darkPhotonSRSkimmer)
zx_map_sequence.add(variableProducer)

darkphoton_cr_sequence = Sequence()
darkphoton_cr_sequence.add(darkPhotonCRSkimmer)

darkphoton_cr_v2_sequence = Sequence()
darkphoton_cr_v2_sequence.add(variableProducer)
darkphoton_cr_v2_sequence.add(darkPhotonCRV2Skimmer)

darkphoton_m4lSB_sequence = Sequence()
darkphoton_m4lSB_sequence.add(variableProducer)
darkphoton_m4lSB_sequence.add(darkPhotonM4lSBSkimmer)

higgs_signal_sequence = Sequence()
higgs_signal_sequence.add(higgsSRSkimmer)

higgs_m4lNarrowWindow_sequence = Sequence()
higgs_m4lNarrowWindow_sequence.add(m4lNarrowSkimmer)

higgs_cr_sequence = Sequence()
higgs_cr_sequence.add(higgsCRSkimmer)

higgs_3p1f_sequence = Sequence()
higgs_3p1f_sequence.add(variableProducer)
higgs_3p1f_sequence.add(higgs3P1FSkimmer)

darkphoton_3p1f_sequence = Sequence()
darkphoton_3p1f_sequence.add(variableProducer)
darkphoton_3p1f_sequence.add(darkPhoton3P1FSkimmer)
darkphoton_3p1f_sequence.add(xsWeighter)
darkphoton_3p1f_sequence.add(nloWeighter)
darkphoton_3p1f_sequence.add(dataMCWeighter)
darkphoton_3p1f_sequence.add(fakeRateWeighter)

higgs_m4lSB_sequence = Sequence()
higgs_m4lSB_sequence.add(m4lSBSkimmer)

upsilon_sequence = Sequence()
upsilon_sequence.add(upsilonCRSkimmer)
upsilon_sequence.add(xsWeighter)
upsilon_sequence.add(nloWeighter)
upsilon_sequence.add(fakeRateWeighter)

upsilon_signal_sequence = Sequence()
upsilon_signal_sequence.add(darkPhotonSRSkimmer)
upsilon_signal_sequence.add(nloWeighter)
upsilon_signal_sequence.add(xsWeighter)
upsilon_signal_sequence.add(fakeRateWeighter)

wrongFC_signal_sequence = Sequence()
wrongFC_signal_sequence.add(WrongFCSkimmer)
wrongFC_signal_sequence.add(variableProducer)
wrongFC_signal_sequence.add(nloWeighter)
wrongFC_signal_sequence.add(xsWeighter)
wrongFC_signal_sequence.add(dataMCWeighter)
wrongFC_signal_sequence.add(fakeRateWeighter)


allSequence = [
        darkphoton_signal_sequence,
        darkphoton_cr_sequence,
        higgs_signal_sequence,
        higgs_cr_sequence,
        higgs_3p1f_sequence,
        higgs_m4lSB_sequence,
        higgs_m4lNarrowWindow_sequence,
        ]
for sequence in allSequence:
    sequence.add(bliSkimmer)
    sequence.add(xsWeighter)
    sequence.add(nloWeighter)
    sequence.add(dataMCWeighter)
    sequence.add(fakeRateWeighter)

for sequence in [
        darkphoton_m4lSB_sequence,
        darkphoton_cr_v2_sequence,
        ]:
    sequence.add(xsWeighter)
    sequence.add(nloWeighter)
    sequence.add(dataMCWeighter)
    sequence.add(fakeRateWeighter)

zx_map_sequence.add(bliSkimmer)
zx_map_sequence.add(xsWeighter)
zx_map_sequence.add(nloWeighter)
zx_map_sequence.add(dataMCWeighter)
zx_map_sequence.add(fakeRateWeighter_map)
