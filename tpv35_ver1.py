import fdfault
import numpy as np

# create problem

p = fdfault.problem('tpv35')

# set rk and fd order

p.set_rkorder(4)
p.set_sbporder(4)

# set time step info

nt = 4192

p.set_nt(nt)
p.set_dt(0.004294)
p.set_ninfo(500)

p.set_ndim(3)

# set number of blocks and coordinate information

refine = 1
total_nz= 17

nx = 600*refine+1   # total domain size along strike 60km 
ny1 = 240*refine+1  # total domain size each side  of fault 20km


# total depth is 25 km
nz1 = 10*refine+1
nz2=  8*refine+1
nz3=  2*refine+1
nz4=  1*refine+1
nz5= 9*refine+1
nz6= 4*refine+1
nz7= 1*refine+1
nz8= 4*refine+1
nz9= 19*refine+1
nz10= 25*refine+1
nz11= 44*refine+1
nz12= 14*refine+1
nz13= 30*refine+1
nz14= 4*refine+1
nz15= 28*refine+1
nz16= 1*refine+1
nz17= 46*refine+1



# This block of the code is to find the depths of the different interfaces defined at the top

layers_z = np.array ([10, 8, 2, 1, 9, 4, 1, 4 , 19, 25, 44, 14, 30, 4, 28, 1 , 46])
summ=0
layers_depth=np.zeros(len(layers_z))
for i in range (len(layers_z)):
 summ= layers_z[i] + summ
 layers_depth[i]= summ




# This block of code sets the number of blocks in each cartesian direction

p.set_nblocks((1,2,17))  
p.set_nx_block(([nx], [ny1, ny1], [nz1, nz2, nz3, nz4, nz5, nz6, nz7, nz8, nz9, nz10, nz11, nz12, nz13, nz14, nz15, nz16, nz17]))


# set block dimensions

p.set_block_lx((0,0,0),(60.,24.,1.))
p.set_block_lx((0,0,0),(60.,24.,1.))
p.set_block_lx((0,0,1),(60.,24.,.8))
p.set_block_lx((0,0,2),(60.,24.,.2))
p.set_block_lx((0,0,3),(60.,24.,.1))
p.set_block_lx((0,0,4),(60.,24.,.9))
p.set_block_lx((0,0,5),(60.,24.,.4))
p.set_block_lx((0,0,6),(60.,24.,.1))
p.set_block_lx((0,0,7),(60.,24.,.4))
p.set_block_lx((0,0,8),(60.,24.,1.9))
p.set_block_lx((0,0,9),(60.,24.,2.5))
p.set_block_lx((0,0,10),(60.,24.,4.4))
p.set_block_lx((0,0,11),(60.,24.,1.4))
p.set_block_lx((0,0,12),(60.,24.,3.0))
p.set_block_lx((0,0,13),(60.,24.,.4))
p.set_block_lx((0,0,14),(60.,24.,2.8))
p.set_block_lx((0,0,15),(60.,24.,.1))
p.set_block_lx((0,0,16),(60.,24.,4.6))



p.set_block_lx((0,1,0),(60.,24.,1.0))
p.set_block_lx((0,1,1),(60.,24.,.8))
p.set_block_lx((0,1,2),(60.,24.,.2))
p.set_block_lx((0,1,3),(60.,24.,.1))
p.set_block_lx((0,1,4),(60.,24.,.9))
p.set_block_lx((0,1,5),(60.,24.,.4))
p.set_block_lx((0,1,6),(60.,24.,.1))
p.set_block_lx((0,1,7),(60.,24.,.4))
p.set_block_lx((0,1,8),(60.,24.,1.9))
p.set_block_lx((0,1,9),(60.,24.,2.5))
p.set_block_lx((0,1,10),(60.,24.,4.4))
p.set_block_lx((0,1,11),(60.,24.,1.4))
p.set_block_lx((0,1,12),(60.,24.,3.0))
p.set_block_lx((0,1,13),(60.,24.,.4))
p.set_block_lx((0,1,14),(60.,24.,2.8))
p.set_block_lx((0,1,15),(60.,24.,.1))
p.set_block_lx((0,1,16),(60.,24.,4.6))




