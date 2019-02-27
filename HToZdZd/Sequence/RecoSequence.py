from Core.Sequence import Sequence

from HToZdZd.Skimmer.AnalysisSkimmer import AnalysisSkimmer
from HToZdZd.Skimmer.BlindSkimmer import BlindSkimmer
from DarkZ.Weighter.DataMCWeighter import DataMCWeighter
from DarkZ.Weighter.NLOWeighter import NLOWeighter
from DarkZ.Weighter.FakeRateWeighter import FakeRateWeighter
from DarkZ.Producer.VariableProducer import VariableProducer

from NanoAOD.Weighter.XSWeighter import XSWeighter # Stealing module from NanoAOD framework

blindSkimmer                = BlindSkimmer("BlindSkimmer")
xsWeighter                  = XSWeighter("XSWeighter")
nloWeighter                 = NLOWeighter("NLOWeighter")
dataMCWeighter              = DataMCWeighter("DataMCWeighter")
variableProducer            = VariableProducer("VariableProducer")
fakeRateWeighter            = FakeRateWeighter("FakeRateWeighter")

darkPhotonSRSkimmer         = AnalysisSkimmer("DarkPhotonSRSkimmer")
darkPhotonSBSkimmer         = AnalysisSkimmer("DarkPhotonSRSkimmer",cutflow="DarkPhoton-m4lSB")
darkPhotonFullM4lSkimmer    = AnalysisSkimmer("DarkPhotonSRSkimmer",cutflow="DarkPhoton-m4l70")
#darkPhotonSignifSkimmer     = AnalysisSkimmer("DarkPhotonSRSkimmer",cutflow="DarkPhoton-signifmasswindow")
darkPhoton3P1FSkimmer       = AnalysisSkimmer("DarkPhotonSRSkimmer",cutflow="DarkPhoton-3P1F")

darkphoton_signal_sequence = Sequence()
darkphoton_signal_sequence.add(blindSkimmer)
darkphoton_signal_sequence.add(xsWeighter)
darkphoton_signal_sequence.add(nloWeighter)
darkphoton_signal_sequence.add(dataMCWeighter)
darkphoton_signal_sequence.add(variableProducer)
darkphoton_signal_sequence.add(fakeRateWeighter)
darkphoton_signal_sequence.add(darkPhotonSRSkimmer) ## Signal-Region Skimmer

darkphoton_signal_unblind_sequence = Sequence()
darkphoton_signal_unblind_sequence.add(xsWeighter)
darkphoton_signal_unblind_sequence.add(nloWeighter)
darkphoton_signal_unblind_sequence.add(dataMCWeighter)
darkphoton_signal_unblind_sequence.add(variableProducer)
darkphoton_signal_unblind_sequence.add(fakeRateWeighter)
darkphoton_signal_unblind_sequence.add(darkPhotonSRSkimmer)

darkphoton_sb_sequence = Sequence()
darkphoton_sb_sequence.add(blindSkimmer)
darkphoton_sb_sequence.add(xsWeighter)
darkphoton_sb_sequence.add(nloWeighter)
darkphoton_sb_sequence.add(dataMCWeighter)
darkphoton_sb_sequence.add(variableProducer)
darkphoton_sb_sequence.add(fakeRateWeighter)
darkphoton_sb_sequence.add(darkPhotonSBSkimmer) ## Signal-Background Skimmer

darkphoton_fullm4l_sequence = Sequence()
darkphoton_fullm4l_sequence.add(blindSkimmer)
darkphoton_fullm4l_sequence.add(xsWeighter)
darkphoton_fullm4l_sequence.add(nloWeighter)
darkphoton_fullm4l_sequence.add(dataMCWeighter)
darkphoton_fullm4l_sequence.add(variableProducer)
darkphoton_fullm4l_sequence.add(fakeRateWeighter)
darkphoton_fullm4l_sequence.add(darkPhotonFullM4lSkimmer) ## Full m4l skimmer

# Perhaps make a significance skimmer?
#darkphoton_signif_masswindow_sequence = Sequence()
#darkphoton_signif_masswindow_sequence.add(blindSkimmer)
#darkphoton_signif_masswindow_sequence.add(xsWeighter)
#darkphoton_signif_masswindow_sequence.add(nloWeighter)
#darkphoton_signif_masswindow_sequence.add(dataMCWeighter)
#darkphoton_signif_masswindow_sequence.add(variableProducer)
#darkphoton_signif_masswindow_sequence.add(fakeRateWeighter)
#darkphoton_signif_masswindow_sequence.add() ## 
#
darkphoton_3p1f_sequence = Sequence()
darkphoton_3p1f_sequence.add(darkPhoton3P1FSkimmer)
darkphoton_3p1f_sequence.add(xsWeighter)
darkphoton_3p1f_sequence.add(nloWeighter)
darkphoton_3p1f_sequence.add(dataMCWeighter)
darkphoton_3p1f_sequence.add(variableProducer)
darkphoton_3p1f_sequence.add(fakeRateWeighter)
