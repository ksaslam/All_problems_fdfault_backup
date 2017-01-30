import fdfault
import numpy as np

def calc_diff(f, dx):
    df = (np.roll(f,-3)/60.-np.roll(f,-2)*3./20.+np.roll(f,-1)*3./4.-np.roll(f,1)*3./4.+np.roll(f,2)*3./20.-np.roll(f,3)/60.)/dx
    df[0] = (-21600./13649.*f[0]+81763./40947.*f[1]+131./27298.*f[2]-9143./13649.*f[3]+20539./81894.*f[4])/dx
    df[1] = (-81763./180195.*f[0]+7357./36039.*f[2]+30637./72078.*f[3]-2328./12013.*f[4]+6611./360390.*f[5])/dx
    df[2] = (-131./54220.*f[0]-7357./16266.*f[1]+645./2711.*f[3]+11237./32532.*f[4]-3487./27110.*f[5])/dx
    df[3] = (9143./53590.*f[0]-30637./64308.*f[1]-645./5359.*f[2]+13733./32154.*f[4]-67./4660.*f[5]+72./5359.*f[6])/dx
    df[4] = (-20539./236310.*f[0]+2328./7877.*f[1]-11237./47262.*f[2]-13733./23631.*f[3]+89387./118155.*f[5]-1296./7877.*f[6]+144./7877.*f[7])/dx
    df[5] = (-6611./262806.*f[1]+3487./43801.*f[2]+1541./87602.*f[3]-89387./131403.*f[4]+32400./43801.*f[6]-6480./43801.*f[7]+720./43801.*f[8])/dx
    df[-1] = -(-21600./13649.*f[-1]+81763./40947.*f[-2]+131./27298.*f[-3]-9143./13649.*f[-4]+20539./81894.*f[-5])/dx
    df[-2] = -(-81763./180195.*f[-1]+7357./36039.*f[-3]+30637./72078.*f[-4]-2328./12013.*f[-5]+6611./360390.*f[-6])/dx
    df[-3] = -(-131./54220.*f[-1]-7357./16266.*f[-2]+645./2711.*f[-4]+11237./32532.*f[-5]-3487./27110.*f[-6])/dx
    df[-4] = -(9143./53590.*f[-1]-30637./64308.*f[-2]-645./5359.*f[-3]+13733./32154.*f[-5]-67./4660.*f[-6]+72./5359.*f[-7])/dx
    df[-5] = -(-20539./236310.*f[-1]+2328./7877.*f[-2]-11237./47262.*f[-3]-13733./23631.*f[-4]+89387./118155.*f[-6]-1296./7877.*f[-7]+144./7877.*f[-8])/dx
    df[-6] = -(-6611./262806.*f[-2]+3487./43801.*f[-3]+1541./87602.*f[-4]-89387./131403.*f[-5]+32400./43801.*f[-7]-6480./43801.*f[-8]+720./43801.*f[-9])/dx

    return df

# the refine parameter can be used to increase the resolution of the simulation
# the problem will run with refine = 1, but it is better to use refine = 2
# if using refine = 2, probably best to run on the hpc (for me it took about 2 hours on 32 processors)

refine = 1

nt = 20000*refine+1
nbx = 750*refine+1
nby5 = 100*refine+1
nby4 = 130*refine+1
nby3 = 400*refine+1
nby2 = 500*refine+1
nby1 = 380*refine+1

p = fdfault.problem('lushanMult')

# set rk and fd order

p.set_rkorder(4)
p.set_sbporder(4)

# set time step info

p.set_nt(nt)
p.set_cfl(0.3)
p.set_ninfo(100*refine)

# set number of blocks and coordinate information

p.set_nblocks((2,5,1))
p.set_nx_block(([nbx, nbx], [nby1, nby2, nby3, nby4, nby5], [1]))

# set block dimensions

p.set_block_lx((0,0,0),(30.,17.))
p.set_block_lx((1,0,0),(70.,17.))
p.set_block_lx((0,1,0),(30.,21.))
p.set_block_lx((1,1,0),(70.,21.))
p.set_block_lx((0,2,0),(30.,14.))
p.set_block_lx((1,2,0),(70.,14.))
p.set_block_lx((0,3,0),(46.7,5.))
p.set_block_lx((1,3,0),(53.3,5.))
p.set_block_lx((0,4,0),(52.7,3.))
p.set_block_lx((1,4,0),(47.3,3.))

# set block boundary conditions

p.set_bounds((0,0,0),['absorbing', 'none', 'absorbing', 'none'])
p.set_bounds((1,0,0),['none', 'absorbing', 'absorbing', 'none'])
p.set_bounds((0,1,0),['absorbing', 'none', 'none', 'none'])
p.set_bounds((1,1,0),['none', 'absorbing', 'none', 'none'])
p.set_bounds((0,2,0),['absorbing', 'none', 'none', 'none'])
p.set_bounds((1,2,0),['none', 'absorbing', 'none', 'none'])
p.set_bounds((0,3,0),['absorbing', 'none', 'none', 'none'])
p.set_bounds((1,3,0),['none', 'absorbing', 'none', 'none'])
p.set_bounds((0,4,0),['absorbing', 'none', 'none', 'free'])
p.set_bounds((1,4,0),['none', 'absorbing', 'none', 'free'])

# set block surfaces

# layer 3
x = np.linspace(0., 46.7, nbx)
y = 52.*np.ones(nbx)
nx = np.zeros(nbx)
ny = np.ones(nbx)