# minimum values of the domain
p.set_domain_xm((-30., -12.0, -25.0))





# set block boundary conditions

p.set_bounds((0,0,0),['absorbing', 'absorbing', 'absorbing', 'none', 'absorbing', 'none'])
p.set_bounds((0,1,0),['absorbing', 'absorbing', 'none', 'absorbing', 'absorbing', 'none'])

p.set_bounds((0,0,1),['absorbing', 'absorbing', 'absorbing', 'none', 'none', 'none'])
p.set_bounds((0,1,1),['absorbing', 'absorbing', 'none', 'absorbing', 'none', 'none'])

p.set_bounds((0,0,2),['absorbing', 'absorbing', 'absorbing', 'none', 'none', 'none'])
p.set_bounds((0,1,2),['absorbing', 'absorbing', 'none', 'absorbing', 'none', 'none'])

p.set_bounds((0,0,3),['absorbing', 'absorbing', 'absorbing', 'none', 'none', 'none'])
p.set_bounds((0,1,3),['absorbing', 'absorbing', 'none', 'absorbing', 'none', 'none'])

p.set_bounds((0,0,4),['absorbing', 'absorbing', 'absorbing', 'none', 'none', 'none'])
p.set_bounds((0,1,4),['absorbing', 'absorbing', 'none', 'absorbing', 'none', 'none'])

p.set_bounds((0,0,5),['absorbing', 'absorbing', 'absorbing', 'none', 'none', 'none'])
p.set_bounds((0,1,5),['absorbing', 'absorbing', 'none', 'absorbing', 'none', 'none'])

p.set_bounds((0,0,6),['absorbing', 'absorbing', 'absorbing', 'none', 'none', 'none'])
p.set_bounds((0,1,6),['absorbing', 'absorbing', 'none', 'absorbing', 'none', 'none'])

p.set_bounds((0,0,7),['absorbing', 'absorbing', 'absorbing', 'none', 'none', 'none'])
p.set_bounds((0,1,7),['absorbing', 'absorbing', 'none', 'absorbing', 'none', 'none'])

p.set_bounds((0,0,8),['absorbing', 'absorbing', 'absorbing', 'none', 'none', 'none'])
p.set_bounds((0,1,8),['absorbing', 'absorbing', 'none', 'absorbing', 'none', 'none'])

p.set_bounds((0,0,9),['absorbing', 'absorbing', 'absorbing', 'none', 'none', 'none'])
p.set_bounds((0,1,9),['absorbing', 'absorbing', 'none', 'absorbing', 'none', 'none'])

p.set_bounds((0,0,10),['absorbing', 'absorbing', 'absorbing', 'none', 'none', 'none'])
p.set_bounds((0,1,10),['absorbing', 'absorbing', 'none', 'absorbing', 'none', 'none'])

p.set_bounds((0,0,11),['absorbing', 'absorbing', 'absorbing', 'none', 'none', 'none'])
p.set_bounds((0,1,11),['absorbing', 'absorbing', 'none', 'absorbing', 'none', 'none'])

p.set_bounds((0,0,12),['absorbing', 'absorbing', 'absorbing', 'none', 'none', 'none'])
p.set_bounds((0,1,12),['absorbing', 'absorbing', 'none', 'absorbing', 'none', 'none'])

p.set_bounds((0,0,13),['absorbing', 'absorbing', 'absorbing', 'none', 'none', 'none'])
p.set_bounds((0,1,13),['absorbing', 'absorbing', 'none', 'absorbing', 'none', 'none'])

p.set_bounds((0,0,14),['absorbing', 'absorbing', 'absorbing', 'none', 'none', 'none'])
p.set_bounds((0,1,14),['absorbing', 'absorbing', 'none', 'absorbing', 'none', 'none'])

p.set_bounds((0,0,15),['absorbing', 'absorbing', 'absorbing', 'none', 'none', 'none'])
p.set_bounds((0,1,15),['absorbing', 'absorbing', 'none', 'absorbing', 'none', 'none'])

p.set_bounds((0,0,16),['absorbing', 'absorbing', 'absorbing', 'none', 'none', 'free'])
p.set_bounds((0,1,16),['absorbing', 'absorbing', 'none', 'absorbing', 'none', 'free'])



