from LJMet.Weighter.XSWeighter import XSWeighter
from LJMet.Skimmer.AnalysisSkimmer import AnalysisSkimmer
from LJMet.Skimmer.PreselectionSkimmer import PreselectionSkimmer
from LJMet.Weighter.DataMCWeighter import DataMCWeighter
from LJMet.Producer.CategoryProducer import CategoryProducer

from Core.Sequence import Sequence

xsWeighter              = XSWeighter("XSWeighter")
dataMCWeighter          = DataMCWeighter("DataMCWeighter")
srSkimmer               = AnalysisSkimmer("AnalysisSkimmer",cutflow="SR")
crSkimmer               = AnalysisSkimmer("AnalysisSkimmer",cutflow="CR")
preSkimmer              = PreselectionSkimmer("PreselecionSkimmer")
catProducer				= CategoryProducer("CategoryProducer")

sr_sequence             = Sequence()
sr_sequence.add(srSkimmer)
sr_sequence.add(xsWeighter)
sr_sequence.add(dataMCWeighter)
sr_sequence.add(catProducer)

cr_sequence             = Sequence()
cr_sequence.add(preSkimmer)
cr_sequence.add(crSkimmer)
cr_sequence.add(xsWeighter)
cr_sequence.add(dataMCWeighter)

pre_sequence             = Sequence()
pre_sequence.add(preSkimmer)
pre_sequence.add(xsWeighter)
pre_sequence.add(dataMCWeighter)
