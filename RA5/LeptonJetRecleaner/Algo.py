from Core.Collection import Collection 
from Utils.DeltaR import deltaR

import ROOT

class LeptonJetRecleaner(object):

    def __init__(self,name,label,looseLeptonSel,cleaningLeptonSel,FOLeptonSel,tightLeptonSel,cleanJet,selectJet,cleanTau,looseTau,tightTau,cleanJetsWithTaus,doVetoZ,doVetoLMf,doVetoLMt,jetPt,bJetPt,coneptdef,storeJetVariables=False,cleanTausWithLoose=False,jetVarToStore="pt eta phi mass btagCSV"):
        self.name = name
        self.label = "" if (label in ["",None]) else ("_"+label)
        self.looseLeptonSel = looseLeptonSel
        self.cleaningLeptonSel = cleaningLeptonSel # applied on top of looseLeptonSel
        self.FOLeptonSel = FOLeptonSel # applied on top of looseLeptonSel
        self.tightLeptonSel = tightLeptonSel # applied on top of looseLeptonSel
        self.cleanJet = cleanJet
        self.selectJet = selectJet
        self.cleanTau = cleanTau
        self.looseTau = looseTau
        self.tightTau = tightTau
        self.cleanJetsWithTaus = cleanJetsWithTaus
        self.cleanTausWithLoose = cleanTausWithLoose
        self.doVetoZ = doVetoZ
        self.doVetoLMf = doVetoLMf
        self.doVetoLMt = doVetoLMt
        self.coneptdef = coneptdef
        self.jetPt = jetPt
        self.bJetPt = bJetPt
        self.strJetPt = str(int(jetPt))
        self.strBJetPt = str(int(bJetPt))
        self.systsJEC = {0:"", 1:"_jecUp", -1:"_jecDown"}
        self.debugprinted = False
        self.storeJetVariables = storeJetVariables
        self.jetVarToStore = jetVarToStore
        self.btagCSVLoose = 0.5426
        self.btagCSVMedium = 0.8484

    def fillCollWithVeto(self,ret,refcollection,leps,lab,labext,selection,lepsforveto,doVetoZ,doVetoLM,sortby,ht=-1,pad_zeros_up_to=20):
        ret['i'+lab] = [];
        ret['i'+lab+'V'] = [];
        for lep in leps:
            if (selection(lep) if ht<0 else selection(lep,ht)):
                ret['i'+lab].append(refcollection.index(lep))
        ret['i'+lab] = self.sortIndexListByFunction(ret['i'+lab],refcollection,sortby)
        ret['nLep'+labext] = len(ret['i'+lab])
        ret['LepGood_is'+labext] = [(1 if i in ret['i'+lab] else 0) for i in xrange(len(refcollection))]
        lepspass = [ refcollection[il] for il in ret['i'+lab]  ]
        if lepsforveto==None: lepsforveto = lepspass # if lepsforveto==None, veto selected leptons among themselves
        for lep in lepspass:
            if (not doVetoZ  or passMllTLVeto(lep, lepsforveto, 76, 106, True)) and \
               (not doVetoLM or passMllTLVeto(lep, lepsforveto,  0,  12, True)):
                ret['i'+lab+'V'].append(refcollection.index(lep))
        ret['i'+lab+'V'] = self.sortIndexListByFunction(ret['i'+lab+'V'],refcollection,sortby)
        ret['nLep'+labext+'Veto'] = len(ret['i'+lab+'V'])
        ret['LepGood_is'+labext+'Veto'] = [(1 if i in ret['i'+lab+'V'] else 0) for i in xrange(len(refcollection))]
        lepspassveto = [ refcollection[il] for il in ret['i'+lab+'V']  ]
        ret['i'+lab] = ret['i'+lab] + [0]*(pad_zeros_up_to-len(ret['i'+lab]))
        ret['i'+lab+'V'] = ret['i'+lab+'V'] + [0]*(pad_zeros_up_to-len(ret['i'+lab+'V']))
        return (ret,lepspass,lepspassveto)

    def sortIndexListByFunction(self,indexlist,parentcollection,func):
        if not func: return indexlist[:]
        newsort = sorted([(ij,parentcollection[ij]) for ij in indexlist], key = lambda x: func(x[1]), reverse=True)
        return [x[0] for x in newsort]

    def recleanJets(self,jetcollcleaned,jetcolldiscarded,lepcoll,postfix,ret,jetret,discjetret):
        ### Define jets
        ret["iJSel"+postfix] = []
        ret["iDiscJSel"+postfix] = []
        # 0. mark each jet as clean
        for j in jetcollcleaned+jetcolldiscarded: j._clean = True
        # 1. associate to each lepton passing the cleaning selection its nearest jet 
        for lep in lepcoll:
            best = None; bestdr = 0.4
            for j in jetcollcleaned+jetcolldiscarded:
                dr = deltaR(lep,j)
                if dr < bestdr:
                    best = j; bestdr = dr
            if best is not None and self.cleanJet(lep,best,bestdr):
                best._clean = False
        # 2. compute the jet list
        for ijc,j in enumerate(jetcollcleaned):
            if not self.selectJet(j): continue
            elif not j._clean: ret["iDiscJSel"+postfix].append(ijc)
            else: 
                ret["iJSel"+postfix].append(ijc)
        for ijd,j in enumerate(jetcolldiscarded):
            if not self.selectJet(j): continue
            elif not j._clean: ret["iDiscJSel"+postfix].append(-1-ijd)
            else: 
                ret["iJSel"+postfix].append(-1-ijd)
        # 3. sort the jets by pt
        ret["iJSel"+postfix].sort(key = lambda idx : jetcollcleaned[idx].pt if idx >= 0 else jetcolldiscarded[-1-idx].pt, reverse = True)
        ret["iDiscJSel"+postfix].sort(key = lambda idx : jetcollcleaned[idx].pt if idx >= 0 else jetcolldiscarded[-1-idx].pt, reverse = True)
        ret["nJetSel"+postfix] = len(ret["iJSel"+postfix])
        ret["nDiscJetSel"+postfix] = len(ret["iDiscJSel"+postfix])
        # 4. if needed, store the jet 4-vectors
        if self.storeJetVariables:
            #print postfix, self.label
            if postfix==self.label:
                for jfloat in self.jetVarToStore.split():
                    jetret[jfloat] = []
                    discjetret[jfloat] = []
                for idx in ret["iJSel"+postfix]:
                    jet = jetcollcleaned[idx] if idx >= 0 else jetcolldiscarded[-1-idx]
                    for jfloat in self.jetVarToStore.split():
                        jetret[jfloat].append( getattr(jet,jfloat) )
                for idx in ret["iDiscJSel"+postfix]:
                    jet = jetcollcleaned[idx] if idx >= 0 else jetcolldiscarded[-1-idx]
                    for jfloat in self.jetVarToStore.split():
                        discjetret[jfloat].append( getattr(jet,jfloat) )
         # 5. compute the sums
        ret["nJet"+self.strBJetPt+postfix] = 0; ret["htJet"+self.strBJetPt+"j"+postfix] = 0; ret["mhtJet"+self.strBJetPt+postfix] = 0; ret["nBJetLoose"+self.strBJetPt+postfix] = 0; ret["nBJetMedium"+self.strBJetPt+postfix] = 0
        ret["nJet"+self.strJetPt+postfix] = 0; ret["htJet"+self.strJetPt+"j"+postfix] = 0; ret["mhtJet"+self.strJetPt+postfix] = 0; ret["nBJetLoose"+self.strJetPt+postfix] = 0; ret["nBJetMedium"+self.strJetPt+postfix] = 0
        cleanjets = [];
        mhtBJetPtvec = ROOT.TLorentzVector(0,0,0,0)
        mhtJetPtvec = ROOT.TLorentzVector(0,0,0,0)
        for x in lepcoll: mhtBJetPtvec = mhtBJetPtvec - x.p4()
        for x in lepcoll: mhtJetPtvec = mhtJetPtvec - x.p4()
        for j in jetcollcleaned+jetcolldiscarded:
            if not (j._clean and self.selectJet(j)): continue
            cleanjets.append(j)
            if j.pt > float(self.bJetPt):
                ret["nJet"+self.strBJetPt+postfix] += 1; ret["htJet"+self.strBJetPt+"j"+postfix] += j.pt; 
                if j.btagCSV>self.btagCSVLoose: ret["nBJetLoose"+self.strBJetPt+postfix] += 1
                if j.btagCSV>self.btagCSVMedium: ret["nBJetMedium"+self.strBJetPt+postfix] += 1
                mhtBJetPtvec = mhtBJetPtvec - j.p4()
            if j.pt > float(self.jetPt):
                ret["nJet"+self.strJetPt+postfix] += 1; ret["htJet"+self.strJetPt+"j"+postfix] += j.pt; 
                if j.btagCSV>self.btagCSVLoose: ret["nBJetLoose"+self.strJetPt+postfix] += 1
                if j.btagCSV>self.btagCSVMedium: ret["nBJetMedium"+self.strJetPt+postfix] += 1
                mhtJetPtvec = mhtJetPtvec - j.p4()
        ret["mhtJet"+self.strBJetPt+postfix] = mhtBJetPtvec.Pt()
        ret["mhtJet"+self.strJetPt+postfix] = mhtJetPtvec.Pt()
        return cleanjets

    def recleanTaus(self, taucollcleaned, taucolldiscarded, lepcoll, postfix, ret, tauret, event):
        ### Define taus
        alltaus = taucollcleaned + taucolldiscarded
        # 0. mark each tau as clean
        for t in alltaus: t._clean = True
        # 1. check for every tau if it is too close to a loose lepton
        for t in alltaus:
            for lep in lepcoll:
                dr = deltaR(lep, t)
                if self.cleanTau(lep, t, dr):
                    t._clean = False
        # 2. compute the tau list
        ret["iTauSel"+postfix]=[]
        for itc, t in enumerate(taucollcleaned):
            if not t._clean        : continue
            if not self.looseTau(t): continue
            setattr(t, "reclTauId", 1 + self.tightTau(t))
            ret["iTauSel"+postfix].append(itc)
        for itd, t in enumerate(taucolldiscarded):
            if not t._clean        : continue
            if not self.looseTau(t): continue
            setattr(t, "reclTauId", 1 + self.tightTau(t))
            ret["iTauSel"+postfix].append(-1-itd)
        # 3. sort the taus by pt
        ret["iTauSel"+postfix].sort(key = lambda idx : taucollcleaned[idx].pt if idx >= 0 else taucolldiscarded[-1-idx].pt, reverse = True)
        goodtaus = [(taucollcleaned[idx] if idx >= 0 else taucolldiscarded[-1-idx]) for idx in ret["iTauSel"+postfix]]
        ret["nTauSel"      + postfix] = len(goodtaus)
        ret["nTightTauSel" + postfix] = sum([1 for g in goodtaus if g.reclTauId == 2])
        # 4. store the tau 4-vectors
        if postfix==self.label:
            for tfloat in "pt eta phi mass reclTauId pdgId".split():
                tauret[tfloat] = []
                for g in goodtaus:
                    tauret[tfloat].append( getattr(g, tfloat) )
            for tfloat in "mcMatchId".split():
                tauret[tfloat] = []
                for g in goodtaus:
                    tauret[tfloat].append( getattr(g, tfloat) if hasattr(event,"TauGood_"+tfloat) else -99 )
        return goodtaus

    def __call__(self,event):
        self.ev = event
        fullret = {}
        leps = [l for l in Collection(event,"LepGood")]
        if not self.coneptdef: raise RuntimeError, 'Choose the definition to be used for cone pt'
        for lep in leps: lep.conept = self.coneptdef(lep)
        tausc = [t for t in Collection(event,"TauGood")]
        tausd = [t for t in Collection(event,"TauOther")] 
        jetsc={}
        jetsd={}
        for var in self.systsJEC:
            _var = var
            if not hasattr(event,"nJet"+self.systsJEC[var]):
                _var = 0
                if not self.debugprinted:
                    print '-'*15
                    print 'WARNING: jet energy scale variation %s not found, will set it to central value'%self.systsJEC[var]
                    print '-'*15
            jetsc[var] = [j for j in Collection(event,"Jet"+self.systsJEC[_var])]
            jetsd[var] = [j for j in Collection(event,"DiscJet"+self.systsJEC[_var])]
        self.debugprinted = True
        ret = {}; retwlabel = {}; jetret = {}; discjetret = {};
        lepsl = []; lepslv = [];
        ret, lepsl, lepslv = self.fillCollWithVeto(ret,leps,leps,'L','Loose',self.looseLeptonSel, lepsforveto=None, doVetoZ=self.doVetoZ, doVetoLM=self.doVetoLMf, sortby=None)
        lepsc = []; lepscv = [];
        ret, lepsc, lepscv = self.fillCollWithVeto(ret,leps,lepsl,'C','Cleaning',self.cleaningLeptonSel, lepsforveto=lepsl, doVetoZ=self.doVetoZ, doVetoLM=self.doVetoLMf, sortby=None)

        ret['mZ1'] = bestZ1TL(lepsl, lepsl)
        ret['minMllAFAS'] = minMllTL(lepsl, lepsl) 
        ret['minMllAFOS'] = minMllTL(lepsl, lepsl, paircut = lambda l1,l2 : l1.charge !=  l2.charge) 
        ret['minMllAFSS'] = minMllTL(lepsl, lepsl, paircut = lambda l1,l2 : l1.charge ==  l2.charge) 
        ret['minMllSFOS'] = minMllTL(lepsl, lepsl, paircut = lambda l1,l2 : l1.pdgId  == -l2.pdgId) 

        loosetaus=[]; rettlabel = {}; tauret = {}; 
        loosetaus = self.recleanTaus(tausc, tausd, lepsl if self.cleanTausWithLoose else lepsc, self.label, rettlabel, tauret, event)

        cleanjets={}
        for var in self.systsJEC:
            cleanjets[var] = self.recleanJets(jetsc[var],jetsd[var],lepsc+loosetaus if self.cleanJetsWithTaus else lepsc,self.label+self.systsJEC[var],retwlabel,jetret,discjetret)

        # calculate FOs and tight leptons using the cleaned HT, sorted by conept
        lepsf = []; lepsfv = [];
        ret, lepsf, lepsfv = self.fillCollWithVeto(ret,leps,lepsl,'F','FO',self.FOLeptonSel,lepsforveto=lepsl,ht=retwlabel["htJet"+self.strJetPt+"j"+self.label],sortby = lambda x: x.conept, doVetoZ=self.doVetoZ, doVetoLM=self.doVetoLMf)
        lepst = []; lepstv = [];
        ret, lepst, lepstv = self.fillCollWithVeto(ret,leps,lepsl,'T','Tight',self.tightLeptonSel,lepsforveto=lepsl,ht=retwlabel["htJet"+self.strJetPt+"j"+self.label],sortby = lambda x: x.conept, doVetoZ=self.doVetoZ, doVetoLM=self.doVetoLMt)


        ### attach labels and return
        fullret["nLepGood"]=len(leps)
        fullret["LepGood_conePt"] = [lep.conept for lep in leps]
        for k,v in ret.iteritems(): 
            fullret[k+self.label] = v
        fullret.update(retwlabel)
        fullret.update(rettlabel)
        for k,v in tauret.iteritems(): 
            fullret["TauSel%s_%s" % (self.label,k)] = v
        for k,v in jetret.iteritems(): 
            fullret["JetSel%s_%s" % (self.label,k)] = v
        return fullret


