from LJMet.Weighter.XSWeighter import XSWeighter
from LJMet.Skimmer.AnalysisSkimmer import AnalysisSkimmer
from LJMet.Weighter.DataMCWeighter import DataMCWeighter
from LJMet.Producer.CategoryProducer import CategoryProducer

from Core.Sequence import Sequence

xsWeighter              = XSWeighter("XSWeighter")
dataMCWeighter          = DataMCWeighter("DataMCWeighter")
srSkimmer               = AnalysisSkimmer("AnalysisSkimmer",cutflow="SR")
catProducer				= CategoryProducer("CategoryProducer")

sr_sequence             = Sequence()
sr_sequence.add(srSkimmer)
sr_sequence.add(xsWeighter)
sr_sequence.add(dataMCWeighter)
sr_sequence.add(catProducer)
