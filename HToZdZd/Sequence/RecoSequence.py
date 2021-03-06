from Core.Sequence import Sequence
from Core.BaseObject import BaseObject
from Core.Utils.LambdaFunc import LambdaFunc

from HToZdZd.Skimmer.AnalysisSkimmer import AnalysisSkimmer
from HToZdZd.Skimmer.BlindSkimmer import BlindSkimmer
from HToZdZd.Skimmer.WindowSkimmer import WindowSkimmer
from HToZdZd.Skimmer.ZabVetoSkimmer import ZabVetoSkimmer
from DarkZ.Weighter.DataMCWeighter import DataMCWeighter
from DarkZ.Weighter.NLOWeighter import NLOWeighter
from DarkZ.Weighter.FakeRateWeighter import FakeRateWeighter
from DarkZ.Producer.VariableProducer import VariableProducer
from DarkZ.Skimmer.NarrowResonanceSkimmer import NarrowResonanceSkimmer

from NanoAOD.Weighter.XSWeighter import XSWeighter # Stealing module from NanoAOD framework

#____________________________________________________________________________________________________
# Define Skimmers
windowSkimmer               = WindowSkimmer("WindowSkimmer")
invertWindowSkimmer         = WindowSkimmer("WindowSkimmer",invert=True)
zabVetoSkimmer              = ZabVetoSkimmer("ZabVetoSkimmer")
blindSkimmer                = BlindSkimmer("BlindSkimmer")
xsWeighter                  = XSWeighter("XSWeighter")
nloWeighter                 = NLOWeighter("NLOWeighter")
dataMCWeighter              = DataMCWeighter("DataMCWeighter")
variableProducer            = VariableProducer("VariableProducer")
fakeRateWeighter            = FakeRateWeighter("FakeRateWeighter")

darkPhotonSRSkimmer         = AnalysisSkimmer("DarkPhotonSRSkimmer")
darkPhotonSBSkimmer         = AnalysisSkimmer("DarkPhotonSRSkimmer",cutflow="DarkPhoton-m4lSB")
darkPhotonFullM4lSkimmer    = AnalysisSkimmer("DarkPhotonSRSkimmer",cutflow="DarkPhoton-m4l70")
darkPhoton3P1FSkimmer       = AnalysisSkimmer("DarkPhotonSRSkimmer",cutflow="DarkPhoton-3P1F")
resonaceZ2Skimmer           = NarrowResonanceSkimmer(
        "NarrowResonanceSkimmer",
        [
            BaseObject(
                "NarrowResonanceSelection",
                selFunc=LambdaFunc("x: (abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11 and x.massZ2[0] > 8.50 and x.massZ2[0] < 11.0) or (abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13 and x.massZ2[0] > 8.50 and x.massZ2[0] < 11.0)"),
                ),
        ],
        )
resonaceZ1Skimmer           = NarrowResonanceSkimmer(
        "NarrowResonanceSkimmer",
        [
            BaseObject(
                "NarrowResonanceSelection",
                selFunc=LambdaFunc("x: (abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11 and x.massZ1[0] > 8.50 and x.massZ1[0] < 11.0) or (abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13 and x.massZ1[0] > 8.50 and x.massZ1[0] < 11.0)"),
                ),
        ],
        )

#____________________________________________________________________________________________________
# Make Sequences
darkphoton_signal_sequence = Sequence()
darkphoton_signal_sequence.add(blindSkimmer)
darkphoton_signal_sequence.add(xsWeighter)
darkphoton_signal_sequence.add(nloWeighter)
darkphoton_signal_sequence.add(dataMCWeighter)
darkphoton_signal_sequence.add(variableProducer)
darkphoton_signal_sequence.add(fakeRateWeighter)
darkphoton_signal_sequence.add(darkPhotonSRSkimmer) ## Signal-Region Skimmer
darkphoton_signal_sequence.add(resonaceZ1Skimmer)
darkphoton_signal_sequence.add(resonaceZ2Skimmer)

darkphoton_signal_unblind_sequence = Sequence()
darkphoton_signal_unblind_sequence.add(xsWeighter)
darkphoton_signal_unblind_sequence.add(nloWeighter)
darkphoton_signal_unblind_sequence.add(dataMCWeighter)
darkphoton_signal_unblind_sequence.add(variableProducer)
darkphoton_signal_unblind_sequence.add(fakeRateWeighter)
darkphoton_signal_unblind_sequence.add(darkPhotonSRSkimmer)
darkphoton_signal_unblind_sequence.add(resonaceZ1Skimmer)
darkphoton_signal_unblind_sequence.add(resonaceZ2Skimmer)
darkphoton_signal_unblind_sequence.add(windowSkimmer)
#darkphoton_signal_unblind_sequence.add(zabVetoSkimmer)

darkphoton_sb_sequence = Sequence()
darkphoton_sb_sequence.add(blindSkimmer)
darkphoton_sb_sequence.add(xsWeighter)
darkphoton_sb_sequence.add(nloWeighter)
darkphoton_sb_sequence.add(dataMCWeighter)
darkphoton_sb_sequence.add(variableProducer)
darkphoton_sb_sequence.add(fakeRateWeighter)
darkphoton_sb_sequence.add(darkPhotonSBSkimmer) ## Signal-Background Skimmer

darkphoton_fullm4l_sequence = Sequence()
#darkphoton_fullm4l_sequence.add(blindSkimmer)
darkphoton_fullm4l_sequence.add(xsWeighter)
darkphoton_fullm4l_sequence.add(nloWeighter)
darkphoton_fullm4l_sequence.add(dataMCWeighter)
darkphoton_fullm4l_sequence.add(variableProducer)
darkphoton_fullm4l_sequence.add(fakeRateWeighter)
darkphoton_fullm4l_sequence.add(darkPhotonFullM4lSkimmer) ## Full m4l skimmer
darkphoton_fullm4l_sequence.add(resonaceZ1Skimmer)
darkphoton_fullm4l_sequence.add(resonaceZ2Skimmer)

darkphoton_3p1f_sequence = Sequence()
darkphoton_3p1f_sequence.add(xsWeighter)
darkphoton_3p1f_sequence.add(nloWeighter)
darkphoton_3p1f_sequence.add(dataMCWeighter)
darkphoton_3p1f_sequence.add(variableProducer)
darkphoton_3p1f_sequence.add(fakeRateWeighter)
darkphoton_3p1f_sequence.add(darkPhoton3P1FSkimmer) ## Full m4l skimmer
