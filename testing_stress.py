import fdfault
import numpy as np
import matplotlib.pyplot as plt
import seistools.rough
# create problem

p = fdfault.problem('stress_test')

# set rk and fd order

p.set_rkorder(4)
p.set_sbporder(4)

# set time step info

end_time= 201
interval_time=20
p.set_nt(end_time)
p.set_cfl(0.3)
p.set_ninfo(interval_time)

# set material type 
p.set_mattype("elastic")

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
y = 16.*np.ones(1201)
#y = 16.*np.ones(1201)+seistools.rough.generate_profile(1201, 24, 10**-2, 8, h = 1, seed=None)
np.savetxt('../data/y_fault.out', y, delimiter=',') 

plt.plot(x,y)
plt.axis([0, 20, 13, 19])
plt.show()

surf = fdfault.curve(1201, 'y', x, y)

p.set_block_surf((0,0,0), 3, surf)
p.set_block_surf((0,1,0), 2, surf)

# set initial fields

#p.set_stress((sxx, sxy., 0., syy., 0., 0.))   # for horizental fault, syx is shear stress and syy is normal stress.
p.set_stress((-120., 70., 0., -100., 0., 0.))

# set interface type



p.set_iftype(0,'slipweak')

# set slip weakening parameters

p.add_pert(fdfault.swparam('constant', dc = 0.4, mus = 0.676, mud = 0.325),0)
p.add_pert(fdfault.swparam('boxcar', x0 = 3., dx = 1., mus = 10000.),0)
p.add_pert(fdfault.swparam('boxcar', x0 = 18., dx = 1., mus = 10000.),0)



#p.set_iftype(0,'stz')
#p.set_state(0, 100)
#p.add_pert(fdfault.stzparam('constant', 0, 0, 0, 0, 0, 0.0005, 0., 0.01, 0.1, 1000, 4., 0.4, 10**20,  100.0 ),0)
#p.add_pert(fdfault.stzparam('constant',v0 = 0.0005, f0 = 0., a = 10.**-2, muy = 0.1, c0 = 10**3, R = 4., beta = 0.4, chiw = 10**20, v1 = 100.0),0)
#p.add_pert(fdfault.stzparam('boxcar', y0 = 3., dy = 1., muy = 100.),0)
#p.add_pert(fdfault.stzparam('boxcar', y0 = 21., dy = 2., muy = 100.),0)

# add load perturbations
# parameters for the load pertubation
#t0 = 0., x0 = 0., dx = 0., y0 = 0., dy = 0., dc = 0., mus = 0., mud =0.)
p.add_load(fdfault.load('boxcar',0., 7., 2, 0., 0., 0., 5.6, 0.))
#p.add_load(fdfault.load('boxcar',0., 7., 2, 0., 0., 0., 15.6, 0.))
#p.add_load(fdfault.load('boxcar', t0 = 0., x0 = 0., dx = 0., y0 = 0., dy = 0., sn = 0., s2 = 0., s3 =0.):


# add output unit

p.add_output(fdfault.output('vxbody','vx',0, end_time-1, interval_time, 0, 1200, 2, 0, 1600, 2, 0, 0, 1))
p.add_output(fdfault.output('vybody','vy',0, end_time-1, interval_time, 0, 1200, 2, 0, 1600, 2, 0, 0, 1))
p.add_output(fdfault.output('vfault','V',0, end_time-1, interval_time, 0, 1200, 2, 801, 801, 1, 0, 0, 1))
#p.add_output(fdfault.output('ufault','U',0, end_time-1, interval_time, 0, 1200, 2, 801, 801, 1, 0, 0, 1))
#p.add_output(fdfault.output('sfault','S',0, end_time-1, interval_time, 0, 1200, 2, 801, 801, 1, 0, 0, 1))
p.add_output(fdfault.output('sxxbody','sxx',0, end_time-1, interval_time, 0, 1200, 2, 0, 1600, 2, 0, 0, 1))
#p.add_output(fdfault.output('lambdabody','lambda',0, end_time-1, interval_time, 0, 1200, 2, 0, 1600, 2, 0, 0, 1))
#p.add_output(fdfault.output('gammabody','gammap',0, end_time-1, interval_time, 0, 1200, 2, 0, 1600, 2, 0, 0, 1))
p.add_output(fdfault.output('sxybody','sxy',0, end_time-1, interval_time, 0, 1200, 2, 0, 1600, 2, 0, 0, 1))
p.add_output(fdfault.output('syybody','syy',0, end_time-1, interval_time, 0, 1200, 2, 0, 1600, 2, 0, 0, 1))

p.write_input()
