from Core.ComponentList import *
from Core.Dataset import Dataset

cmp = Component(
        "",
        "",
        "Events",
        keyword="tree",
        inUFTier2=True,
        )

cmpList = ComponentList(
        [cmp,],
        )

 = Dataset(
        "",
        cmpList,
        xs                  = , #pb
        )
