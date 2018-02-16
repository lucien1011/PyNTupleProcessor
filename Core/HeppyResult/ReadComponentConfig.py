# Tai Sakuma <tai.sakuma@cern.ch>

##____________________________________________________________________________||
import os
import ast

##____________________________________________________________________________||
class ReadComponentConfig(object):
    def __call__(self, path):
        if not os.path.isfile(path): return None
        file = open(path)
        return self._readImp(file)

    def _readImp(self, file):
        file.readline() # skip the 1st line
        l = [[e.strip() for e in l.split(":", 1)] for l in file]
        return dict([(e[0], self._literal_eval_or_string(e[1])) for e in l])

    def _literal_eval_or_string(self, val):
        try:
            return ast.literal_eval(val)
        except:
            return val

##____________________________________________________________________________||