# set material

# 0- 1000 layer 1 & 2     =1 
rho = 2.0
cs = 1.1
cp = 2.0
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,0,0))
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,1,0))

# 1000- 2000 layer 1   = 2,3
rho = 2.3
cs = 2.0
cp = 3.5
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,0,1))


# 1000- 1800 layer 2   = 2
rho = 2.3
cs = 2.2
cp = 3.5
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,1,1))

# 1000- 2000 layer 1   = 2,3
rho = 2.3
cs = 2.0
cp = 3.5

p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,0,2))

# 1800- 2100 layer 2     = 3,4
rho = 2.3
cs = 2.2
cp = 4.3
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,1,2))
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,1,3))

# 2000- 3000 layer 1  = 4,5
rho = 2.3
cs = 2.5
cp = 4.5
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,0,3))
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,0,4))

# 2100- 3400 layer 2 = 5,6
rho = 2.3
cs = 2.7
cp = 4.8
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,1,4))
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,1,5))

# 3000- 3500 layer 1  = 6,7
rho = 2.5
cs = 3.0
cp = 5.2
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,0,5))
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,0,6))

# 3400- 3900 layer 2  = 7,8
rho = 2.3
cs = 2.8
cp = 5.2
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,1,6))
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,1,7))

# 3500- 5800 layer 1  = 8,9
rho = 2.7
cs = 3.2
cp = 5.7
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,0,7))
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,0,8))

# 3900- 8300 layer 2   = 9,10
rho = 2.7
cs = 3.2
cp = 5.3
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,1,8))
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,1,9))

# 5800- 14100 layer 1  = 10,11,12
rho = 2.7
cs = 3.6
cp = 6.2
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,0,9))
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,0,10))
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,0,11))

# 8300-12700 layer 2 = 11
rho = 2.8
cs = 3.7
cp = 5.7
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,1,10))

# 12700-17500 layer 2 =12,13,14
rho = 2.8 
cs = 3.8
cp = 6.5
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,1,11))
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,1,12))
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,1,13))

# 14100-17100 layer 1 = 13
rho = 2.8
cs = 3.6
cp = 6.8
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,0,12))

# 17100-20,400 layer 1    = 14,15,16
rho = 2.8
cs = 4.3
cp = 6.8
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,0,13))
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,0,14))
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,0,15))

# 20,400-full depth layer 1  = 17
rho = 2.8
cs = 4.3
cp = 7.3
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,0,16))

# 17500-20,300 layer 2 = 15
rho = 2.8
cs = 4.3
cp = 6.7
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,1,14))

# 20,300-full depth layer 2 = 16,17
rho = 2.8
cs = 4.3
cp = 7.3
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,1,15))
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,1,16))





# turn on artificial dissipation
#p.set_cdiss(0.1)





# set interface type for the friction. I am just defining the type of interface here but I will do the parameters assignment 
#later below:
for i in range(total_nz):
 p.set_iftype(i,'slipweak')
#  p.add_pert(fdfault.swparam('constant',0., 0., 0., 0., 0., 0.18, 0.55, 0.45),i)


 



# loading the input data file. Then reshaping it to make it workable to  code conditions.
input_data = np.loadtxt("tpv35_input_data.txt")
friction_coeff= input_data[:,4]
shear_stress= input_data[:, 5]
data_nx= 401
data_ny= int( len(friction_coeff)/ data_nx ) 
friction_value=np.reshape(friction_coeff, (data_nx,data_ny) ) # reshaping data to make it in the usable format
shear_stress_value= np.reshape(shear_stress, (data_nx,data_ny) ) # reshaping data to make it in the usable format
friction_value= friction_value[:,::-1]           # flipping the values because the code goes from max. depth to min
shear_stress_value=shear_stress_value[:,::-1]
print('shape of the fields after reshaping',shear_stress_value.shape)






# finding the starting block (having depth 15.5 km) because we need to set shear stress from input file
first_layer_index= np.where(layers_depth >= 155)
starting_depth= first_layer_index[0][0]   # this is the index that will tell from where we start giving stress values.



