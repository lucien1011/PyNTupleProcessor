enum anal_type_t { HighHigh = 0, HighLow = 1, LowLow = 2, Undefined = -1 };
anal_type_t analysisCategory(int id1, int id2, float lep1pt, float lep2pt){
  if      (lep1pt > ptCutHigh     && lep2pt > ptCutHigh)      return HighHigh;
  else if (lep1pt > ptCutHigh     && lep2pt > ptCutLowAG(id2))  return HighLow;
  else if (lep2pt > ptCutHigh     && lep1pt > ptCutLowAG(id1))  return HighLow;
  else if (lep1pt > ptCutLowAG(id1) && lep2pt > ptCutLowAG(id2))  return LowLow;
  return Undefined;
}
int signalRegionChargeSplit_HH_HL_38_HT_splitnjets(int njets, int nbtags, float met, float ht, float mt_min, int id1, int id2, float lep1pt, float lep2pt){

  //Calculate lep_pt
  anal_type_t lep_pt = analysisCategory(id1, id2, lep1pt, lep2pt); 

  // remember that sgn(pdgid) != sgn(charge), it's flipped. so mad.
  int mm = (id1 > 0);

  //Reject events out of kinematic acceptance
  if (met < 50) return -1; 
  if (njets < 2) return -1; 
  if (lep_pt != LowLow && met > 500 && ht < 300) return -1; 
  if (lep_pt != LowLow && njets>=2 && met>300 && ht<300) return -1;

  //High-high
  if (lep_pt == HighHigh){
    if (met >= 300 && ht >= 300) {
        if(met < 500 && njets<5) return 42+mm;
        else if(met < 500) return 56+mm;
        else if (njets<5) return 58+mm;
        else return 44+mm;
    }
    if (ht >= 1125) {
        if(ht < 1300 && njets<5) return 46;
        else if(ht < 1300 && (njets==5 || njets==6)) return 47;
        else if(ht < 1300 && njets>6) return 48;
        else if(ht < 1600 && njets<5) return 49;
        else if(ht < 1600 && (njets==5 || njets==6)) return 50;
        else if(ht < 1600 && njets>6) return 51;
        else if(njets<5) return 60;
        else if((njets==5 || njets==6)) return 61;
        else if(njets>6) return 62;
    }
    if (ht < 300){
      if (nbtags == 0 && mt_min < 120 && met < 200 && njets <= 4) return 1; 
      if (nbtags == 0) return 3; 
      if (nbtags == 1 && mt_min < 120 && met < 200 && njets <= 4) return 11;
      if (nbtags == 1) return 13+mm; 
      if (nbtags == 2 && mt_min < 120 && met < 200 && njets <= 4) return 23; 
      if (nbtags == 2) return 25+mm; 
      if (nbtags >= 3 && mt_min < 120 && met < 200) return 35+mm; 
      if (nbtags >= 3 && mt_min < 120 && met >= 200) return 35+mm; 
      if (nbtags >= 3) return 40;
    }
    if (ht >= 300 && ht < 1125){
      if (nbtags == 0){
        if (mt_min < 120 && met < 200 && njets <= 4) return 2; 
        if (mt_min < 120 && met < 200 && njets > 4) return 4; 
        if (mt_min < 120 && met >= 200 && njets <= 4) return 5+mm; 
        if (mt_min < 120 && met >= 200 && njets > 4) return 7; 
        if (mt_min >= 120 && met < 200 && njets <= 4) return 8+mm;
        return 10;
      } 
      if (nbtags == 1){
        if (mt_min < 120 && met < 200 && njets <= 4) return 12; 
        if (mt_min < 120 && met < 200 && njets > 4) return 15+mm; 
        if (mt_min < 120 && met >= 200 && njets <= 4) return 17+mm; 
        if (mt_min < 120 && met >= 200 && njets > 4) return 19; 
        if (mt_min >= 120 && met < 200 && njets <= 4) return 20+mm;
        return 22;
      } 
      if (nbtags == 2){
        if (mt_min < 120 && met < 200 && njets <= 4) return 24; 
        if (mt_min < 120 && met < 200 && njets > 4) return 27+mm; 
        if (mt_min < 120 && met >= 200 && njets <= 4) return 29+mm; 
        if (mt_min < 120 && met >= 200 && njets > 4) return 31; 
        if (mt_min >= 120 && met < 200 && njets <= 4) return 32+mm;
        return 34;
      } 
      if (nbtags >= 3){
        if (mt_min < 120 && met < 200 && njets<5) return 37+mm;
        if (mt_min < 120 && met < 200) return 52+mm;
        if (mt_min < 120 && met >= 200 && njets<5) return 39;
        if (mt_min < 120 && met >= 200) return 54;
        if (mt_min >= 120 &njets<5) return 41;
        if (mt_min >= 120) return 55;
      }
    }
  }
  
  //High-Low
  if (lep_pt == HighLow){
    if (met >= 300 && ht >= 300) {
        if(met < 500 && njets<5) return 34+mm;
        else if(met < 500) return 42+mm;
        else if(njets<5) return 36+mm;
        else return 44+mm;
    }
    if (ht >= 1125) {
        if(ht < 1300) return 38+mm;
        else return 40+mm;
    }
    if (ht < 300){ 
      if (nbtags == 0 && met < 200 && njets <= 4) return 1; 
      if (mt_min < 120 && nbtags == 0) return 3;
      if (mt_min < 120 && nbtags == 1 && met < 200 && njets <= 4) return 8; 
      if (mt_min < 120 && nbtags == 1) return 10+mm;
      if (mt_min < 120 && nbtags == 2 && met < 200 && njets <= 4) return 18; 
      if (mt_min < 120 && nbtags == 2) return 20+mm;
      if (mt_min < 120 && nbtags >= 3 && met < 200) return 27+mm; 
      if (mt_min < 120 && nbtags >= 3) return 27+mm;
      if (mt_min >= 120) return 32;
    }  
    if (ht >= 300){
      if (nbtags == 0 && mt_min < 120 && met < 200 && njets <= 4) return 2; 
      if (nbtags == 0 && mt_min < 120 && met < 200 && njets > 4) return 4; 
      if (nbtags == 0 && mt_min < 120 && met < 500 && njets <= 4) return 5+mm; 
      if (nbtags == 0 && mt_min < 120 && met < 500 && njets > 4) return 7; 
      if (nbtags == 1 && mt_min < 120 && met < 200 && njets <= 4) return 9; 
      if (nbtags == 1 && mt_min < 120 && met < 200 && njets > 4) return 12+mm; 
      if (nbtags == 1 && mt_min < 120 && met < 500 && njets <= 4) return 14+mm; 
      if (nbtags == 1 && mt_min < 120 && met < 500 && njets > 4) return 16+mm; 
      if (nbtags == 2 && mt_min < 120 && met < 200 && njets <= 4) return 19; 
      if (nbtags == 2 && mt_min < 120 && met < 200 && njets > 4) return 22+mm; 
      if (nbtags == 2 && mt_min < 120 && met < 500 && njets <= 4) return 24+mm; 
      if (nbtags == 2 && mt_min < 120 && met < 500 && njets > 4) return 26; 
      if (nbtags >= 3 && mt_min < 120 && met < 200) return 29+mm; 
      if (nbtags >= 3 && mt_min < 120 && met >= 200) return 31;
      if (mt_min >= 120) return 33;
    }
  }

  //Low-Low
  if (lep_pt == LowLow){
    if (ht < 300) return -1; 
    if (mt_min > 120) return 8; 
    if (nbtags == 0 && met < 200) return 1;
    if (nbtags == 0 && met >= 200) return 2;
    if (nbtags == 1 && met < 200) return 3;
    if (nbtags == 1 && met >= 200) return 4;
    if (nbtags == 2 && met < 200) return 5;
    if (nbtags == 2 && met >= 200) return 6;
    if (nbtags >= 3) return 7;
  }

  //Otherwise undefined
  cout << "WARNING: SR UNDEFINED (should never get here)" << endl;
  cout << "  --> lepton pts are: " << lep1pt << " " << lep2pt << endl;
  cout << "  --> ht & met are: " << ht << " " << met << endl;
  cout << "  --> njets & nbtags: " << njets << " " << nbtags << endl;
  return -1;
}
