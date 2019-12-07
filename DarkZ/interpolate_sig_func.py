import ROOT,array

def makePlot(x_points,y_points,err_points):
    if len(x_points) != len(y_points) or len(x_points) != len(err_points) or len(err_points) != len(y_points): raise RuntimeError
    n = len(x_points)
    gr = ROOT.TGraphErrors(n,array.array('d',x_points),array.array('d',y_points),array.array('d',[0.]*n),array.array('d',err_points))
    return gr

class SignalModel(object):
    def __init__(self,
            sig_name,
            centre,
            yieldFactor=1.,
            ):
        self.sig_name = sig_name
        self.centre = centre
        self.yieldFactor = yieldFactor
