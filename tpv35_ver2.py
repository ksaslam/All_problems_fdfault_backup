import fdfault
import numpy as np
import matplotlib.pyplot as plt
# create problem

p = fdfault.problem('tpv35')

# set rk and fd order

p.set_rkorder(4)
p.set_sbporder(4)

# set time step info

refine =  1


nt = 4192

p.set_nt(nt)
p.set_dt(0.004294)
p.set_ninfo(500)

p.set_ndim(3)

# set number of blocks and coordinate information
nx = 600*refine+1
ny = 120*refine+1
nz = 250*refine+1

p.set_nblocks((1,2,1))
p.set_nx_block(([nx], [ny, ny], [nz]))

# set block dimensions
p.set_block_lx((0,0,0),(60.,12., 25.))
p.set_block_lx((0,1,0),(60.,12., 25.))

# minimum values of the domain
p.set_domain_xm((-30., -12.0, -25.0))

# set block boundary conditions

p.set_bounds((0,0,0),['absorbing', 'absorbing', 'absorbing', 'none', 'absorbing', 'free'])
p.set_bounds((0,1,0),['absorbing', 'absorbing', 'none', 'absorbing', 'absorbing', 'free'])

# set material
cs = np.empty((nx, 2*ny, nz))
cp = np.empty((nx, 2*ny, nz))
rho = np.empty((nx, 2*ny, nz))

# starting with the velocity model of the first side(-y), we have 9 layers on this side
for k in range(nz):
    # layer 1
    if k >= 0 and k <10: 
     cp[:,0:ny,k] = 2. 
     cs[:,0:ny,k] = 1.1
     rho[:,0:ny,k] = 2.  
     # layer 2
    if k >= 10 and k <20: 
     cp[:,0:ny,k] = 3.5 
     cs[:,0:ny,k] = 2.
     rho[:,0:ny,k] = 2.3
     # layer 3
    if k >= 20 and k <30: 
     cp[:,0:ny,k] = 4.5 
     cs[:,0:ny,k] = 2.5
     rho[:,0:ny,k] = 2.3
     # layer 4
    if k >= 30 and k <35: 
     cp[:,0:ny,k] = 5.2 
     cs[:,0:ny,k] = 3.0
     rho[:,0:ny,k] = 2.5
     # layer 5
    if k >= 35 and k <58: 
     cp[:,0:ny,k] = 5.7 
     cs[:,0:ny,k] = 3.2
     rho[:,0:ny,k] = 2.7 
     # layer 6
    if k >= 58 and k <141: 
     cp[:,0:ny,k] = 6.2 
     cs[:,0:ny,k] = 3.6
     rho[:,0:ny,k] = 2.7
     # layer 7 
    if k >= 141 and k <171: 
     cp[:,0:ny,k] = 6.8 
     cs[:,0:ny,k] = 3.6
     rho[:,0:ny,k] = 2.8
     # layer 8
    if k >= 171 and k <204: 
     cp[:,0:ny,k] = 6.8 
     cs[:,0:ny,k] = 4.3
     rho[:,0:ny,k] = 2.8  
     # layer 9
    if k >= 204 and k <=250: 
     cp[:,0:ny,k] = 7.3 
     cs[:,0:ny,k] = 4.3
     rho[:,0:ny,k] = 2.8                                      
     
# setting the velocity model of the second side  (+y) , we have around 9 layers on this side

