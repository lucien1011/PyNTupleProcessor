from ROOT import TFile,TTree,TH1D,TCanvas,TGraphErrors,TF1,TLegend,gROOT,kTRUE,gStyle,gPad,TH1Editor,TF1Convolution
import os, sys, shutil
import numpy as np
import numpy

from DarkZ.Script.Fitting.Functions_Navigation import make_dir_copy_file
from DarkZ.Script.Fitting.Fns_Math import lorentzian

class MyHist:
    def __init__(self,fs,mass,year):
        self.fs = fs
        self.mass = mass
        self.year = year
        
        self.best_fit_sigma = -1
        self.best_fit_sigma_err = -1
        self.best_fit_rel_sigma = -1
        self.best_fit_rel_sigma_err = -1
        
        # self.bin_width = 0
        self.hist = None
        
        self.hist_fit_list = []
        self.fit_list = []
        self.canvas_list = []
        
        self.fit_const_list = []
        self.fit_const_err_list = []
        self.fit_mean_list = []
        self.fit_mean_err_list = []
        self.fit_sigma_list = []
        self.fit_sigma_err_list = []
        self.fit_rel_sigma_list = []
        self.fit_rel_sigma_err_list = []
        
        self.n_stdev_list = []
        self.red_chi2_list = []
        self.n_dof_list = []
        
        
    def fit_with_gaus(self, n_stdev_list, draw=False, fit_around_center="mpv", combine_bins=1):
        """
        FIXME
        fit_with_gaus(self, n_stdev_list, draw=False, fit_around_mean=False)

        Fits a single histogram (self.hist) with various gaus fits, over different sigma ranges.
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
        hist_list_tmp = []
        fit_list = []
        canvas_list = []
        n_dof_list = []

        for nstdev in n_stdev_list:

            canvas_list.append(TCanvas())
            hist_list_tmp.append( self.hist.Clone() )
            h_tmp = hist_list_tmp[-1]
            h_tmp.mass = self.mass
            # print "self.mass is:",self.mass
            # print "h_tmp.mass is:",h_tmp.mass
            # if rebin > 1: 
            #     h_tmp.Rebin(rebin)
            self.bin_width = h_tmp.GetBinWidth(1)  # Select bin next to underflow bin, for safety.
            h_tmp.bin_width = self.bin_width
            h_tmp.n_sigmas = nstdev
            h_tmp.mean = h_tmp.GetMean()
            h_tmp.stdev = h_tmp.GetStdDev()

            h_tmp.bin_at_max = h_tmp.GetMaximumBin()
            h_tmp.most_prob_val = h_tmp.GetXaxis().GetBinCenter(h_tmp.bin_at_max)

            if fit_around_center in "mean":
                center = h_tmp.mean
                center_str = "mean"
                print "Fitting around mean."
            elif fit_around_center in "mpv":
                # Fit around the peak instead.
                center = h_tmp.most_prob_val
                center_str = "most_prob_val"
                print "Fitting around mean."
            # else: 
            #     raise SyntaxError("Warning: fit_around_center string not understood.")
                
            fit_x_min = center - nstdev*h_tmp.stdev
            fit_x_max = center + nstdev*h_tmp.stdev
            fit_list.append( TF1("fit1","gaus",fit_x_min,fit_x_max) )
            fit_tmp = fit_list[-1]

            # Do the fit.
            h_tmp.params = h_tmp.Fit(fit_tmp,"SRQ")  # S=store_result, R=ranged_fit, Q=quiet 
            
            # Get parameters.
            params = h_tmp.params
            
            h_tmp.fit_const = params.Parameter(0) 
            h_tmp.fit_const_err = params.ParError(0)
            h_tmp.fit_mean = params.Parameter(1)
            h_tmp.fit_mean_err = params.ParError(1)
            h_tmp.fit_sigma = params.Parameter(2)
            h_tmp.fit_sigma_err = params.ParError(2)            
            h_tmp.chi2 = fit_tmp.GetChisquare()  # This returns TOTAL chi^2, not reduced!
            h_tmp.n_dof = fit_tmp.GetNDF()
            
            # Since I'm storing each h_tmp in a hist_fit_list, 
            # I probably don't need these lists below.
            # FIXME: which values do I want to save? 
            #     - the main histogram (self)?
            #     - the h_tmp, of which there will be many? <-- probably this one?
            #     - lists of all the individual variables (listed below)
            self.fit_const_list.append( h_tmp.fit_const )
            self.fit_const_err_list.append( h_tmp.fit_const_err )
            self.fit_mean_list.append( h_tmp.fit_mean )
            self.fit_mean_err_list.append( h_tmp.fit_mean_err ) 
            self.fit_sigma_list.append( h_tmp.fit_sigma )
            self.fit_sigma_err_list.append( h_tmp.fit_sigma_err )
            self.fit_rel_sigma_list.append( h_tmp.fit_sigma/float(h_tmp.mass) )
            self.fit_rel_sigma_err_list.append( h_tmp.fit_sigma_err/float(h_tmp.mass) )
            self.n_dof_list.append( h_tmp.n_dof )
            
            try:
                h_tmp.reduced_chi2 = h_tmp.chi2/float(h_tmp.n_dof)
            except ZeroDivisionError:
                h_tmp.reduced_chi2 = np.inf
            self.red_chi2_list.append( h_tmp.reduced_chi2 )
            
            if not (draw):
                gROOT.SetBatch(kTRUE)  # Prevent ROOT from drawing plots to screen.
            gStyle.SetOptFit(1111)
#             gStyle.SetStatX(-0.1)
#             gStyle.SetStatY
            h_tmp.SetXTitle("m_{X} [GeV]")
            h_tmp.SetYTitle( "Events / [%.3f GeV]" % h_tmp.bin_width )

            extra_title = "Fit range: [%s #pm %.2f*sigma]" % (center_str,nstdev)
            if h_tmp.GetName() in ["mZ2_4e","mZ2_2mu2e"]:
                h_tmp.SetTitle("X #rightarrow e^{-}e^{+}, " + extra_title)
            else:
                h_tmp.SetTitle("X #rightarrow #mu^{-}#mu^{+}, " + extra_title)

            h_tmp.Draw('hist e1')
            fit_tmp.Draw("same")
            canvas_list[-1].Update()
            canvas_list[-1].Draw()
            # Done with this one fit.
                
        # Save all info in object.
        self.hist_fit_list = hist_list_tmp
        self.fit_list = fit_list
        self.canvas_list = canvas_list
        self.n_stdev_list = n_stdev_list
        
        # return hist_list_tmp, fit_list, canvas_list, n_stdev_list
    
    
    def save_plots(self, fullpath_phpfile, outpath, save_plots=False):
        """
        save_plots(self, fullpath_phpfile, outpath, save_plots=False)
        
        Save the drawn canvases to some directory path (outpath).
        
        Parameters
        ----------
        fullpath_phpfile : str
            Path to an index.php that will be copied to outpath.
        outpath : str
            Path to store drawn canvases, usually tier2.ihepa.ufl.edu/~...
        save_plots : bool, optional
            Save drawn plots to outpath.
     
        Returns
        -------
        Nothing; just save the canvases.
        """
        if (save_plots): 
            stdev_ls = self.n_stdev_list
            canv_ls = self.canvas_list

            # Make sure dir to store plots exists.
            year_ = str(self.year)
            fs_ = str(self.fs)
            mass_ = str(self.mass)
            newdir = "%s/%s/%sGeV/" % (year_,fs_,mass_)  # Trailing underscore used to avoid naming conflicts.
            fullpath_newdir = os.path.join(outpath,newdir)
            make_dir_copy_file(fullpath_phpfile,fullpath_newdir)

            for count,stdev in enumerate(stdev_ls):
                plot_name = newdir.replace("/","_") + str(stdev).replace(".","p") + "sigmas"
                canv_ls[count].SaveAs(fullpath_newdir + plot_name + ".png")
                canv_ls[count].SaveAs(fullpath_newdir + plot_name + ".pdf")
        else:
            print "You specified that the fit plots should not be saved."
    
    
    def print_fit_info(self, print_info=False):
        """print_fit_info(self, print_info=False)"""
        
        if (print_info):
            # print "bin width: %.2f" % self.bin_width
            print "fit_mean\tfit_sigma\tchi^2/n_dof\tn_dof\t+-N*hist_sigmas"

            for h in self.hist_fit_list:
                mean = h.fit_mean
                sigma = h.fit_sigma
                red_chi2 = h.reduced_chi2
                n_dof = h.n_dof
                n_sigmas = h.n_sigmas
                # bin_width = h.bin_width

        #         print "Fit Parameters:"
                print "%.4f\t\t%.4f\t\t%.4f\t\t%d\t%.2f" % (mean,sigma,red_chi2,n_dof,n_sigmas)
     
    
    def get_best_fit_sigma(self,verbose=False):
        """
        
        Store the sigma value, as the average of all sigmas, weighted by their chi^2.
        The chi^2 values are weighted using a Lorentzian function peaked at 1.
        
        Parameters
        ----------
        """
        print "Is this thing on?"
        red_chi2_list = self.red_chi2_list
        sigma_list = self.fit_sigma_list

        # Normalize the reduced chi^2 values based on how close they are to 1.
        norm_weights = lorentzian(red_chi2_list,1,0.05)
        best_calc_sigma = np.average(sigma_list,weights=norm_weights)
        
        # Use the calculated sigma above to find which actual best_fit_sigma value was closest.
        best_sig = min(self.fit_sigma_list, key = lambda x: abs(x-best_calc_sigma))
        
        # Find the corresponding best values.
        best_sig_index = self.fit_sigma_list.index(best_sig)
        best_sig_err = self.fit_sigma_err_list[best_sig_index]
        best_r_chi2 = self.red_chi2_list[best_sig_index]
        best_n_stdev = self.n_stdev_list[best_sig_index]
        
        best_rel_sig = best_sig/float(self.mass)
        best_rel_sig_err = best_sig_err/float(self.mass)
        
        # Save values.
        self.best_fit_sigma = best_sig
        self.best_fit_sigma_err = best_sig_err
        self.best_fit_rel_sigma = best_rel_sig
        self.best_fit_rel_sigma_err = best_rel_sig_err
        self.best_red_chi2 = best_r_chi2
        self.best_n_stdev = best_n_stdev
        
        if (verbose):
            print "Best chi^2 found:\t\t\t",best_r_chi2
            print "Best calculated sigma:\t\t\t",best_calc_sigma
            print "Best fit sigma matched:\t\t\t",best_sig
            print "Best fit sigma_err found:\t\t",best_sig_err
            print "Best fit sigma index is:\t\t",best_sig_index
            print "Best fit rel_sigma of:\t\t\t",best_rel_sig
            print "Best fit rel_sigma_err of:\t\t",best_rel_sig_err,"\n"

       
    # chi2_list = [hist.reduced_chi2 for hist in hist_list]
    # best_chi2 = min(chi2_list)
    # best_index = chi2_list.index(best_chi2)