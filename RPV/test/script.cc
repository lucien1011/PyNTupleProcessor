void script()
             { TFile *f1 = TFile::Open("1000.root");
               TH1F *met_1 = (TH1F*)f1->Get("met");
 	       met_1->Sumw2(); met_1->Scale(1.0/met_1->Integral()); met_1->SetLineColor(kBlue); met_1->SetTitle("met");
 	       met_1->Draw("met");
               TFile *f2 = TFile::Open("1800.root"); 
  	       TH1F *met_2 = (TH1F*)f2->Get("met");
	       met_2->Sumw2(); met_2->Scale(1.0/met_2->Integral()); met_2->SetLineColor(kRed);
	       met_2->Draw("same");
	       TFile *f3 = TFile::Open("2000.root");
	       TH1F *met_3 = (TH1F*)f3->Get("met");
	       met_3->Sumw2(); met_3->Scale(1.0/met_3->Integral()); met_3->SetLineColor(kGreen);
	       met_3->Draw("same"); 






               /*TH1F *nBJet25_1 = (TH1F*)f1->Get("nBJet25");
               nBJet25_1->Sumw2(); nBJet25_1->Scale(1/nBJet25_1->Integral()); nBJet25_1->SetLineColor(kBlue); nBJet25_1->SetTitle("nBJet25");
               nBJet25_1->Draw("nBJet25");
               TH1F *nBJet25_2 = (TH1F*)f2->Get("nBJet25");
               nBJet25_2->Sumw2(); nBJet25_2->Scale(1/nBJet25_2->Integral()); nBJet25_2->SetLineColor(kRed);
               nBJet25_2->Draw("same");
               TH1F *nBJet25_3 = (TH1F*)f3->Get("nBJet25");
               nBJet25_3->Sumw2(); nBJet25_3->Scale(1/nBJet25_3->Integral()); nBJet25_3->SetLineColor(kGreen);
               nBJet25_3->Draw("same");*/

}
	       //TF1 *func1 = (TF1*)c2->GetPrimitive("fun1"); 
	       //TF1 *func2 = (TF1*)c3->GetPrimitive("fun2"); c1->cd(); func1->Draw("same"); func2->Draw("same"); }                                                                                                                       
