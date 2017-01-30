import fdfault
import numpy as np
from rough import generate_profile 
# create problem

p = fdfault.problem('testprob_hor')

# set rk and fd order

p.set_rkorder(4)
p.set_sbporder(4)

# set time step info

p.set_nt(401)
p.set_cfl(0.3)
p.set_ninfo(50)

# set number of blocks and coordinate information

p.set_nblocks((1,2,1))
p.set_nx_block(([1201], [801,801], [1]))

# set block dimensions

p.set_block_lx((0,0,0),(24.,16.))
p.set_block_lx((0,1,0),(24.,16.))

# set block boundary conditions

p.set_bounds((0,0,0),['absorbing', 'absorbing', 'absorbing', 'none'])
p.set_bounds((0,1,0),['absorbing', 'absorbing', 'none', 'absorbing'])

# set block surface
# need to look at it carefully 

x = np.linspace(0., 24., 1201)
y = 16.*np.ones(1201)+generate_profile(1201, 24, 10**-2, 8, h = 1., seed=None, sd = 1.e-1)

surf = fdfault.curve(1201, 'y', x, y)

p.set_block_surf((0,0,0), 3, surf)
p.set_block_surf((0,1,0), 2, surf)

# set initial fields

p.set_stress((-120., 70., 0., -100., 0., 0.))

# set interface type

p.set_iftype(0,'slipweak')

# set slip weakening parameters

p.add_pert(fdfault.swparam('constant', dc = 0.4, mus = 0.676, mud = 0.225),0)
p.add_pert(fdfault.swparam('boxcar', y0 = 3., dy = 2., mus = 10000.),0)
p.add_pert(fdfault.swparam('boxcar', y0 = 21., dy = 2., mus = 10000.),0)

# add load perturbations

p.add_load(fdfault.load('boxcar',0., 16., 1.5, 0., 0., 0., 11.6, 0.))

# add output unit

p.add_output(fdfault.output('vxbody','vx',0, 400, 50, 0, 1200, 2, 0, 1600, 2, 0, 0, 1))
p.add_output(fdfault.output('vybody','vy',0, 400, 50, 0, 1200, 2, 0, 1600, 2, 0, 0, 1))
#p.add_output(fdfault.output('vfault','V',0, 1600, 10, 601, 601, 1, 0, 1600, 2, 0, 0, 1))

p.write_input()
