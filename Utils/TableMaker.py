class TableMaker(object):
    def __init__(self):
        pass

    @staticmethod
    def printHeader(file,landscape=False):
        outStr = "\documentclass[12pt]{article}\n"
        outStr += "\\usepackage{longtable}\n"
        outStr += "\\usepackage{color, colortbl}\n"
        if landscape:
            outStr += "\\usepackage{lscape}"
        outStr += "\\begin{document}\n"
        outStr += "\\definecolor{Red}{rgb}{1,0,0}\n"

        file.write(outStr)

    @staticmethod
    def printEnd(file):
        outStr = "\end{document}\n"
        file.write(outStr)

    @staticmethod
    def printTableHeader(file,nColumn,cat,caption,landscape):
        outStr = ""
        if landscape:
            outStr += "\\begin{landscape}"
        outStr += "\\begin{longtable}{"+"| c "*nColumn+" | }\n"
        outStr += "\\caption{%s} \label{tab:%s} \\\\"%(caption,cat)
        outStr += "    \hline \n"
        file.write(outStr)

    @staticmethod
    def printTableEnd(file,landscape):
        outStr = ""
        outStr += "    \hline \n"
        outStr += "    \hline \n"
        outStr += "\end{longtable}\n"
        if landscape:
            outStr += "\\end{landscape}"
        #outStr += "  \end{tabular}\n"
        file.write(outStr)   

    @staticmethod
    def printTableContent(file,inputList):
        for rowContent in inputList:
            rowStr = ""
            for i,entry in enumerate(rowContent):
                if i != len(rowContent)-1:
                    rowStr += str(entry)+" & "
                else:
                    rowStr += str(entry)
            rowStr += "\\\\ \hline \n"
            file.write(rowStr)
    
    @classmethod
    def makeTexFile(cls,outFilePath,tableDict,isANInput=False,landscape=False):
        outFile = open(outFilePath,"w")
        if not isANInput:
            cls.printHeader(outFile,landscape)
        cls.printTableHeader(outFile,tableDict["nColumn"],tableDict["tab"],tableDict["caption"],landscape)
        cls.printTableContent(outFile,tableDict["tableList"])
        cls.printTableEnd(outFile,landscape)
        if not isANInput:
            cls.printEnd(outFile)
        outFile.close()
