import math

def mtFunc(x1_pt,x1_phi,x2_pt,x2_phi):
    return math.sqrt(2*x1_pt*x2_pt*(1-math.cos(x1_phi-x2_phi)))
