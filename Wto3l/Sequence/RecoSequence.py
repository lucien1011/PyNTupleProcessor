from Core.Sequence import Sequence

from NanoAOD.Weighter.XSWeighter import XSWeighter # Stealing module from NanoAOD framework
from Wto3l.Skimmer.ZSelector import ZSelector

xsWeighter              = XSWeighter("XSWeighter")
zSelector            	= ZSelector("ZSelector")

Wto3l_sequence = Sequence()
Wto3l_sequence.add(zSelector)
Wto3l_sequence.add(xsWeighter)

