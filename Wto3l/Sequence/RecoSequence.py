from Core.Sequence import Sequence

from DarkZ.Weighter.DataMCWeighter import DataMCWeighter
from NanoAOD.Weighter.XSWeighter import XSWeighter # Stealing module from NanoAOD framework
from Wto3l.Skimmer.ZSelector import ZSelector
from Wto3l.Weighter.FakerateWeighter import FakerateWeighter

xsWeighter              = XSWeighter("XSWeighter")
dataMCWeighter          = DataMCWeighter("DataMCWeighter")
zSelector            	= ZSelector("ZSelector")
fakerateWeighter        = FakerateWeighter("FakerateWeighter")

Wto3l_sequence = Sequence()
Wto3l_sequence.add(xsWeighter)
Wto3l_sequence.add(dataMCWeighter)
Wto3l_sequence.add(zSelector)
#Wto3l_sequence.add(fakerateWeighter)

