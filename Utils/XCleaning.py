from DeltaR import deltaR2

def cleanJetsAndLeptons(jets,leptons,deltaR,arbitration=lambda jet,lepton: lepton):
    dr2 = deltaR**2
    goodjet = [ True for j in jets ]
    goodlep = [ True for l in leptons ]
    for il, l in enumerate(leptons):
        ibest, d2m = -1, dr2
        for i,j in enumerate(jets):
            d2i = deltaR2(l.eta,l.phi, j.eta,j.phi)
            if d2i < dr2:
                choice = arbitration(j,l)
                if choice == j:
                   # if the two match, and we prefer the jet, then drop the lepton and be done
                   goodlep[il] = False
                   break 
                elif choice == (j,l) or choice == (l,j):
                   # asked to keep both, so we don't consider this match
                   continue
            if d2i < d2m:
                ibest, d2m = i, d2i
        # this lepton has been killed by a jet, then we clean the jet that best matches it
        if not goodlep[il]: continue 
        if ibest != -1: goodjet[ibest] = False
    return ( [ j for (i ,j) in enumerate(jets)    if goodjet[i ] == True ], 
             [ l for (il,l) in enumerate(leptons) if goodlep[il] == True ] )
