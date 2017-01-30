import numpy as np
import matplotlib.pyplot as plt

nx= 601
nz=211

input_data = np.loadtxt("tpv35_input_data.txt")
friction_coeff= input_data[:,4]
shear_stress= input_data[:, 5]
data_nx= 401
data_ny= int( len(friction_coeff)/ data_nx )
print(data_ny)
x = np.linspace(-30., 10., data_nx)
y=np.linspace(0,15.5,data_ny)
friction_value=np.reshape(friction_coeff, (data_nx,data_ny) ) # reshaping data to make it in the usable format
shear_stress_value= np.reshape(shear_stress, (data_nx,data_ny) ) # reshaping data to make it in the usable format

plt.pcolor(y,x, friction_value)
plt.show()
plt.colorbar()
friction_value= friction_value[:,::-1]           # flipping the values because the code goes from max. depth to min
shear_stress_value=shear_stress_value[:,::-1]


x = np.linspace(-30., 30., nx)
y = np.linspace(210, 0, nz ) # inorder to make it similar to the input file, i used 210 which is 21km
sigman = -60.*np.ones((nx,nz))
tauh = np.zeros((nx,nz))
tauv = np.zeros((nx,nz))
# Setting the interface frictional law parameters now
dc = 0.15*np.ones((nx,nz))
mus = np.zeros((nx,nz))
mud = 0.3*np.ones((nx,nz))
trup = np.zeros((nx,nz))
tc= np.zeros((nx,nz))
c0= np.zeros((nx,nz))


starting_index_x =np.where(x == -30.)   # we just need to find the first index since spatial resolution is same both in file and in code.
starting_index_y= np.where(y == 155)
print ('from here it will start',starting_index_y[0][0])

for i in range(data_nx):
 for j in range(data_ny):  
  tauh[i][starting_index_y[0][0]+j]= shear_stress_value[i][j]  # 'i' needs to be  tau [i +starting_index_x] [j+starting_index_y[0][0]] but since my x starts at -30 so I donot need it.
  mus[i][starting_index_y[0][0]+j]= friction_value[i][j]  

print(tauh.shape)
print(x.shape)
print(y.shape)

# plt.pcolor(y,x,mus)
# plt.axis([0, 155, -30, 10])
# plt.colorbar()
# plt.show()

