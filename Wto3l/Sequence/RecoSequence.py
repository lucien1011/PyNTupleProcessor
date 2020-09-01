from Core.Sequence import Sequence

from NanoAOD.Weighter.XSWeighter import XSWeighter # Stealing module from NanoAOD framework

xsWeighter              = XSWeighter("XSWeighter")

Wto3l_sequence = Sequence()
Wto3l_sequence.add(xsWeighter)
