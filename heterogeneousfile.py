import fdfault
import numpy as np

# create problem

p = fdfault.problem('heterogeneousfile')

# set rk and fd order

p.set_rkorder(4)
p.set_sbporder(4)

# grid info

nt = 11
nx = 601
ny = 1601

# set time step info
interval_time=5
p.set_nt(nt)
p.set_cfl(0.3)
p.set_ninfo(interval_time)

# set number of blocks and coordinate information

p.set_nblocks((2,1,1))
p.set_nx_block(([nx, nx], [ny], [1]))

# set block dimensions

lx = 12.
ly = 32.

p.set_block_lx((0,0,0),(lx, ly))
p.set_block_lx((1,0,0),(lx, ly))

# set block boundary conditions

p.set_bounds((0,0,0),['absorbing', 'none', 'absorbing', 'absorbing'])
p.set_bounds((1,0,0),['none', 'absorbing', 'absorbing', 'absorbing'])

# set initial stress
#p.set_stress((-120., 60., 0., -100., 0., 0.))
# set interface type

p.set_iftype(0,'slipweak')

# set slip weakening parameters

y = np.linspace(0., ly, ny)

dc = np.ones((ny,1))*0.4
mus = np.ones((ny,1))*0.677
mus[np.abs(y-16.) >= 12.] = 10000.
mud = np.ones((ny,1))*0.525
zer = np.zeros((ny,1))

p.set_paramfile(0, fdfault.swparamfile(ny, 1, dc, mus, mud, zer, zer, zer))

# add load perturbation

sn = -120.*np.ones((ny,1))
s2 = 70.*np.ones((ny,1))
s3 = np.zeros((ny,1))

s2[np.abs(y-16.) <= 1.5] += 11.6

p.set_loadfile(0, fdfault.loadfile(ny, 1, sn, s2, s3))

# add output unit

p.add_output(fdfault.output('vxbody','vx',0, nt, interval_time, 0, 2*nx-1, 2, 0, ny-1, 2, 0, 0, 1))
p.add_output(fdfault.output('vybody','vy',0, nt, interval_time, 0, 2*nx-1, 2, 0, ny-1, 2, 0, 0, 1))
p.add_output(fdfault.output('vfault','V',0, nt, interval_time, nx, nx, 1, 0, ny-1, 1, 0, 0, 1))
p.add_output(fdfault.output('snfault','Sn',0, nt, interval_time, nx, nx, 1, 0, ny-1, 1, 0, 0, 1))
p.add_output(fdfault.output('sfault','S',0, nt, interval_time, nx, nx, 1, 0, ny-1, 1, 0, 0, 1))
p.add_output(fdfault.output('sxxbody','sxx',0, nt, interval_time, 0, 2*nx-1, 2, 0, ny-1, 2, 0, 0, 1))
p.add_output(fdfault.output('sxybody','sxy',0, nt, interval_time, 0, 2*nx-1, 2, 0, ny-1, 2, 0, 0, 1))
p.add_output(fdfault.output('syybody','syy',0, nt, interval_time, 0, 2*nx-1, 2, 0, ny-1, 2, 0, 0, 1))

p.write_input()