def bestZ1TL(lepsl,lepst,cut=lambda lep:True):
      pairs = []
      for l1 in lepst:
        if not cut(l1): continue
        for l2 in lepsl:
            if not cut(l2): continue
            if l1.pdgId == -l2.pdgId:
               mz = (l1.p4() + l2.p4()).M()
               diff = abs(mz-91)
               pairs.append( (diff,mz) )
      if len(pairs):
          pairs.sort()
          return pairs[0][1]
      return 0.

def minMllTL(lepsl, lepst, bothcut=lambda lep:True, onecut=lambda lep:True, paircut=lambda lep1,lep2:True):
        pairs = []
        for l1 in lepst:
            if not bothcut(l1): continue
            for l2 in lepsl:
                if l2 == l1 or not bothcut(l2): continue
                if not onecut(l1) and not onecut(l2): continue
                if not paircut(l1,l2): continue
                mll = (l1.p4() + l2.p4()).M()
                pairs.append(mll)
        if len(pairs):
            return min(pairs)
        return -1

def passMllVeto(l1, l2, mZmin, mZmax, isOSSF ):
    if  l1.pdgId == -l2.pdgId or not isOSSF:
        mz = (l1.p4() + l2.p4()).M()
        if mz > mZmin and  mz < mZmax:
            return False
    return True

def passMllTLVeto(lep, lepsl, mZmin, mZmax, isOSSF):
    for ll in lepsl:
        if ll == lep: continue
        if not passMllVeto(lep, ll, mZmin, mZmax, isOSSF):
            return False
    return True

def passTripleMllVeto(l1, l2, l3, mZmin, mZmax, isOSSF ):
    ls = [passMllVeto(l1, l2, mZmin, mZmax, isOSSF), \
          passMllVeto(l1, l3, mZmin, mZmax, isOSSF), \
          passMllVeto(l2, l3, mZmin, mZmax, isOSSF)]
    if all(ls): return True
    return False
