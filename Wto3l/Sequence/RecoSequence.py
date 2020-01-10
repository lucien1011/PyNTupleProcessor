from Core.Sequence import Sequence

#from DarkZ.Skimmer.AnalysisSkimmer import AnalysisSkimmer
#from DarkZ.Skimmer.BlindSkimmer import BlindSkimmer
from DarkZ.Weighter.DataMCWeighter import DataMCWeighter
from DarkZ.Weighter.NLOWeighter import NLOWeighter

from Wto3l.Skimmer.FinalstateSkimmer import FinalstateSkimmer
from Wto3l.Skimmer.EventSkimmer import EventSkimmer
from Wto3l.Weighter.FakerateWeighter import FakerateWeighter
from Wto3l.Producer.DeltaR_Producer import DeltaR_Producer
from Wto3l.Producer.Lep_Producer import Lep_Producer

from NanoAOD.Weighter.XSWeighter import XSWeighter # Stealing module from NanoAOD framework

dataMCWeighter          = DataMCWeighter("DataMCWeighter")
nloWeighter             = NLOWeighter("NLOWeighter")
xsWeighter              = XSWeighter("XSWeighter")
finalstateSkimmer       = FinalstateSkimmer("FinalstateSkimmer")
eventSkimmer            = EventSkimmer("EventSkimmer")
fakerateWeighter        = FakerateWeighter("FakerateWeighter")
deltar_producer         = DeltaR_Producer("DeltaR_Producer")
lep_producer            = Lep_Producer("Lep_Producer")
#bliSkimmer              = BlindSkimmer("BlindSkimmer")


Wto3l_sequence = Sequence()
Wto3l_sequence.add(xsWeighter)
Wto3l_sequence.add(dataMCWeighter)
#Wto3l_sequence.add(nloWeighter)
Wto3l_sequence.add(deltar_producer)
Wto3l_sequence.add(lep_producer)
Wto3l_sequence.add(finalstateSkimmer)
Wto3l_sequence.add(eventSkimmer)
Wto3l_sequence.add(fakerateWeighter)
#Wto3l_sequence.add(bliSkimmer)

Wto3l_mptest_sequence = Sequence()
Wto3l_mptest_sequence.add(xsWeighter)
Wto3l_mptest_sequence.add(dataMCWeighter)

