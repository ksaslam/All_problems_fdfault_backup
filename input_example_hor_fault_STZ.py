import fdfault
import numpy as np
import seistools.rough
# create problem

p = fdfault.problem('testprob_hor')

# set rk and fd order

p.set_rkorder(4)
p.set_sbporder(4)

# set time step info
nt=10
interval_time= 5
p.set_nt(nt)
p.set_cfl(0.3)
p.set_ninfo(interval_time)

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
y = 16.*np.ones(1201)+seistools.rough.generate_profile(1201, 24, 10**-2, 8, h = 1., seed=None)

# Saving the output for the normal vector calculation
np.savetxt('x.out', x, delimiter=',') 
np.savetxt('y.out', y, delimiter=',')


surf = fdfault.curve(1201, 'y', x, y)

p.set_block_surf((0,0,0), 3, surf)
p.set_block_surf((0,1,0), 2, surf)

# set initial fields

p.set_stress((-100., 72.5, 0., -120., 0., 0.))
# set interface type

p.set_iftype(0,'stz')


p.add_pert(fdfault.stzparam('constant', v0=1.e-6, f0 = 130., a = 0.0037, muy = 0.3, c0 = 500., R = 0., beta = 0., chiw = 0.8, v1 = 1000.), 0)
#p.add_pert(fdfault.stzparam('constant',v0 = 0.0005, f0 = 0., a = 10.**-2, muy = 0.1, c0 = 10**3, R = 4., beta = 0.4, chiw = 10**20, v1 = 100.0),0)
p.set_state(0, 0.025)
p.add_load(fdfault.load('boxcar',0., 20., 1.5, 0., 0., 0., 9.1, 0.))

p.add_pert(fdfault.stzparam('boxcar', x0 = 3., dx = 1., muy = 100.),0)
p.add_pert(fdfault.stzparam('boxcar', x0 = 18., dx = 1., muy = 100.),0)

# add load perturbations

#p.add_load(fdfault.load('boxcar',0., 16., 1.5, 0., 0., 0., 11.6, 0.))

# add output unit

p.add_output(fdfault.output('vxbody','vx',0, nt, interval_time, 0, 1200, 2, 0, 1600, 2, 0, 0, 1))
p.add_output(fdfault.output('vybody','vy',0, nt, interval_time, 0, 1200, 2, 0, 1600, 2, 0, 0, 1))
#p.add_output(fdfault.output('vfault','V',0, 1600, 10, 601, 601, 1, 0, 1600, 2, 0, 0, 1))
p.add_output(fdfault.output('sxybody','sxy',0, nt, interval_time, 0, 1200, 2, 0, 1600, 2, 0, 0, 1))
p.add_output(fdfault.output('vfault','V',0, nt, interval_time, 0, 1200, 1, 801, 801, 1, 0, 0, 1))
p.add_output(fdfault.output('sfault','S',0, nt, interval_time, 0, 1200, 1, 801, 801, 1, 0, 0, 1))
p.add_output(fdfault.output('snfault','Sn',0, nt, interval_time, 0, 1200, 1, 801, 801, 1, 0, 0, 1))





p.write_input()
