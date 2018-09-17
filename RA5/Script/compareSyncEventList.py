ufTextFilePath = "/home/lucien/public_html/SUSY/RA5/Sync2016/2018-09-16/uf_TTW_80X_dump_leptons.txt"
#ucTextFilePath = "/home/lucien/public_html/SUSY/RA5/Sync2016/2018-09-02/ucsx_TTW_80X_dump_global.txt"
ucTextFilePath = "/home/lucien/public_html/SUSY/RA5/Sync2016/2018-09-02/uf_TTW_80X_dump_leptons.txt"

ufEvtList = []
uff = open(ufTextFilePath,"r")
lines = uff.readlines()
for l in lines:
    key = l.split()
    run = key[0]
    lumi = key[1]
    evt = key[2]
    ufEvtList.append((run,lumi,evt))

ucEvtList = []
ucf = open(ucTextFilePath,"r")
lines = ucf.readlines()
for l in lines:
    key = l.split()
    run = key[0]
    lumi = key[1]
    evt = key[2]
    ucEvtList.append((run,lumi,evt))

for key in ufEvtList:
    if key not in ucEvtList: print key
print "-"*50
for key in ucEvtList:
    if key not in ufEvtList: print key

