#include <iostream>
#include <set>
#include <TString.h>
#include <TFile.h>
#include <TTree.h>

void removeDuplicates(TString filename, TString outfilename) {

    std::cout<<filename<<std::endl;

    //TFile *oldfile = new TFile(filename);
    TFile *oldfile = TFile::Open(filename);
    TTree *oldtree = (TTree*)oldfile->Get("Ana/passedEvents");
    if(!oldtree) oldtree = (TTree*)oldfile->Get("passedEvents");

    Long64_t nentries = oldtree->GetEntries();
    std::cout<<nentries<<" total entries."<<std::endl;
    ULong64_t Run, LumiSect, Event;
    bool passedZ4lSelection;
    oldtree->SetBranchAddress("Run",&Run);
    oldtree->SetBranchAddress("LumiSect",&LumiSect);
    oldtree->SetBranchAddress("Event",&Event);

    //Create a new file + a clone of old tree in new file
    TFile *newfile = new TFile(
            //filename.ReplaceAll(".root","_noDuplicates.root")
            outfilename
            ,"recreate");
    TTree *newtree = oldtree->CloneTree(0);

    std::set<TString> runlumieventSet;
    int nremoved = 0;
    for (Long64_t i=0;i<nentries; i++) {
        if (i%100000==0) std::cout<<i<<"/"<<nentries<<std::endl;
        oldtree->GetEntry(i);

        TString s_Run  = std::to_string(Run);
        TString s_Lumi = std::to_string(LumiSect);
        TString s_Event = std::to_string(Event);
        TString runlumievent = s_Run+":"+s_Lumi+":"+s_Event;
        
        if (runlumieventSet.find(runlumievent)==runlumieventSet.end()) {
            runlumieventSet.insert(runlumievent);
            newtree->Fill();
        } else {
            nremoved++;
        }
        //if (passedZ4lSelection) newtree->Fill();
    }

    std::cout<<nremoved<<" duplicates."<<std::endl;
    newtree->Print();
    newtree->AutoSave();
    //delete oldfile;
    delete newfile;
}