# Setting the shear stress and frictional paramters for all the blocks that lie outside the extent provided in the input file.
counter=0
for i in range(total_nz):
 layer_no= 'nz' + str(total_nz-i)

 if total_nz-i > starting_depth+1:   # Since we just need to stop outside the layer which has depth 155km.
  counter= counter+1                  # counting number of layers which are outside the range.
  first_inside_layer= 'nz' + str(total_nz-i-1) # This particular step is used to store the last layer number in the loop. 
  
  # setting stresses
  sigman = -60.*np.ones((nx, eval(layer_no)))
  tauh = np.zeros((nx,eval(layer_no)))
  tauv = np.zeros((nx,eval(layer_no)))
  p.set_loadfile(i, fdfault.loadfile(nx, eval(layer_no), sigman, tauh, tauv))
  
  # Setting the interface frictional law parameters now
  dc = 0.15*np.ones((nx, eval(layer_no)))
  mus = np.zeros((nx, eval(layer_no)))
  mud = 0.3*np.ones((nx, eval(layer_no)))
  trup = np.zeros((nx, eval(layer_no)))
  tc= np.zeros((nx, eval(layer_no)))
  c0= np.zeros((nx, eval(layer_no)))
  p.set_paramfile(i, fdfault.swparamfile(nx, eval(layer_no), dc, mus, mud, c0, trup, tc) )

  final_interface_outside= i





# Setting  the shear stress for 'only' first block inside the extent of the input provided.
# layers_depth[first_layer_index[0][0]]) and layers_depth[first_layer_index[0][0]-1] are the starting and ending depth of 
# the full layer. (17.1 km to 14.1 km. Since 15.5km is inside that layer, we will start inserting values at that location)

x = np.linspace(-30., 30., nx)
y = np.linspace(layers_depth[first_layer_index[0][0]], layers_depth[first_layer_index[0][0]-1], eval(first_inside_layer) ) 
print ('a test check', layers_depth[first_layer_index[0][0]], layers_depth[first_layer_index[0][0]-1])
starting_index_x =np.where(x == -30.)   # we just need to find the first index since spatial resolution is same both in file and in code.
starting_index_y= np.where(y == 155)
print(starting_index_y)
total_entries_in_first_inside_layer = eval(first_inside_layer)-starting_index_y[0][0] # total entries to populate 
sigman = -60.*np.ones((nx, eval(first_inside_layer)))
tauh = np.zeros((nx,eval(first_inside_layer)))
tauv = np.zeros((nx,eval(first_inside_layer)))
# Setting the interface frictional law parameters now
dc = 0.15*np.ones((nx, eval(first_inside_layer)))
mus = np.zeros((nx,eval(first_inside_layer)))
mud = 0.3*np.zeros((nx,eval(first_inside_layer)))
trup = np.zeros((nx,eval(first_inside_layer)))
tc= np.zeros((nx,eval(first_inside_layer)))
c0= np.zeros((nx,eval(first_inside_layer)))

for i in range(data_nx):
 for j in range(total_entries_in_first_inside_layer):  
  layer_depth= j
  tauh[i][starting_index_y[0][0]+j]= shear_stress_value[i][j]  # 'i' needs to be  tau [i +starting_index_x] [j+starting_index_y[0][0]] but since my x starts at -30 so I donot need it.
  mus[i][starting_index_y[0][0]+j]= friction_value[i][j]
print ('layer_depth',layer_depth)
number_of_coloums_skip=total_entries_in_first_inside_layer     # how many values are we skipping from the file
print(' z value at that particluar place', y[starting_index_y[0][0]+j])
p.set_loadfile(final_interface_outside+1, fdfault.loadfile(nx, eval(first_inside_layer), sigman, tauh, tauv)) 
p.set_paramfile(final_interface_outside+1, fdfault.swparamfile(nx, eval(first_inside_layer), dc, mus, mud, c0, trup, tc) )






# Setting the stresses for inside layers starting from the second inside layer . Since i have given the first layer manually.

number_of_inside_layers= total_nz-counter-1       # since I have done the first inside layer separately
print ('number_of_inside_layers', number_of_inside_layers)

