from Core.Sequence import Sequence

from HToZdZd.Skimmer.AnalysisSkimmer import AnalysisSkimmer
from HToZdZd.Skimmer.BlindSkimmer import BlindSkimmer
from DarkZ.Weighter.DataMCWeighter import DataMCWeighter
from DarkZ.Weighter.NLOWeighter import NLOWeighter
from DarkZ.Weighter.FakeRateWeighter import FakeRateWeighter
from DarkZ.Producer.VariableProducer import VariableProducer

from NanoAOD.Weighter.XSWeighter import XSWeighter # Stealing module from NanoAOD framework

darkPhotonSRSkimmer         = AnalysisSkimmer("DarkPhotonSRSkimmer")
darkPhotonSBSkimmer         = AnalysisSkimmer("DarkPhotonSRSkimmer",cutflow="DarkPhoton-m4lSB")
darkPhotonFullM4lSkimmer    = AnalysisSkimmer("DarkPhotonSRSkimmer",cutflow="DarkPhoton-m4l70")
dataMCWeighter          = DataMCWeighter("DataMCWeighter")
nloWeighter             = NLOWeighter("NLOWeighter")
xsWeighter              = XSWeighter("XSWeighter")
blindSkimmer            = BlindSkimmer("BlindSkimmer")
fakeRateWeighter        = FakeRateWeighter("FakeRateWeighter")
variableProducer        = VariableProducer("VariableProducer")

darkphoton_signal_sequence = Sequence()
darkphoton_signal_sequence.add(blindSkimmer)
darkphoton_signal_sequence.add(darkPhotonSRSkimmer)
darkphoton_signal_sequence.add(xsWeighter)
darkphoton_signal_sequence.add(nloWeighter)
darkphoton_signal_sequence.add(dataMCWeighter)
darkphoton_signal_sequence.add(variableProducer)
darkphoton_signal_sequence.add(fakeRateWeighter)

darkphoton_signal_unblind_sequence = Sequence()
darkphoton_signal_unblind_sequence.add(darkPhotonSRSkimmer)
darkphoton_signal_unblind_sequence.add(xsWeighter)
darkphoton_signal_unblind_sequence.add(nloWeighter)
darkphoton_signal_unblind_sequence.add(dataMCWeighter)
darkphoton_signal_unblind_sequence.add(variableProducer)
darkphoton_signal_unblind_sequence.add(fakeRateWeighter)

darkphoton_sb_sequence = Sequence()
darkphoton_sb_sequence.add(blindSkimmer)
darkphoton_sb_sequence.add(darkPhotonSBSkimmer)
darkphoton_sb_sequence.add(xsWeighter)
darkphoton_sb_sequence.add(nloWeighter)
darkphoton_sb_sequence.add(dataMCWeighter)
darkphoton_sb_sequence.add(variableProducer)
darkphoton_sb_sequence.add(fakeRateWeighter)

darkphoton_fullm4l_sequence = Sequence()
darkphoton_fullm4l_sequence.add(blindSkimmer)
darkphoton_fullm4l_sequence.add(darkPhotonFullM4lSkimmer)
darkphoton_fullm4l_sequence.add(xsWeighter)
darkphoton_fullm4l_sequence.add(nloWeighter)
darkphoton_fullm4l_sequence.add(dataMCWeighter)
darkphoton_fullm4l_sequence.add(variableProducer)
darkphoton_fullm4l_sequence.add(fakeRateWeighter)

