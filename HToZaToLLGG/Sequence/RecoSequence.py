from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence
from Core.Utils.LambdaFunc import LambdaFunc

from NanoAOD.Weighter.XSWeighter import XSWeighter
from NanoAOD.Weighter.PUWeighter import PUWeighter
from NanoAOD.Skimmer.JSONSkimmer import JSONSkimmer
from NanoAOD.Skimmer.METFilter import METFilter

from HToZaToLLGG.Skimmer.SRSkimmer import ResolvedSRSkimmer,MergedSRSkimmer
from HToZaToLLGG.Producer.ElectronProducer import ElectronProducer
from HToZaToLLGG.Producer.MuonProducer import MuonProducer
from HToZaToLLGG.Producer.PhotonProducer import PhotonProducer
from HToZaToLLGG.Producer.VariableProducer import VariableProducer

# ____________________________________________________________________________________________________________________________________________ ||
xsWeighter              = XSWeighter("XSWeighter")
muProducer              = MuonProducer(
        "MuonProducer",
        LambdaFunc("x: x.mediumId == 1"),
        LambdaFunc("x: x.pfRelIso03_all < 0.35"),
        LambdaFunc("x: x.pt > 0. and abs(x.eta) < 2.5"),
        )
elProducer              = ElectronProducer(
        "ElectronProducer",
        LambdaFunc("x: x.cutBased == 3 or x.cutBased == 4"),
        #LambdaFunc("x: x.pfRelIso03_all < 0.35"),
        LambdaFunc("x: True"),
        LambdaFunc("x: x.pt > 0. and abs(x.eta) < 2.5"),
        )
phoProducer             = PhotonProducer(
        "PhotonProducer",
        #LambdaFunc("x: (abs(x.eta) < 1.4 and x.mvaID_WP90 > -0.02) or (abs(x.eta) > 1.4 and abs(x.eta) < 2.5 and x.mvaID_WP90 > -0.26)"),
        LambdaFunc("x: x.mvaID_WP90"),
        #LambdaFunc("x: x.pfRelIso03_all < 0.35"),
        LambdaFunc("x: True"),
        LambdaFunc("x: x.pt > 0. and abs(x.eta) < 2.5"),
        LambdaFunc("ev,x: all([x.electronIdx != e.getIndex() for e in ev.selElectrons])"),
        #LambdaFunc("x: x.cutBasedBitmap == 1"),
        #LambdaFunc("x: x.pfRelIso03_all < 0.35"),
        )
variableProducer        = VariableProducer(
        "VariableProducer",
        )
reolvedSRSkimmer        = ResolvedSRSkimmer(
        "SRSkimmer",
        )
mergedSRSkimmer         = MergedSRSkimmer(
        "SRSkimmer",
        )

# ____________________________________________________________________________________________________________________________________________ ||
sr_resolved_sequence = Sequence()
sr_resolved_sequence.add(muProducer)
sr_resolved_sequence.add(elProducer)
sr_resolved_sequence.add(phoProducer)
sr_resolved_sequence.add(reolvedSRSkimmer)
sr_resolved_sequence.add(xsWeighter)

sr_merged_sequence = Sequence()
sr_merged_sequence.add(muProducer)
sr_merged_sequence.add(elProducer)
sr_merged_sequence.add(phoProducer)
sr_merged_sequence.add(mergedSRSkimmer)
sr_merged_sequence.add(xsWeighter)

# ____________________________________________________________________________________________________________________________________________ ||
