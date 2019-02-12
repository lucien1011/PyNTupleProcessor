from Core.Sequence import Sequence

from HToZdZd.Skimmer.AnalysisSkimmer import AnalysisSkimmer
from HToZdZd.Skimmer.BlindSkimmer import BlindSkimmer
from DarkZ.Weighter.DataMCWeighter import DataMCWeighter
from DarkZ.Weighter.NLOWeighter import NLOWeighter
from DarkZ.Weighter.FakeRateWeighter import FakeRateWeighter
from DarkZ.Producer.VariableProducer import VariableProducer

from NanoAOD.Weighter.XSWeighter import XSWeighter # Stealing module from NanoAOD framework

blindSkimmer                = BlindSkimmer("BlindSkimmer")
darkPhotonSRSkimmer         = AnalysisSkimmer("DarkPhotonSRSkimmer")
darkPhotonSBSkimmer         = AnalysisSkimmer("DarkPhotonSRSkimmer",cutflow="DarkPhoton-m4lSB")
darkPhotonFullM4lSkimmer    = AnalysisSkimmer("DarkPhotonSRSkimmer",cutflow="DarkPhoton-m4l70")
xsWeighter                  = XSWeighter("XSWeighter")
nloWeighter                 = NLOWeighter("NLOWeighter")
dataMCWeighter              = DataMCWeighter("DataMCWeighter")
variableProducer            = VariableProducer("VariableProducer")
fakeRateWeighter            = FakeRateWeighter("FakeRateWeighter")

darkphoton_signal_sequence = Sequence()
darkphoton_signal_sequence.add(blindSkimmer)
darkphoton_signal_sequence.add(darkPhotonSRSkimmer) ## Signal-Region Skimmer
darkphoton_signal_sequence.add(xsWeighter)
darkphoton_signal_sequence.add(nloWeighter)
darkphoton_signal_sequence.add(dataMCWeighter)
darkphoton_signal_sequence.add(variableProducer)
darkphoton_signal_sequence.add(fakeRateWeighter)

darkphoton_sb_sequence = Sequence()
darkphoton_sb_sequence.add(blindSkimmer)
darkphoton_sb_sequence.add(darkPhotonSBSkimmer) ## Signal-Background Skimmer
darkphoton_sb_sequence.add(xsWeighter)
darkphoton_sb_sequence.add(nloWeighter)
darkphoton_sb_sequence.add(dataMCWeighter)
darkphoton_sb_sequence.add(variableProducer)
darkphoton_sb_sequence.add(fakeRateWeighter)

darkphoton_fullm4l_sequence = Sequence()
darkphoton_fullm4l_sequence.add(blindSkimmer)
darkphoton_fullm4l_sequence.add(darkPhotonFullM4lSkimmer) ## Full m4l skimmer
darkphoton_fullm4l_sequence.add(xsWeighter)
darkphoton_fullm4l_sequence.add(nloWeighter)
darkphoton_fullm4l_sequence.add(dataMCWeighter)
darkphoton_fullm4l_sequence.add(variableProducer)
darkphoton_fullm4l_sequence.add(fakeRateWeighter)

