from decimal import *
from math import *
import numpy as np
idx=390
with localcontext() as ctx:
    ctx.prec = 32  # desired precision
    p = ctx.power(3, idx)
    depart = exp(-3) * p 
    depart /= factorial(idx)
    print depart
