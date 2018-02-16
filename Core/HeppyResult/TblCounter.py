# Tai Sakuma <tai.sakuma@cern.ch>
from ..mkdir_p import mkdir_p
from ..listToAlignedText import listToAlignedText
import os
from ReadCounter import ReadCounter

##____________________________________________________________________________||
class TblCounter(object):
    """This class reads counter files of HeppyResult.

    Args:
        analyzerName (str): the name of the Heppy analyzer, e.g., skimAnalyzerCount
        fileName (str): the name of the counter file, e.g., SkimReport.txt
        outPath (str): a path to the output file
        levels (list): a list of the levels to read. If not given, all levels will be read
        columnNames (list): a list of the column names of the output file. If not given, the levels will be used
    """
    def __init__(self, analyzerName, fileName, outPath, levels = None, columnNames = None):
        self.analyzerName = analyzerName
        self.fileName = fileName
        self._outPath = outPath
        self.levels = levels
        self.columnNames = columnNames

        self._readCounter = ReadCounter()

        if self.levels is not None:
            self._determine_columnNames_start_rows()

    def begin(self): pass

    def read(self, component):
        path = os.path.join(getattr(component, self.analyzerName).path, self.fileName)
        counter = self._readCounter(path)

        if self.levels is None:
            self.levels = counter.keys()
            self._determine_columnNames_start_rows()

        row = [component.name]
        for level, column in zip(self.levels, self.columnNames):
            row.append(counter[level]['count'])
        self._rows.append(row)

    def end(self):
        if self.levels is None:
            self._rows = [['component']]

        f = self._open(self._outPath)
        f.write(listToAlignedText(self._rows))
        self._close(f)

    def _determine_columnNames_start_rows(self):
        if self.columnNames is None:
            self.columnNames = self.levels

            # quote if space is in a level, e.g., "Sum Weights"
            self.columnNames = ['"' + n + '"' if ' ' in n else n for n in self.columnNames]
        self._rows = [['component'] + list(self.columnNames)]


    def _open(self, path):
        mkdir_p(os.path.dirname(path))
        return open(path, 'w')

    def _close(self, file): file.close()

##____________________________________________________________________________||
