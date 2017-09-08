import numpy as np
import matplotlib as mplot

P = np.matrix('0.5 0.3 0.2;0.4 0.3 0.3;0.6 0.3 0.1')
I = np.matrix('1 0 0;0 1 0;0 0 1')

n = 500

Pn = P**n
print("P")
print(P)

print("Pn")
print(Pn)
print("//////////////////////")
tp = P.transpose()
print(tp)

eigval,eigvecmat = np.linalg.eig(tp)

print("Mat of eigvec")
print(eigvecmat)
print("list+index")
print(eigval.tolist())
print(eigval.tolist().index(eigval.max()))

steadystate = eigvecmat[:,eigval.tolist().index(eigval.max())]
print("Steady state")
steadystate = (1/steadystate.sum())*steadystate
print(steadystate)