skip=total_entries_in_first_inside_layer-1      # have to give the last value to the next value. Since it is a common node.
previous_boundary= shear_stress_value[:][skip]     # storing all values at the common interface of the first inside interface.
previous_boundary_friction= friction_value[:][skip]
for layers in range (number_of_inside_layers):   
 layer= 'nz'+ str(number_of_inside_layers-layers)
 sigman = -60.*np.ones((nx, eval(layer) ))
 tauh = np.zeros((nx,eval(layer)))
 tauv = np.zeros((nx,eval(layer))) 
# Setting the interface frictional law parameters now
 dc = 0.15*np.ones((nx, eval(layer)))
 mus = np.zeros((nx, eval(layer)))
 mud = 0.3*np.ones((nx, eval(layer)))
 trup = np.zeros((nx, eval(layer)))
 tc= np.zeros((nx, eval(layer)))
 c0= np.zeros((nx, eval(layer)))
 
 value=eval(layer)-1             # storing the number of coloumns, we need to skip.  '-1' because every layer have 1 entry extra than the normal 
 for i in range(data_nx):
  for j in range( eval(layer) ):  
   if j==0:
    for k in range(len(previous_boundary)):
     tauh[k][j]= previous_boundary[k]
     mus[k][j]= previous_boundary_friction[k]
    else:
     tauh[i][j]= shear_stress_value[i][j+skip]
     mus[i][j]= friction_value[i][j+skip] 
  #print(j+skip) 
   #tauh[i][j]= shear_stress_value[i][j+number_of_coloums_skip-1-layer] 
  previous_boundary= shear_stress_value[:][j+skip]
  previous_boundary_friction= friction_value[:][j+skip]
 skip= value+ skip
 p.set_loadfile(final_interface_outside+2+layers, fdfault.loadfile(nx, eval(layer), sigman, tauh, tauv))
 p.set_paramfile(final_interface_outside+2+layers, fdfault.swparamfile(nx, eval(layer), dc, mus, mud, c0, trup, tc) )
 


 
  







#p.add_load(fdfault.load('boxcar',0., 5., 2., 5., 1., 0., 0.7, 0.))
#for i in range(nx):
#    for j in range(nz):
#        if x[i] == -30.:
#            counter=0
#            print (i)
#            tauh(i)= 
#        elif x[i] > 1.1:
#            Rx = (x[i]-1.1)/10.
#        else:
#            Rx = 0.
#        if y[j] < 2.3:
#            Ry = (-y[j]+2.3)/10.
#        elif y[j] > 8.:
#            Ry = (y[j]-8.)/10.
#        else:
#            Ry = 0.
#        Rt = np.minimum(1., np.sqrt(Rx**2+Ry**2))
#        r = np.sqrt((x[i]+6.)**2+(y[j]-6.)**2)
#        if r <= 0.55:
#            tnucl = 3.15
#        elif r <= 0.8:
#            tnucl = 1.575*(1.+np.cos(np.pi*(r-0.55)/0.25))
#        else:
#            tnucl = 0.
#        tauh[i,j] = 30.*(1.-Rt)+tnucl

#p.set_loadfile(1, fdfault.loadfile(nx, nz, sigman, tauh, tauv))

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
    xpt, ypt, zpt = p.find_nearest_point((xcoord, 0., zcoord), known='y', knownloc=ny1)
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

for station in offfault:
    xcoord = float(station[0])/1000
    ycoord = float(station[1])/1000
    zcoord = -float(station[2])
    xpt, ypt, zpt = p.find_nearest_point((xcoord, ycoord, zcoord))
    for fld, fn in zip(fields, fname):
        p.add_output(fdfault.output(station[3] +'-'+fld, fn, 0, nt, 1, xpt, xpt, 1,
                                    ypt, ypt, 1, zpt, zpt, 1))

#print(dp1) 
#print(offfault)

# for st in st1:
#     for ac in ac1:
#      offfault.append((st1, ac1))

#print(offfault)      
#print(offfault)
# #p.add_output(fdfault.output('vfault','V', 0, nt, 10, 0, nx-1, 2, ny1+ny2, ny1+ny2, 1, 0, nz-1, 2))

# #p.set_front_output(True)
print (p.get_nifaces() )
p.write_input()