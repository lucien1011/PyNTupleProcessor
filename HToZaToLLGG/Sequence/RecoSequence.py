from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence
from Core.Utils.LambdaFunc import LambdaFunc

from NanoAOD.Weighter.XSWeighter import XSWeighter
from NanoAOD.Weighter.PUWeighter import PUWeighter
from NanoAOD.Skimmer.JSONSkimmer import JSONSkimmer
from NanoAOD.Skimmer.METFilter import METFilter

from HToZaToLLGG.Skimmer.SRSkimmer import SRSkimmer
from HToZaToLLGG.Producer.ElectronProducer import ElectronProducer
from HToZaToLLGG.Producer.PhotonProducer import PhotonProducer

# ____________________________________________________________________________________________________________________________________________ ||
xsWeighter              = XSWeighter("XSWeighter")
elProducer              = ElectronProducer(
        "ElectronProducer",
        LambdaFunc("x: x.cutBased[0] == 3"),
        LambdaFunc("x: x.pfRelIso03_all[0] < 0.35"),
        )
phoProducer             = PhotonProducer(
        "PhotonProducer",
        LambdaFunc("x: x.cutBasedBitmap[0] == 1"),
        LambdaFunc("x: x.pfRelIso03_all[0] < 0.35"),
        )
srSkimmer               = SRSkimmer(
        "SRSkimmer",
        )

# ____________________________________________________________________________________________________________________________________________ ||
sr_sequence = Sequence()
sr_sequence.add(elProducer)
sr_sequence.add(phoProducer)
sr_sequence.add(srSkimmer)
sr_sequence.add(xsWeighter)

# ____________________________________________________________________________________________________________________________________________ ||
