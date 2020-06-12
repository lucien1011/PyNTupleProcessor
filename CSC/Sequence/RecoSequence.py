from Core.Sequence import Sequence

from CSC.Producer.StandAloneMuonProducer import StandAloneMuonProducer
from CSC.Weighter.EventWeighter import EventWeighter

eventWeighter = EventWeighter("EventWeighter")
standAloneMuonProducer = StandAloneMuonProducer("StandAloneMuonProducer")

MuonSequence = Sequence()
MuonSequence.add(eventWeighter)
MuonSequence.add(standAloneMuonProducer)