#surf1 = fdfault.curve(nbx, 'y', x, y, nx, ny)

p.set_block_surf((0,2,0), 3, surf1)
p.set_block_surf((0,3,0), 2, surf1)

x = np.linspace(46.7, 100, nbx)
y = 52.*np.ones(nbx)
nx = np.zeros(nbx)
ny = np.ones(nbx)

#surf2 = fdfault.curve(nbx, 'y', x, y, nx, ny)

p.set_block_surf((1,2,0), 3, surf2)
p.set_block_surf((1,3,0), 2, surf2)

x = np.linspace(30., 46.7, nby3)
y = np.linspace(38., 52., nby3)
m = np.ones(nby3)*(x[-1]-x[0])/(y[-1]-y[0])
nx = 1./np.sqrt(1.+m**2)
ny = -m/np.sqrt(1.+m**2)

#surf3 = fdfault.curve(nby3,'x',x, y, nx, ny)

p.set_block_surf((0,2,0), 1, surf3)
p.set_block_surf((1,2,0), 0, surf3)

# layer 2

x = np.linspace(0., 52.7, nbx)
y = 57.*np.ones(nbx)
nx = np.zeros(nbx)
ny = np.ones(nbx)

#surf4 = fdfault.curve(nbx, 'y', x, y, nx, ny)

p.set_block_surf((0,3,0), 3, surf4)
p.set_block_surf((0,4,0), 2, surf4)

x = np.linspace(52.7, 100., nbx)
y = 57.*np.ones(nbx)
nx = np.zeros(nbx)
ny = np.ones(nbx)

#surf5 = fdfault.curve(nbx, 'y', x, y, nx, ny)

p.set_block_surf((1,3,0), 3, surf5)
p.set_block_surf((1,4,0), 2, surf5)

x = np.linspace(46.7, 52.7, nby4)
y = np.linspace(52., 57., nby4)
m = np.ones(nby4)*(x[-1]-x[0])/(y[-1]-y[0])
nx = 1./np.sqrt(1.+m**2)
ny = -m/np.sqrt(1.+m**2)

#surf6 = fdfault.curve(nby4,'x',x, y, nx, ny)

p.set_block_surf((0,3,0), 1, surf6)
p.set_block_surf((1,3,0), 0, surf6)

# set topography

x = np.linspace(0,52.7, nbx)
y = 64-4./(1+np.exp(-0.2*(x-52)))
m = calc_diff(x,52.7/(nbx-1))
ny = -m/np.sqrt(1.+m**2)
nx = 1./np.sqrt(1.+m**2)

#surf7 = fdfault.curve(nbx, 'x', x, y, nx, ny)

p.set_block_surf((0,4,0), 3, surf7)

x = np.linspace(52.7,100, nbx)
y = 64-4./(1+np.exp(-0.2*(x-52)))
m = calc_diff(x,47.3/(nbx-1))
ny = -m/np.sqrt(1.+m**2)
nx = 1./np.sqrt(1.+m**2)

#surf8 = fdfault.curve(nbx, 'x', x, y, nx, ny)

p.set_block_surf((1,4,0), 3, surf8)

# set interface types

p.set_iftype(2,'slipweak')
p.set_iftype(3,'slipweak')

# set interface surface

p.set_iface_surf(2,surf3)
p.set_iface_surf(3,surf6)

# set material
newMaterial = fdfault.material("elastic",3.38,85.6,67.53)
p.set_material(newMaterial, (0,0,0))
p.set_material(newMaterial, (1,0,0))

newMaterial = fdfault.material("elastic",2.9,43,46)
p.set_material(newMaterial, (0,1,0))
p.set_material(newMaterial, (1,1,0))

newMaterial = fdfault.material("elastic",2.75,31.,34.66)
p.set_material(newMaterial, (0,2,0))
p.set_material(newMaterial, (1,2,0))

newMaterial = fdfault.material("elastic",2.7,28.4,31.21)
p.set_material(newMaterial, (0,3,0))
p.set_material(newMaterial, (1,3,0))
p.set_material(newMaterial, (0,4,0))

newMaterial = fdfault.material("elastic",2.55,19,20.86)
p.set_material(newMaterial, (1,4,0))
# p.set_material(newMaterial, (0,4,0))

# set slip weakening parameters

p.set_params(1.2, 0.677, 0.525,2)
p.set_params(1.2, 0.677, 0.525,3)

# add load perturbations

p.add_load(fdfault.load('constant',0., 0., 0., 0., 0., -120., 64.5, 0.),2)
p.add_load(fdfault.load('constant',0., 0., 0., 0., 0., -120., 64.5, 0.),3)
p.add_load(fdfault.load('boxcar',0., 47, 1.05, 0., 0., 0., 17.2, 0.),2)

# add output unit

p.add_output(fdfault.output('vxbody','vx',0, nt-1, 25*refine, 0, 2*nbx-1, 4*refine, 0, (nby1+nby2+nby3+nby4+nby5)-4, 4*refine, 0, 0, 1))
p.add_output(fdfault.output('vybody','vy',0, nt-1, 25*refine, 0, 2*nbx-1, 4*refine, 0, (nby1+nby2+nby3+nby4+nby5)-4, 4*refine, 0, 0, 1))
p.add_output(fdfault.output('vfault','V',0, nt-1, 25*refine, nbx, nbx, 1, (nby1+nby2), (nby1+nby2+nby3-1), 2*refine, 0, 0, 1))

p.write_input()
