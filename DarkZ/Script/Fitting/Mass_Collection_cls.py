class HistCollection:

    def __init__(self, fs):
#    def __init__(self, masslist, fs)
#        self.masslist = masslist
        self.fs = fs
        self.hist_title = ""
        self.mass_list = []
        self.hist_list = []
        self.const_list = []
        self.const_err_list = []
        self.mean_list = []
        self.mean_err_list = []
        self.sigma_list = []
        self.sigma_err_list = []
        self.rel_sigma_list = []
        self.rel_sigma_err_list = []

        if fs in "4e":
            self.X1_fs = "2e"
            self.X2_fs = "2e"
        elif fs in "4mu":
            self.X1_fs = "2mu"
            self.X2_fs = "2mu"
        elif fs in "2e2mu":
            self.X1_fs = "2e"
            self.X2_fs = "2mu"
        elif fs in "2mu2e":
            self.X1_fs = "2mu"
            self.X2_fs = "2e"
        else:
            raise RuntimeError("Warning: fs not recognized!")

    def calc_x_binwidth(self):
        pass
#        x_binwidth_list = 
#        return x_binwidth_list
