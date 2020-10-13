import sys
sys.path = ['', '/home/nikmenendez/.local/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/share/overrides/python', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/cmssw/CMSSW_9_4_4/python', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/cmssw/CMSSW_9_4_4/lib/slc6_amd64_gcc630', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/coral/CORAL_2_3_21-fmblme4/slc6_amd64_gcc630/python', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/coral/CORAL_2_3_21-fmblme4/slc6_amd64_gcc630/lib', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/professor2/2.2.1-fmblme5/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/pyqt/4.11.4-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/sherpa/2.2.4-fmblme2/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/rivet/2.5.4/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/python-ldap/2.4.10-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-matplotlib/1.5.2-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/sip/4.17-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/llvm/4.0.1/lib64/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-sqlalchemy/1.1.4-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-lint/0.25.1-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-dxr/1.0-fmblme3/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-cx-oracle/5.2.1-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-numpy/1.12.1-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/frontier_client/2.8.20-fmblme/python/lib', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/das_client/v03.01.00-fmblme/bin', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/xrootd/4.6.1-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/yoda/1.6.7/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/lcg/root/6.10.08/lib', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/pyminuit2/0.0.1-fmblme3/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-PyYAML/3.11-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-pygithub/1.23.0-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-pip/9.0.1-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-dablooms/0.9.1-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-pippkgs_depscipy/3.0-fmblme4/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-pippkgs/6.0-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/professor/1.4.0-fmblme3/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/dbs-client/DBS_2_1_9-fmblme/lib', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/dbs-client/DBS_2_1_9-fmblme/lib/DBSAPI', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/cvs2git/5419-fmblme/lib', '/blue/avery/nikmenendez/Wto3l/Analyzer2/UF-PyNTupleRunner/Wto3l', '/blue/avery/nikmenendez/Wto3l/Analyzer2/UF-PyNTupleRunner', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-sqlalchemy/1.1.4-fmblme/lib/python2.7/site-packages/SQLAlchemy-1.1.4-py2.7-linux-x86_64.egg', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-numpy/1.12.1-fmblme/lib/python2.7/site-packages/numpy-1.12.1-py2.7-linux-x86_64.egg', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/python/2.7.11-fmblme/lib/python27.zip', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/python/2.7.11-fmblme/lib/python2.7', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/python/2.7.11-fmblme/lib/python2.7/plat-linux2', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/python/2.7.11-fmblme/lib/python2.7/lib-tk', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/python/2.7.11-fmblme/lib/python2.7/lib-old', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/python/2.7.11-fmblme/lib/python2.7/lib-dynload', '/home/nikmenendez/.local/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/python/2.7.11-fmblme/lib/python2.7/site-packages']

import time

#start_import = time.time()
from Core.Module import Module
import ROOT as r
from ROOT import TLorentzVector 
import math as m
from Utils.DeltaR import deltaR
from random import choice
import numpy as np
from tensorflow.keras.models import model_from_json, load_model
from tensorflow.keras.backend import clear_session
#end_import = time.time()