for k in range(nz):
    # layer 1
    if k >= 0 and k <10: 
     cp[:,ny:2*ny,k] = 2. 
     cs[:,ny:2*ny,k] = 1.1
     rho[:,ny:2*ny,k] = 2.
    # layer 2
    if k >= 10 and k <18: 
     cp[:,ny:2*ny,k] = 3.5 
     cs[:,ny:2*ny,k] = 2.2
     rho[:,ny:2*ny,k] = 2.3
    # layer 3
    if k >= 18 and k <21: 
     cp[:,ny:2*ny,k] = 4.2 
     cs[:,ny:2*ny,k] = 2.8
     rho[:,ny:2*ny,k] = 2.3
    # layer 4
    if k >= 21 and k <34: 
     cp[:,ny:2*ny,k] = 4.8 
     cs[:,ny:2*ny,k] = 2.7
     rho[:,ny:2*ny,k] = 2.3
    # layer 5
    if k >= 34 and k <39: 
     cp[:,ny:2*ny,k] = 5.2 
     cs[:,ny:2*ny,k] = 2.8
     rho[:,ny:2*ny,k] = 2.3
    # layer 6
    if k >= 34 and k <83: 
     cp[:,ny:2*ny,k] = 5.3 
     cs[:,ny:2*ny,k] = 3.2
     rho[:,ny:2*ny,k] = 2.7
    # layer 7
    if k >= 83 and k <127: 
     cp[:,ny:2*ny,k] = 5.7 
     cs[:,ny:2*ny,k] = 3.7
     rho[:,ny:2*ny,k] = 2.8
    # layer 8
    if k >= 127 and k <175: 
     cp[:,ny:2*ny,k] = 6.5 
     cs[:,ny:2*ny,k] = 3.8
     rho[:,ny:2*ny,k] = 2.8
    # layer 9
    if k >= 175 and k <203: 
     cp[:,ny:2*ny,k] = 6.7 
     cs[:,ny:2*ny,k] = 4.3
     rho[:,ny:2*ny,k] = 2.8
    # layer 10
    if k >= 203 and k <=250: 
     cp[:,ny:2*ny,k] = 7.3 
     cs[:,ny:2*ny,k] = 4.3
     rho[:,ny:2*ny,k] = 2.8     



mat = np.zeros((3, nx, 2*ny, nz))
mat[0,:,:,:] = rho
mat[1,:,:,:] = rho*(cp**2-2.*cs**2)
mat[2,:,:,:] = rho*cs**2
mat = mat[:,:,:,::-1]

p.set_het_material(mat)

# set interface type

p.set_iftype(0,'slipweak')

# *************************************************
# need to remove this block
# set slip weakening parameters

# p.add_pert(fdfault.swparam('constant',0., 0., 0., 0., 0., 0.18, 0.58, 0.45),0)
# p.add_pert(fdfault.swparam('boxcar',0., 0., 24., -24., 9., 0., 10000., 0., 10.),0)
# p.add_pert(fdfault.swparam('boxcar',0., -24., 9., -7.5, 7.5, 0., 10000., 0., 10.),0)
# p.add_pert(fdfault.swparam('boxcar',0., 24., 9., -7.5, 7.5, 0., 10000., 0., 10.),0)

# *****************************************************




# loading the input data file. Then reshaping it to make it workable to  code.

input_data = np.loadtxt("tpv35_input_data.txt")
friction_coeff= input_data[:,4]
shear_stress= input_data[:, 5]
data_nx= 401
data_ny= int( len(friction_coeff)/ data_nx ) 
friction_value=np.reshape(friction_coeff, (data_ny, data_nx)) # reshaping data to make it in the usable format
shear_stress_value= np.reshape(shear_stress, (data_ny, data_nx)) # reshaping data to make it in the usable format
friction_value= friction_value[::-1, :]           # flipping the values because the code goes from max. depth to min
shear_stress_value=shear_stress_value[::-1,:]
friction_value= np.transpose(friction_value)
shear_stress_value=np.transpose(shear_stress_value)
print (friction_value.shape)
print('shape of the fields after reshaping',shear_stress_value.shape)



# I am settting the stresses and frictional parameters together. Since both are being loaded from the same file.
# It will be easier this way.
x = np.linspace(-30., 30., nx)
y = np.linspace(250, 0, nz ) # inorder to make it similar to the input file, i used 250 which is 25km
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

starting_index_x = np.where(x == -30.)   # we just need to find the first index since spatial resolution is same both in file and in code.
starting_index_y= np.where(y == 155)
print ('from here it will start',starting_index_y[0][0])

for i in range(data_nx):
 for j in range(data_ny):  
  tauh[i][starting_index_y[0][0]+j]= shear_stress_value[i][j]  # 'i' needs to be  tau [i +starting_index_x] [j+starting_index_y[0][0]] but since my x starts at -30 so I donot need it.
  mus[i][starting_index_y[0][0]+j]= friction_value[i][j]  

