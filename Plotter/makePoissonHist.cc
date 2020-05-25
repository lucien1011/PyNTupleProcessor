#include "Math/QuantFuncMathCore.h"
#include "TMath.h"

#include "TGraphAsymmErrors.h"

TGraphAsymmErrors* makePoissonHist(TH1* h1,bool skip_zero){
    const double alpha = 1 - 0.6827;
    TGraphAsymmErrors * g = new TGraphAsymmErrors(h1);  
    for (int i = 0; i < g->GetN(); ++i) {
        int N = g->GetY()[i];
        double L =  (N==0) ? 0  : (ROOT::Math::gamma_quantile(alpha/2,N,1.));
        double U =  ROOT::Math::gamma_quantile_c(alpha/2,N+1,1) ;
        if (!skip_zero||(g->GetPointY(i) != 0.)) {
            g->SetPointEYlow(i, N-L);
            g->SetPointEYhigh(i, U-N);
        } else {
            g->SetPointEYlow(i, 0.);
            g->SetPointEYhigh(i, 0.);
        };
    };
    return g;
}
