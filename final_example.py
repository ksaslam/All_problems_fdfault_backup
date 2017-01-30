import fdfault
import numpy as np

# create problem

p = fdfault.problem('yixin_example_final')

# set rk and fd order

p.set_rkorder(4)
p.set_sbporder(4)

# set time step info

nt = 161
tinterval = 20
p.set_nt(nt)
p.set_cfl(0.3)
p.set_ninfo(tinterval)

# set number of blocks and coordinate information

##########################
#model has a length x=320km, width 2*y=300km (1,2,1)
#use refine=500m so the mesh will be 640*1200
refine = 0.5
#model blocks will be
nbx = 641
nby = 601
mdx = (nbx-1)*refine
mdy = (nby-1)*refine
###########################

p.set_nblocks((1,2,1))
p.set_nx_block(([nbx], [nby,nby], [1]))

# set block dimensions

p.set_block_lx((0,0,0),(mdx,mdy))
p.set_block_lx((0,1,0),(mdx,mdy))

# set block boundary conditions

p.set_bounds((0,0,0),['absorbing', 'absorbing', 'absorbing', 'none'])
p.set_bounds((0,1,0),['absorbing', 'absorbing', 'none', 'absorbing'])

########################
x = np.linspace(0., 320., 641)
y = 300.*np.ones(641)
plt.plot(x,y)
#plt.show()

surf = fdfault.curve(641, 'y', x, y)

p.set_block_surf((0,0,0), 1, surf)
p.set_block_surf((0,1,0), 0, surf)
###############################

# set initial fields

p.set_stress((-100., 70., 0., -120., 0., 0.)) # first is sxx (normal), third is sxz (shear)

# set interface type

p.set_iftype(0,'slipweak')


#############################
# set slip weakening parameters

p.add_pert(fdfault.swparam('constant', dc = 0.4, mus = 0.676, mud = 0.525),0)
p.add_pert(fdfault.swparam('boxcar', x0 = 50., dx = 50., mus = 10000.),0) # lower barrier from 0 to 12 km
p.add_pert(fdfault.swparam('boxcar', x0 = 270., dx = 50., mus = 10000.),0) # upper barrier from 16 to 24 km

#############################
# add load perturbations

p.add_load(fdfault.load('boxcar',0., 160., .2, 0., 0., 13.6, 0., 0.)) # nucleation

#############################
# add output unit
p.add_output(fdfault.output('vxbody','vx',0, nt-1, 20, 0, nbx-1, 2, 0, 2*nby-2, 2, 0, 0, 1)) # change 900 to match appropriate station location
p.add_output(fdfault.output('vybody','vy',0, nt-1, 20, 0, nbx-1, 2, 0, 2*nby-2, 2, 0, 0, 1)) 
#p.add_output(fdfault.output('vypt','vy',0, nt-1, 1, 164, 164, 1, 343, 343, 1, 0, 0, 1)) # change 900 to match appropriate station location
p.add_output(fdfault.output('vfault','V',0, nt-1, 1, nbx-1, nbx-1, 1, 0, nby-1, 2, 0, 0, 1)) # on-fault output

# getting the value of nx
print('This is nx value')
p.get_nx()
p.write_input()


