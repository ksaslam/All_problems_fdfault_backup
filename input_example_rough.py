import fdfault
import numpy as np
import seistools.rough

# create problem

p = fdfault.problem('rough_fault')

# set rk and fd order

p.set_rkorder(4)
p.set_sbporder(4)

# set time step info

end_time= 1001
interval_time=50
p.set_nt(end_time)
p.set_cfl(0.3)
p.set_ninfo(interval_time)

# set number of blocks and coordinate information

p.set_nblocks((2,1,1))
p.set_nx_block(([601, 601], [1601], [1]))

# set block dimensions

p.set_block_lx((0,0,0),(12.,32.))
p.set_block_lx((1,0,0),(12.,32.))

# set block boundary conditions

p.set_bounds((0,0,0),['absorbing', 'none', 'absorbing', 'absorbing'])
p.set_bounds((1,0,0),['none', 'absorbing', 'absorbing', 'absorbing'])

# set block surface

y = np.linspace(0., 32., 1601)
x = 12.*np.ones(1601)+seistools.rough.generate_profile(1601, 32, 10**-2,20, h = 1., seed=None)

surf = fdfault.curve(1601, 'x', x, y)

p.set_block_surf((0,0,0), 1, surf)
p.set_block_surf((1,0,0), 0, surf)

# set initial fields

p.set_stress((-120., 70., 0., -100., 0., 0.))

# set interface type

p.set_iftype(0,'slipweak')

# set slip weakening parameters

p.add_pert(fdfault.swparam('constant', dc = 0.4, mus = 0.676, mud = 0.525),0)
p.add_pert(fdfault.swparam('boxcar', x0 = 2., dx = 2., mus = 10000.),0)
p.add_pert(fdfault.swparam('boxcar', x0 = 30., dx = 2., mus = 10000.),0)

# add load perturbations

p.add_load(fdfault.load('boxcar',0., 16., 1.5, 0., 0., 0., 11.6, 0.))

# add output unit

p.add_output(fdfault.output('sxxbody','sxx',0, 400, 50, 0, 1200, 2, 0, 1600, 2, 0, 0, 1))

# first 3 coord for time , then space 
p.add_output(fdfault.output('vxbody','vx',0, 400, 50, 0, 1200, 2, 0, 1600, 2, 0, 0, 1))
p.add_output(fdfault.output('vybody','vy',0, 400, 50, 0, 1200, 2, 0, 1600, 2, 0, 0, 1))
p.add_output(fdfault.output('vfault','V',0, 400, 50, 601, 601, 1, 0, 1600, 2, 0, 0, 1))
p.add_output(fdfault.output('vfault','U',0, 400, 50, 601, 601, 1, 0, 1600, 2, 0, 0, 1))
p.add_output(fdfault.output('sxxbody','sxx',0, 400, 50, 0, 1200, 2, 0, 1600, 2, 0, 0, 1))
p.add_output(fdfault.output('sxybody','sxy',0, 400, 50, 0, 1200, 2, 0, 1600, 2, 0, 0, 1))
p.add_output(fdfault.output('syybody','syy',0, 400, 50, 0, 1200, 2, 0, 1600, 2, 0, 0, 1))


p.write_input()
