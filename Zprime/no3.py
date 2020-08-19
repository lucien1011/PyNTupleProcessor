import numpy as np

n = 997799
maxfac = 0
div = 2
while n != 0:
    if n % div != 0:
        div = div + 1
    else:
        maxfac = n
        n = n / div
        if n == 1:
            print maxfac
            break

