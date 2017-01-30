import numpy as np
from numpy import linalg as LA
import seistools.rough
import matplotlib.pyplot as plt

x = np.loadtxt("x.out")
y= 16.*np.ones(1601)
#x= x* 0.
#y = np.loadtxt("y.out")
#x= np.zeros(1601)
plt.plot(x,y)
plt.show()


vector_array= np.zeros((len(x), 2))
vector_array[:,0]= x
vector_array[:,1]=y

normalized_vector= np.zeros((len(x), 2))
normal_vector= np.zeros((len(x), 2))
normal_stress= np.zeros((len(x)))
shear_stress= np.zeros((len(x)))

norm= ( (vector_array[:,0] **2 + vector_array[:,1] ** 2 )  ) ** (0.5)
#print(norm)

normalized_vector[:, 0]= vector_array[:, 0] / norm[:]
normalized_vector[:, 1]= vector_array[:, 1] / norm[:]
print(normalized_vector)

for i in range(len(x)):
#normal_vector[i,:]=seistools.coulomb.tangent_2d(normalized_vector[i,:])

 #stresses[i] =seistools.coulomb.rotate_xy2nt_2d(-100, 72.5, -120, normal_vector_array[i])
 normal_stress[i], shear_stress[i]= seistools.coulomb.rotate_xy2nt_2d(-100, 72.5, -120, normalized_vector[i,:])

#plt.plot (normal_stress)

#plt.plot(normal_stress)
#plt.show()