class ZSelector(Module):
    def __init__(self,name):
        super(ZSelector,self).__init__(name)

    def analyze(self,event):
	start_import = time.time()
	event.Lep1, event.Lep2, event.Lep3, event.Met = TLorentzVector(), TLorentzVector(), TLorentzVector(), TLorentzVector(),
        event.Met.SetPtEtaPhiM(event.met[0],0,event.met_phi[0],0)
        event.Lep_leading_fromM1, event.Lep_leading_fromM2 = TLorentzVector(), TLorentzVector(),
	# --------- Order leptons by pT. L1 and L2 are tight muons, L3 is loose. L1 and L2 already ordered by pT. --------
	if event.pTL3[0] > event.pTL1[0]:
		event.Lep1.SetPtEtaPhiM(event.pTL3[0],event.etaL3[0],event.phiL3[0],event.massL3[0])
		event.Lep2.SetPtEtaPhiM(event.pTL1[0],event.etaL1[0],event.phiL1[0],event.massL1[0])
		event.Lep3.SetPtEtaPhiM(event.pTL2[0],event.etaL2[0],event.phiL2[0],event.massL2[0])

		Lep1id = event.idL3[0]
		Lep2id = event.idL1[0]
		Lep3id = event.idL2[0]

		event.Lep1Iso = event.IsoL3[0]
		event.Lep2Iso = event.IsoL1[0]
		event.Lep3Iso = event.IsoL2[0]

		event.Lep1Mom = event.MomIdL3[0]
		event.Lep2Mom = event.MomIdL1[0]
		event.Lep3Mom = event.MomIdL2[0]
	elif event.pTL3[0] > event.pTL2[0] and event.pTL1[0] > event.pTL3[0]:
		event.Lep1.SetPtEtaPhiM(event.pTL1[0],event.etaL1[0],event.phiL1[0],event.massL1[0])
                event.Lep2.SetPtEtaPhiM(event.pTL3[0],event.etaL3[0],event.phiL3[0],event.massL3[0])
                event.Lep3.SetPtEtaPhiM(event.pTL2[0],event.etaL2[0],event.phiL2[0],event.massL2[0])

		Lep1id = event.idL1[0]
                Lep2id = event.idL3[0]
                Lep3id = event.idL2[0]

		event.Lep1Iso = event.IsoL1[0]
                event.Lep2Iso = event.IsoL3[0]
                event.Lep3Iso = event.IsoL2[0]

		event.Lep1Mom = event.MomIdL1[0]
                event.Lep2Mom = event.MomIdL3[0]
                event.Lep3Mom = event.MomIdL2[0]
	elif event.pTL3[0] < event.pTL2[0]:
		event.Lep1.SetPtEtaPhiM(event.pTL1[0],event.etaL1[0],event.phiL1[0],event.massL1[0])
                event.Lep2.SetPtEtaPhiM(event.pTL2[0],event.etaL2[0],event.phiL2[0],event.massL2[0])
                event.Lep3.SetPtEtaPhiM(event.pTL3[0],event.etaL3[0],event.phiL3[0],event.massL3[0])

		Lep1id = event.idL1[0]
                Lep2id = event.idL2[0]
                Lep3id = event.idL3[0]

		event.Lep1Iso = event.IsoL1[0]
                event.Lep2Iso = event.IsoL2[0]
                event.Lep3Iso = event.IsoL3[0]

		event.Lep1Mom = event.MomIdL1[0]
                event.Lep2Mom = event.MomIdL2[0]
                event.Lep3Mom = event.MomIdL3[0]
	# ----------------------------------------------------------------------------------------------------------------
	vec = event.Lep1 + event.Lep2 + event.Lep3 + event.Met
	v3l = event.Lep1 + event.Lep2 + event.Lep3
        event.mt = vec.Mt()
	event.m3l = v3l.M()
        totallep = event.Lep1 + event.Lep2 + event.Lep3

	event.dR12 = deltaR(event.Lep1.Eta(),event.Lep1.Phi(),event.Lep2.Eta(),event.Lep2.Phi())
        event.dR13 = deltaR(event.Lep1.Eta(),event.Lep1.Phi(),event.Lep3.Eta(),event.Lep3.Phi())
        event.dR23 = deltaR(event.Lep2.Eta(),event.Lep2.Phi(),event.Lep3.Eta(),event.Lep3.Phi())

	# --------- Define Mass1 as the highest pT muon + highest pT anti-muon -------------------------------------------
	#if Lep1id + Lep2id == 0:
	#	P1 = event.Lep1 + event.Lep2
	#	if Lep1id + Lep3id == 0: 
	#		P2 = event.Lep1 + event.Lep3
	#	else:
	#		P2 = event.Lep2 + event.Lep3
	#elif Lep1id + Lep3id == 0:
	#	P1 = event.Lep1 + event.Lep3
	#	if Lep1id + Lep2id == 0:
	#		P2 = event.Lep1 + event.Lep2
	#	else:
	#		P2 = event.Lep2 + event.Lep3
	# ----------------------------------------------------------------------------------------------------------------

	# --------- Define Mass1 as two closet muons ---------------------------------------------------------------------
	#if Lep1id + Lep2id == 0:
	#	if Lep1id + Lep3id == 0:
	#		if deltaR(event.Lep1.Eta(),event.Lep1.Phi(),event.Lep2.Eta(),event.Lep2.Phi()) < deltaR(event.Lep1.Eta(),event.Lep1.Phi(),event.Lep3.Eta(),event.Lep3.Phi()):
	#			P1 = event.Lep1 + event.Lep2
	#			P2 = event.Lep1 + event.Lep3
	#		else:
	#			P1 = event.Lep1 + event.Lep3
	#			P2 = event.Lep1 + event.Lep2
	#	elif Lep2id + Lep3id == 0:
	#		if deltaR(event.Lep1.Eta(),event.Lep1.Phi(),event.Lep2.Eta(),event.Lep2.Phi()) < deltaR(event.Lep2.Eta(),event.Lep2.Phi(),event.Lep3.Eta(),event.Lep3.Phi()):
	#			P1 = event.Lep1 + event.Lep2
	#			P2 = event.Lep2 + event.Lep3
	#		else:
	#			P1 = event.Lep2 + event.Lep3
	#			P2 = event.Lep1 + event.Lep2
	#elif Lep1id + Lep3id == 0:
	#	if Lep1id + Lep2id == 0:
	#		if deltaR(event.Lep1.Eta(),event.Lep1.Phi(),event.Lep2.Eta(),event.Lep2.Phi()) < deltaR(event.Lep1.Eta(),event.Lep1.Phi(),event.Lep3.Eta(),event.Lep3.Phi()):
        #                        P1 = event.Lep1 + event.Lep2
        #                        P2 = event.Lep1 + event.Lep3
        #                else:
        #                        P1 = event.Lep1 + event.Lep3
        #                        P2 = event.Lep1 + event.Lep2
	#	elif Lep2id + Lep3id == 0:
	#		if deltaR(event.Lep1.Eta(),event.Lep1.Phi(),event.Lep3.Eta(),event.Lep3.Phi()) < deltaR(event.Lep2.Eta(),event.Lep2.Phi(),event.Lep3.Eta(),event.Lep3.Phi()):
        #                        P1 = event.Lep1 + event.Lep3
        #                        P2 = event.Lep2 + event.Lep3
        #                else:
        #                        P1 = event.Lep2 + event.Lep3
        #                        P2 = event.Lep1 + event.Lep3
	# ----------------------------------------------------------------------------------------------------------------

	# --------- Define Mass1 From Neural Network ---------------------------------------------------------------------
	start_selection = time.time()
	start_load = time.time()
	clear_session()
	ZSelector = load_model('/blue/avery/nikmenendez/Wto3l/Analyzer2/UF-PyNTupleRunner/Wto3l/MVA/ZSelector_model.h5', compile=False)
	#json_file = open("/blue/avery/nikmenendez/Wto3l/Analyzer2/UF-PyNTupleRunner/Wto3l/MVA/ZSelector_model.json", 'r')
	#loaded_model_json = json_file.read()
	#json_file.close()
	#ZSelector = model_from_json(loaded_model_json)
	#ZSelector.load_weights("/blue/avery/nikmenendez/Wto3l/Analyzer2/UF-PyNTupleRunner/Wto3l/MVA/ZSelector_weights.h5")
	end_load = time.time()

	start_array = time.time()
	Selector_vars = np.array((event.Lep1.Pt(),event.Lep1.Eta(),event.Lep1.Phi(),event.Lep1Iso,Lep1id,
			 	  event.Lep2.Pt(),event.Lep2.Eta(),event.Lep2.Phi(),event.Lep2Iso,Lep2id,
			 	  event.Lep3.Pt(),event.Lep3.Eta(),event.Lep3.Phi(),event.Lep3Iso,Lep3id,
			 	  event.met[0], event.met_phi[0], event.dR12, event.dR13, event.dR23))
	Selector_vars = Selector_vars.reshape(1,-1)
	end_array = time.time()

	start_predict = time.time()
	prediction_0 = ZSelector.predict(Selector_vars)
	end_predict = time.time()	

	start_max = time.time()
	max_guess = 0
	guess_2nd = 0
	guess_slot = 0
	guess_2nd_slot = 0
	for i in range(len(prediction_0[0])):
	    if prediction_0[0][i] > max_guess:
	        guess_2nd = max_guess
	        guess_2nd_slot = guess_slot
	        max_guess = prediction_0[0][i]
	        guess_slot = i
	    elif prediction_0[0][i] > guess_2nd:
	        guess_2nd = prediction_0[0][i]
	        guess_slot = i
	end_max = time.time()

	start_assign = time.time()
	if guess_slot == 0:
		guess_slot == guess_2nd_slot

	if guess_slot == 1:
		P1 = event.Lep1 + event.Lep2
		if Lep1id + Lep3id == 0:
			P2 = event.Lep1 + event.Lep3
		elif Lep2id + Lep3id == 0:
			P2 = event.Lep2 + event.Lep3
	elif guess_slot == 2:
		P1 = event.Lep1 + event.Lep3
		if Lep1id + Lep2id == 0:
			P2 = event.Lep1 + event.Lep2
		elif Lep2id + Lep3id == 0:
			P2 = event.Lep2 + event.Lep3
	elif guess_slot == 3:
		P1 = event.Lep2 + event.Lep3
		if Lep1id + Lep2id == 0:
			P2 = event.Lep1 + event.Lep2
		elif Lep1id + Lep3id == 0:
			P2 = event.Lep1 + event.Lep3
	end_assign = time.time()
	end_selection = time.time()
	# ----------------------------------------------------------------------------------------------------------------
	event.mass1  = P1.M()
        event.mass2  = P2.M()
        event.mass1_pt = P1.Pt()
        event.mass2_pt = P2.Pt()
        event.mass1_eta = P1.Eta()
        event.mass2_eta = P2.Eta()
        event.mass1_coseta = m.cos(P1.Eta())
        event.mass2_coseta = m.cos(P2.Eta())
        event.mass1_phi = P1.Phi()
        event.mass2_phi = P2.Phi()

	#event.dR12 = deltaR(event.Lep1.Eta(),event.Lep1.Phi(),event.Lep2.Eta(),event.Lep2.Phi())
	#event.dR13 = deltaR(event.Lep1.Eta(),event.Lep1.Phi(),event.Lep3.Eta(),event.Lep3.Phi())
	#event.dR23 = deltaR(event.Lep2.Eta(),event.Lep2.Phi(),event.Lep3.Eta(),event.Lep3.Phi())

	if abs(event.Lep1Mom) == 999888: event.Lep1FromZ = 1
	else: event.Lep1FromZ = 0

	if abs(event.Lep2Mom) == 999888: event.Lep2FromZ = 1
        else: event.Lep2FromZ = 0

	if abs(event.Lep3Mom) == 999888: event.Lep3FromZ = 1
        else: event.Lep3FromZ = 0

	#iMass = 60
	#if (iMass-1) < event.mass1 < (iMass+1):
	#	event.MCorrect = 1
	#elif (iMass-1) < event.mass2 < (iMass+1):
	#	event.MCorrect = 2
	#else:
	#	event.MCorrect = 0

	end_import = time.time()
	print "\n Time to ZSelect = %f s / Time to load = %f s / Time to array = %f s / Time to predict = %f s / Time to get max = %f s / Time to assign = %f s / Time for selection = %f s" % (end_import - start_import, end_load - start_load, end_array - start_array, end_predict - start_predict, end_max - start_max, end_assign - start_assign, end_selection - start_selection)

	if 80 < event.mass1 < 100 or 80 < event.mass2 < 100:
            return False

	return True
