import fdfault
import numpy as np
import seistools.rough

# create problem

p = fdfault.problem('teststz')

# set rk and fd order

p.set_rkorder(4)
p.set_sbporder(4)

# set time step info

p.set_nt(500)
p.set_cfl(0.3)
p.set_ninfo(40)

# set number of blocks and coordinate information

p.set_nblocks((1,2,1))
p.set_nx_block(([1601], [801, 801], [1]))

# set block dimensions

p.set_block_lx((0,0,0),(40.,20.))
p.set_block_lx((0,1,0),(40.,20.))

x = np.linspace(0., 40., 1601)
y = 16.*np.ones(1601)+seistools.rough.generate_profile(1601, 24, 10**-2, 8, h = 1., seed=None)

surf = fdfault.curve(1601, 'y', x, y)

p.set_block_surf((0,0,0), 3, surf)
p.set_block_surf((0,1,0), 2, surf)

# set block boundary conditions

p.set_bounds((0,0,0),['absorbing', 'absorbing', 'absorbing', 'none'])
p.set_bounds((0,1,0),['absorbing', 'absorbing', 'none', 'absorbing'])

# set initial fields

p.set_stress((-100., 72.5, 0., -120., 0., 0.))

# set interface type

p.set_iftype(0,'stz')

# set stz parameters

p.add_pert(fdfault.stzparam('constant', v0=1.e-6, f0 = 130., a = 0.0037, muy = 0.3, c0 = 500., R = 0., beta = 0., chiw = 0.8, v1 = 1000.), 0)

# set initial state

p.set_state(0, 0.025)

# add load perturbations

p.add_load(fdfault.load('boxcar',0., 20., 1.5, 0., 0., 0., 9.1, 0.))

# add output unit
p.add_output(fdfault.output('vybody','vy',0, 500, 20, 0, 1600, 2, 0, 1600, 2, 0, 0, 1))
p.add_output(fdfault.output('vfault','V',0, 500, 8, 0, 1600, 1, 801, 801, 1, 0, 0, 1))
p.add_output(fdfault.output('sfault','S',0, 500, 8, 0, 1600, 1, 801, 801, 1, 0, 0, 1))
p.add_output(fdfault.output('chifault','state',0, 500, 8, 0, 1600, 1, 801, 801, 1, 0, 0, 1))

p.write_input()
