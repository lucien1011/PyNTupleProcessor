#include <TString.h>
#include <stdio.h>
#include <iostream>

using namespace std;
 
const TString LowLow = "LL";
const TString HighLow = "HL";
const TString HighHigh = "HH";

TString leptonCategory(int id1, int id2, float lep1pt, float lep2pt) {
  if ((lep1pt > 25.) && (lep2pt > 25.)) return "HH";
  if ((lep1pt > 25.) && (lep2pt > 10.) && (lep2pt < 25.)) return "HL";
  if ((lep1pt > 10.) && (lep1pt < 25.) && (lep2pt > 10.) && (lep2pt < 25.)) return "LL";
  return "";
};

int rpv_binning_v1(int njets, int nbtags, float met, float ht, float mt_min, int id1, int id2) {
    if (ht >= 1125) {
        if(ht < 1300) return 23;
        else if(ht < 1600) return 24;
        else return 25;
    } else if (ht >= 300 && ht < 1125) {
        if (nbtags==0) {
            if ((njets<=4) && (mt_min<120)) return 9;
            if ((njets>4) && (mt_min<120)) return 10;
            if ((njets<=4) && (mt_min>120)) return 11;
            if ((njets>4) && (mt_min>120)) return 12;
        } else if (nbtags==1) {
            if ((njets<=4) && (mt_min<120)) return 13;
            if ((njets>4) && (mt_min<120)) return 14;
            if ((njets<=4) && (mt_min>120)) return 15;
            if ((njets>4) && (mt_min>120)) return 16;
        } else if (nbtags==2) {
            if ((njets<=4) && (mt_min<120)) return 17;
            if ((njets>4) && (mt_min<120)) return 18;
            if ((njets<=4) && (mt_min>120)) return 19;
            if ((njets>4) && (mt_min>120)) return 20;
        } else if (nbtags>=3) {
            if (mt_min<120) return 21;
            return 22;
        };
    } else if (ht < 300) {
        if (nbtags==0) {
            if ((njets<=4) && (mt_min<120)) return 1;
            return 2;
        } else if (nbtags==1) {
            if ((njets<=4) && (mt_min<120)) return 3;
            return 4;
        } else if (nbtags==2) {
            if ((njets<=4) && (mt_min<120)) return 5;
            return 6;
        } else if (nbtags>=3) {
            if (mt_min<120) return 7;
            return 8;
        };
    };
    return -1;
}


int rpvSignalRegionChargeSplit(int njets, int nbtags, float met, float ht, float mt_min, int id1, int id2, float lep1pt, float lep2pt, TString lepCat){
    int base=52; // total number of baseline SR in HH
    if (lepCat == HighHigh){
        int rpv_sr = rpv_binning_v1(njets,nbtags,met,ht,mt_min,id1,id2);
        if (rpv_sr != -1){
            return base+rpv_sr;
        } else {
            return -1;
        };
    } else {
        return -1;
    };
}
    
int signalRegionChargeSplit(int njets, int nbtags, float met, float ht, float mt_min, int id1, int id2, float lep1pt, float lep2pt){

  //Calculate lep_pt
  TString lep_pt = leptonCategory(id1, id2, lep1pt, lep2pt); 

  // remember that sgn(pdgid) != sgn(charge), it's flipped. so mad.
  int mm = (id1 > 0);

  //Reject events out of kinematic acceptance
  if (njets < 2) return -1; 
  if (lep_pt != LowLow && met > 500 && ht < 300) return -1; 
  if (lep_pt != LowLow && njets>=2 && met>300 && ht<300) return -1;

  //High-high
  if (met < 50.) {
    return rpvSignalRegionChargeSplit(njets,nbtags,met,ht,mt_min,id1,id2,lep1pt,lep2pt,lep_pt);
  } else {
    if (lep_pt == HighHigh){
      if (met >= 300 && ht >= 300) {
          if(met < 500) return 42+mm;
          else return 44+mm;
      }
      if (ht >= 1125) {
          if(ht < 1300) return 46+mm;
          else if(ht < 1600) return 48+mm;
          else return 50+mm;
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
          if (mt_min < 120 && met < 200) return 37+mm;
          if (mt_min < 120 && met >= 200) return 39;
          if (mt_min >= 120) return 41;
        }
      }
    }
    
    //High-Low
    if (lep_pt == HighLow){
      if (met >= 300 && ht >= 300) {
          if(met < 500) return 34+mm;
          else return 36+mm;
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
  };

  //Otherwise undefined
  std::cout << "WARNING: SR UNDEFINED (should never get here)" << std::endl;
  std::cout << "  --> lepton pts are: " << lep1pt << " " << lep2pt << std::endl;
  std::cout << "  --> ht & met are: " << ht << " " << met << std::endl;
  std::cout << "  --> njets & nbtags: " << njets << " " << nbtags << std::endl;
  return -1;
};
