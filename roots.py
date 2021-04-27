'''finding root solutions'''

from sympy.solvers import solve
from sympy import Symbol
import numpy as np
from sympy import Add
from sympy import Mul

k_range = range(0,21)
d_range = range(0,41)
s_range = range(0,11)
x = Symbol('x')

'''checking range for instanes of number of roots to estimate deliniations of root numbers'''

for k in k_range:
    solutions = np.zeros((len(d_range), len(s_range)))
    for d in d_range:
        for s in s_range:
            pts = solve((1-s/50-x)*d/10-(k/10)*x/((s/50)**2+x**2),x)
            for pt in range(len(pts)):
                re, im = pts[pt].as_real_imag()
                if im < 10**-10:
                    pts[pt] = re
            pts = [pt for pt in pts if not isinstance(pt,Add)]
            pts = [pt for pt in pts if not isinstance(pt,Mul)]
            solutions[d,s] = (int(len(pts)))
            print(k,d,s)
    hold_array = solutions.astype(int)
    np.savetxt("k_layer_small"+str(k)+".csv", hold_array, delimiter=",",fmt='%f')


#np.savetxt("foo1.csv", arrReshaped, delimiter=",")
print('Done')
