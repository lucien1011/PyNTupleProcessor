import numpy

def lorentzian(x,shift,gamma):
    """
    lorentzian(x,shift,gamma)
    
    Returns the value of the Lorentzian function (Cauchy, Breit-Wigner).
    
    Parameters
    ----------
    x : float
        The x value to plug into the Lorentzian.
        
    shift : float
            The value on x axis where center of curve will be.
            
    gamma : The width? Sorta?
    """
    x = numpy.array(x,dtype=float)
    shift = float(shift)
    gamma = float(gamma)
    denom = (x-shift)**2 + gamma**2
    return 1/numpy.pi*(gamma/denom)