plt.pcolor(mus)
plt.show()

print(' this is total number of points ', data_ny+ starting_index_y[0][0])
p.set_loadfile(0, fdfault.loadfile(nx, nz, sigman, tauh, tauv)) 
p.set_paramfile(0, fdfault.swparamfile(nx, nz, dc, mus, mud, c0, trup, tc) )

# # set initial stress

# zer = np.zeros((nx, nz))
# c0 = np.zeros((nx, nz))

# x = np.linspace(-30., 30., nx)
# z = np.linspace(-30., 0., nz)

# for i in range(nz):
#     if -z[i] <= 2.4:
#         c0[:,i] = 0.000425*(2400.+1000.*z[i])

# p.set_paramfile(0, fdfault.swparamfile(nx, nz, zer, zer, zer, c0, zer, zer))

# mu0 = 32.03812032

# sn = np.zeros((nx, nz))
# st = np.zeros((nx, nz))

# for i in range(nx):
#     for j in range(nz):
#         r = np.sqrt(x[i]**2+(-z[j]-7.5)**2)
#         sn[i,j] = -60.*mat[2,i,ny,j]/mu0
#         if r <= 1.4:
#             st[i,j] = 34.95*mat[2,i,ny,j]/mu0
#         elif r <= 2.:
#             st[i,j] = (30.+2.475*(1.+np.cos(np.pi*(r-1.4)/0.6)))*mat[2,i,ny,j]/mu0
#         else:
#             st[i,j] = 30.*mat[2,i,ny,j]/mu0

# p.set_loadfile(0, fdfault.loadfile(nx, nz, sn, st, zer))

# add output units

# on fault stations

onfault = []
st1 = ['-250', '-200', '-150', '-100', '-050', '000', '050']
dp1 = ['081']
for st in st1:
    for dp in dp1:
        onfault.append((st, dp))


fields = ['h-slip', 'h-slip-rate', 'h-shear-stress', 'v-slip', 'v-slip-rate', 'v-shear-stress', 'n-stress']
fname = ['Ux', 'Vx', 'Sx', 'Uz', 'Vz', 'Sz', 'Sn']

for station in onfault:
    xcoord = float(station[0])/10.
    zcoord = -float(station[1])/10.
    xpt, ypt, zpt = p.find_nearest_point((xcoord, 0., zcoord), known='y', knownloc=ny)
    for fld, fn in zip(fields, fname):
        p.add_output(fdfault.output('faultst'+station[0]+'dp'+station[1]+'-'+fld, fn, 0, nt, 1, xpt, xpt, 1, ypt, ypt, 1, zpt, zpt, 1))


# # off fault stations
# loading the data file
station_data=np.genfromtxt('tpv35_station_locations.txt',dtype='str')

offfault = []
st1= []
ac1=[]
dp1=[]
station_name=[]
for i in range(station_data.shape[0]):
 st1.append(station_data[i,3])
 ac1.append(station_data[i,2])
 dp1.append('000')
 station_name.append(station_data[i,0]) 
for i in range(station_data.shape[0]):
 offfault.append((st1[i],ac1[i],dp1[i], station_name[i]) )

fields = ['h-vel', 'v-vel', 'n-vel']
fname = ['vx', 'vz', 'vy']

for station in offfault:
    xcoord = float(station[0])/1000
    ycoord = float(station[1])/1000
    zcoord = -float(station[2])
    xpt, ypt, zpt = p.find_nearest_point((xcoord, ycoord, zcoord))
    for fld, fn in zip(fields, fname):
        p.add_output(fdfault.output(station[3] +'-'+fld, fn, 0, nt, 1, xpt, xpt, 1,
                                    ypt, ypt, 1, zpt, zpt, 1))


print (p.get_nifaces() )
#print(dp1) 
#print(offfault)

# for st in st1:
#     for ac in ac1:
#      offfault.append((st1, ac1))

#print(offfault)      
#print(offfault)
# #p.add_output(fdfault.output('vfault','V', 0, nt, 10, 0, nx-1, 2, ny1+ny2, ny1+ny2, 1, 0, nz-1, 2))

# #p.set_front_output(True)

p.write_input()
