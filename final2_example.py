import fdfault
import numpy as np
import matplotlib.pyplot as plt
# create problem

p = fdfault.problem('yixin_final_example')

# set rk and fd order

p.set_rkorder(4)
p.set_sbporder(4)

# set time step info
end_time= 2001
interval_time=500
p.set_nt(end_time)
p.set_cfl(0.5)
p.set_ninfo(interval_time)

interval_time= int(interval_time/100 )

#############
# model has a width 2*mx=600km length my=320km (2,1,1)
# mesh has nx=600 ny=640 refine=2
nx = 600
ny = 640
refine = 2
mx = nx/refine
my = ny/refine
############## 

# set number of blocks and coordinate information

p.set_nblocks((2,1,1))
p.set_nx_block(([nx+1, nx+1], [ny+1], [1]))

# set block dimensions

p.set_block_lx((0,0,0),(mx,my))
p.set_block_lx((1,0,0),(mx,my))

# set block boundary conditions

p.set_bounds((0,0,0),['absorbing', 'none', 'absorbing', 'absorbing'])
p.set_bounds((1,0,0),['none', 'absorbing', 'absorbing', 'absorbing'])

# set block surface

y = np.linspace(0., my, ny+1)
x = mx*np.ones(ny+1)
plt.plot(x,y)
plt.show()

surf = fdfault.curve(ny+1, 'x', x, y)

p.set_block_surf((0,0,0), 1, surf)
p.set_block_surf((1,0,0), 0, surf)

# set initial fields

p.set_stress((-120., 68., 0., -100., 0., 0.))

# set interface type

p.set_iftype(0,'slipweak')

# set slip weakening parameters

p.add_pert(fdfault.swparam('constant', dc = 0.4, mus = 0.676, mud = 0.525),0)
p.add_pert(fdfault.swparam('boxcar', x0 = 20., dx = 20., mus = 10000.),0)
p.add_pert(fdfault.swparam('boxcar', x0 = 300., dx = 20., mus = 10000.),0)

# add load perturbations

p.add_load(fdfault.load('boxcar',0., 160., .5, 0., 0., 0., 13.6, 0.))

# add output unit

#p.add_output(fdfault.output('vxbody','vx',0, end_time-1, interval_time, 0, 1200, 2, 0, 640, 2, 0, 0, 1))
#p.add_output(fdfault.output('vybody','vy',0, end_time-1, interval_time, 0, 1200, 2, 0, 640, 2, 0, 0, 1))
p.add_output(fdfault.output('vfault','V',0, end_time-1, interval_time, 601, 601, 1, 0, 640, 2, 0, 0, 1))
#p.add_output(fdfault.output('snfault','Sn',0, end_time-1, interval_time, 601, 601, 1, 0, 640, 2, 0, 0, 1))
#p.add_output(fdfault.output('sfault','S',0, end_time-1, interval_time, 601, 601, 1, 0, 640, 2, 0, 0, 1))
#p.add_output(fdfault.output('sxxbody','sxx',0, end_time-1, interval_time, 0, 1200, 2, 0, 1600, 2, 0, 0, 1))
#p.add_output(fdfault.output('sxybody','sxy',0, end_time-1, interval_time, 0, 1200, 2, 0, 1600, 2, 0, 0, 1))
#p.add_output(fdfault.output('syybody','syy',0, end_time-1, interval_time, 0, 1200, 2, 0, 1600, 2, 0, 0, 1))
p.add_output(fdfault.output('vypt','vy', 0, end_time-1, 1, 374, 374, 1, 76, 76, 1, 0, 0, 1))

p.write_input()



