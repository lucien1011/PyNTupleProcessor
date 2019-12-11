# Functions for fitting TH1 with Gaussian TF1. 

from ROOT import (TFile,TTree,TH1D,TCanvas,TGraphErrors,TF1,
                  gROOT,kTRUE,gStyle,TH1Editor,TF1Convolution)

import numpy as np
                  
def fit_hist_with_gaus(hist, n_stdev_list, draw=False, fit_around_mean=False):
    """
    fit_hist_with_gaus(hist, n_stdev_list, draw=False, fit_around_mean=False)
    
    Fits a single histogram (hist) with various gaus fits, over different sigma ranges.
        Fit range: mu +- N*sigma
            mu = mean of hist
            sigma = stdev of hist
            N = number of sigmas, taken from n_stdev_list        
            
    # Perform gaus fits over the range: hist_mean +- N*hist_sigma,
    # where X is some number of hist_sigmas. 
    Fit can be done centered at the mean (fit_around_mean=True) or around the peak 
    of the histogram (fit_around_mean=False).
    
    Returns:
            hist_list, fit_list, canvas_list
    """
    hist_list = []
    fit_list = []
    canvas_list = []
 
    for nstdev in n_stdev_list:
        canvas_list.append(TCanvas())
        hist_list.append(hist.Clone())
        h_tmp = hist_list[-1]
        h_tmp.mean = h_tmp.GetMean()
        h_tmp.stdev = h_tmp.GetStdDev()
        
        bin_at_max = h_tmp.GetMaximumBin()
        h_tmp.most_prob_val = h_tmp.GetXaxis().GetBinCenter(bin_at_max)

        if (fit_around_mean):
            center = h_tmp.mean
            center_str = "mean"
#             print "Fitting is centered on the MEAN."
        else:
            # Fit around the peak instead.
            center = h_tmp.most_prob_val
            center_str = "most_prob_val"
#             print "Fitting is centered on the MOST PROBABLE VALUE (peak)."
        fit_x_min = center - nstdev*h_tmp.stdev
        fit_x_max = center + nstdev*h_tmp.stdev
        fit_list.append( TF1("fit1","gaus",fit_x_min,fit_x_max) )
        fit_tmp = fit_list[-1]

        # Get parameters.
        h_tmp.params = h_tmp.Fit(fit_tmp,"SRQ")  # S=store_result, R=ranged_fit, Q=quiet 
        h_tmp.fit_mean = h_tmp.params.Parameter(1)
        h_tmp.fit_sigma = h_tmp.params.Parameter(2)
        h_tmp.chi2 = fit_tmp.GetChisquare()  # This returns TOTAL chi^2, not reduced!
        h_tmp.n_dof = fit_tmp.GetNDF()
        try:
            h_tmp.reduced_chi2 = h_tmp.chi2/float(h_tmp.n_dof)
        except:
            h_tmp.reduced_chi2 = np.inf
        h_tmp.n_sigmas = nstdev
            
        if (draw):
            gStyle.SetOptFit(1111)
            gStyle.SetStatX(0.8)
            gStyle.SetStatY(0)
            h_tmp.SetXTitle("m_{X} [GeV]")
            h_tmp.SetYTitle( "Events / [%.3f GeV]" % h_tmp.GetBinWidth(1) )  # Not underflow bin.

            extra_title = "Fit range: [%s #pm %.2f*sigma]" % (center_str,nstdev)
            if h_tmp.GetName() in ["mZ2_4e","mZ2_2mu2e"]:
                h_tmp.SetTitle("X #rightarrow e^{-}e^{+}, " + extra_title)
            else:
                h_tmp.SetTitle("X #rightarrow #mu^{-}#mu^{+}, " + extra_title)

            h_tmp.Draw('hist e1')
            fit_tmp.Draw("same")
            canvas_list[-1].Update()
            canvas_list[-1].Draw()
            
    return hist_list, fit_list, canvas_list

def print_hist_fit_info(hist_list):
        
    print "fit_mean\tfit_sigma\tchi^2/n_dof\tn_dof\t+-N*hist_sigmas"
    
    for h in hist_list:
        mean = h.fit_mean
        sigma = h.fit_sigma
        red_chi2 = h.reduced_chi2
        n_dof = h.n_dof
        n_sigmas = h.n_sigmas

#         print "Fit Parameters:"
        print "%.4f\t\t%.4f\t\t%.4f\t\t%d\t%.2f" % (mean,sigma,red_chi2,n_dof,n_sigmas)


def rank_hist_fit(hist_list, skip_ndof_eq_0=False):
    """
    Print the 
    Arguments:
        hist_list = histograms that have been fitted.
    n_rank = number of best-fits to show.
        e.g. if n_rank = 5, then the top 5 best-fit histogram data will be displayed.
        
    "Best" is defined as the hist with the lowest chi^2.
    """
    pass
        # Find best fit. 
#     chi2_list = [hist.reduced_chi2 for hist in hist_list]
#     best_chi2 = min(chi2_list)
#     best_index = chi2_list.index(best_chi2)  # Find which histo had best fit. 
    
#     best_hist = hist_list[best_index]
#     best_mean = best_hist.params.Parameter(1)
#     best_sigma = best_hist.params.Parameter(2)
#     best_fit_range = sigma_list[best_index]
#     best_n_dof = best_hist.n_dof  # Not necessarily the "best" n_dof, but they belong to the "best" hist.

#     print "Best chi^2:\t%.3E" % best_chi2
#     print "Best mean:\t%.2f" % best_mean
#     print "Best sigma:\t%.4f" % best_sigma
#     print "Best fit range:\t+-%.3f sigma" % best_fit_range
#     print "n_dof:\t", best_hist.n_dof
    
#     return hist_list, fit_list, chi2_list, best_index
    
#     if n_rank > len(hist_list): 
#         warning = "You must specify a number of "
#         raise RuntimeError(warning)

#     sorted_hist_list
#     for hist in sorted_hist_list:
#         print_hist_fit_info(hist)
#     if hist.n_dof == 0: continue
#     dict_rank = {}
#     for h in range(1,n_rank+1):
#         printdef fit_hist_with_gaus(hist, n_stdev_list, draw=False, fit_around_mean=False):
