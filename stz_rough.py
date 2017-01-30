import fdfault
import numpy as np
import seistools.rough
# create problem

p = fdfault.problem('stz_rough')

# set rk and fd order

p.set_rkorder(4)
p.set_sbporder(4)

# set time step info

end_time= 500
interval_time=20
p.set_nt(end_time)
p.set_cfl(0.3)
p.set_ninfo(interval_time)

# set number of blocks and coordinate information

p.set_nblocks((1,2,1))
p.set_nx_block(([1601], [801, 801], [1]))

# set block dimensions

p.set_block_lx((0,0,0),(40.,20.))
p.set_block_lx((0,1,0),(40.,20.))

# set block boundary conditions

p.set_bounds((0,0,0),['absorbing', 'absorbing', 'absorbing', 'none'])
p.set_bounds((0,1,0),['absorbing', 'absorbing', 'none', 'absorbing'])

# set block surface
# need to look at it carefully 

x = np.linspace(0., 40., 1601)
y = 20.*np.ones(1601)+seistools.rough.generate_profile(1601, 40, 10**-2, 8, h = 1., seed=1000)

# Saving the output for the normal vector calculation
np.savetxt('x.out', x, delimiter=',') 
np.savetxt('y.out', y, delimiter=',')


surf = fdfault.curve(1601, 'y', x, y)

p.set_block_surf((0,0,0), 3, surf)
p.set_block_surf((0,1,0), 2, surf)

# set initial fields

p.set_stress((-100., 60.0, 0., -120., 0., 0.))

# set interface type

p.set_iftype(0,'stz')

# set stz parameters

p.add_pert(fdfault.stzparam('constant', v0=1.e-6, f0 = 130., a = 0.0037, muy = 0.3, c0 = 500., R = 0., beta = 0., chiw = 0.8, v1 = 1000.), 0)

# set initial state

p.set_state(0, 0.025)

# add load perturbations

p.add_load(fdfault.load('boxcar',0., 20., 1.5, 0., 0., 0., 9.1, 0.))
p.add_pert(fdfault.stzparam('boxcar', x0 = 36., dx = 1., muy = 100.),0)
p.add_pert(fdfault.stzparam('boxcar', x0 = 2., dx = 1., muy = 100.),0)


# --------------loading stresses through a file
# sn = -120.*np.ones((1601,1))
# s2 = 72.5*np.ones((1601,1))


#sn = np.zeros((1601,1))
#s2 = np.zeros((1601,1))
#s3 = np.zeros((1601,1))
#nor= np.loadtxt("sn_stress.out")
#hor= np.loadtxt("s2_mod_stress.out")

#s2[:,0]= hor[:]
#sn[:,0]= nor[:]

#s2[np.abs(x-20.) <= 1.5] += 5
# #s2[np.abs(x-20.) <= 1.5] += 9.1

#p.set_loadfile(0, fdfault.loadfile(1601, 1, sn, s2, s3))

# -------------------------------------------


# add output unit

p.add_output(fdfault.output('vfault','V',0, end_time-1, interval_time, 0, 1600, 1, 801, 801, 1, 0, 0, 1))
p.add_output(fdfault.output('sfault','S',0, end_time-1, interval_time, 0, 1600, 1, 801, 801, 1, 0, 0, 1))
p.add_output(fdfault.output('snfault','Sn',0, end_time-1, interval_time, 0, 1600, 1, 801, 801, 1, 0, 0, 1))
p.add_output(fdfault.output('chifault','state',0, end_time-1, interval_time, 0, 1600, 1, 801, 801, 1, 0, 0, 1))
p.add_output(fdfault.output('vxbody','vx',0, end_time-1, interval_time, 0, 1600, 2, 0, 1600, 2, 0, 0, 1))
p.add_output(fdfault.output('vybody','vy',0, end_time-1, interval_time, 0, 1600, 2, 0, 1600, 2, 0, 0, 1))
p.add_output(fdfault.output('sxxbody','sxx',0, end_time-1, interval_time, 0, 1600, 2, 0, 1600, 2, 0, 0, 1))
p.add_output(fdfault.output('sxybody','sxy',0, end_time-1, interval_time, 0, 1600, 2, 0, 1600, 2, 0, 0, 1))
p.add_output(fdfault.output('syybody','syy',0, end_time-1, interval_time, 0, 1600, 2, 0, 1600, 2, 0, 0, 1))

p.write_input()
