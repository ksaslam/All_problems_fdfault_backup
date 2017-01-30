import fdfault
import numpy as np

# create problem

p = fdfault.problem('tpv34_50m')

# set rk and fd order

p.set_rkorder(4)
p.set_sbporder(4)

# set time step info

refine =  4
nt = 6000

p.set_nt(nt)
p.set_dt(0.003334)
p.set_ninfo(500)

p.set_ndim(3)

# set number of blocks and coordinate information

nx = 300*refine+1
ny = 150*refine+1
nz = 150*refine+1

p.set_nblocks((1,2,1))
p.set_nx_block(([nx], [ny, ny], [nz]))

# set block dimensions

p.set_block_lx((0,0,0),(60.,30., 30.))
p.set_block_lx((0,1,0),(60.,30., 30.))

p.set_domain_xm((-30., -30., -30.))

# set block boundary conditions

p.set_bounds((0,0,0),['absorbing', 'absorbing', 'absorbing', 'none', 'absorbing', 'free'])
p.set_bounds((0,1,0),['absorbing', 'absorbing', 'none', 'absorbing', 'absorbing', 'free'])

# set material

cs = np.empty((nx, 2*ny, nz))
cp = np.empty((nx, 2*ny, nz))
rho = np.empty((nx, 2*ny, nz))

f = open('tpv34_matprops_small_50m.txt','r')

for i in range(nx):
    if i%10 == 0:
        print(i)
    for j in range(2*ny):
        for k in range(nz):
            a = f.readline()
            a = a.split()
            rho[i,j,k] = float(a[2])/1000.
            cp[i,j,k] = float(a[0])/1000.
            cs[i,j,k] = float(a[1])/1000.
            if (cp[i,j,k] <= 2.984 or cs[i,j,k] <= 1.4):
                rho[i,j,k] = 2.22034
                cp[i,j,k] = 2.984
                cs[i,j,k] = 1.4

mat = np.zeros((3, nx, 2*ny, nz))

mat[0,:,:,:] = rho
mat[1,:,:,:] = rho*(cp**2-2.*cs**2)
mat[2,:,:,:] = rho*cs**2

p.set_het_material(mat)

# set interface type

p.set_iftype(0,'slipweak')

# set slip weakening parameters

p.add_pert(fdfault.swparam('constant',0., 0., 0., 0., 0., 0.18, 0.58, 0.45))
p.add_pert(fdfault.swparam('boxcar',0., 0., 24., -24., 9., 0., 10000., 0., 10.))
p.add_pert(fdfault.swparam('boxcar',0., -24., 9., -7.5, 7.5, 0., 10000., 0., 10.))
p.add_pert(fdfault.swparam('boxcar',0., 24., 9., -7.5, 7.5, 0., 10000., 0., 10.))

# set cohesion to vary with depth

# set initial stress

zer = np.zeros((nx, nz))
c0 = np.zeros((nx, nz))

x = np.linspace(-30., 30., nx)
z = np.linspace(-30., 0., nz)

for i in range(nz):
    if -z[i] <= 2.4:
        c0[:,i] = 0.000425*(2400.+1000.*z[i])

p.set_paramfile(0, fdfault.swparamfile(nx, nz, zer, zer, zer, c0, zer, zer))

mu0 = 32.03812032

sn = np.zeros((nx, nz))
st = np.zeros((nx, nz))

for i in range(nx):
    for j in range(nz):
        r = np.sqrt(x[i]**2+(-z[j]-7.5)**2)
        sn[i,j] = -60.*mat[2,i,ny,j]/mu0
        if r <= 1.4:
            st[i,j] = 34.95*mat[2,i,ny,j]/mu0
        elif r <= 2.:
            st[i,j] = (30.+2.475*(1.+np.cos(np.pi*(r-1.4)/0.6)))*mat[2,i,ny,j]/mu0
        else:
            st[i,j] = 30.*mat[2,i,ny,j]/mu0

p.set_loadfile(0, fdfault.loadfile(nx, nz, sn, st, zer))

# add output units

# on fault stations

onfault = []
st1 = ['-120', '-060', '000', '060', '120']
dp1 = ['000', '010', '024', '050', '075', '100', '120']

for st in st1:
    for dp in dp1:
        onfault.append((st, dp))

fields = ['h-slip', 'h-slip-rate', 'h-shear-stress', 'v-slip', 'v-slip-rate', 'v-shear-stress', 'n-stress']
fname = ['Ux', 'Vx', 'Sx', 'Uz', 'Vz', 'Sz', 'Sn']

for station in onfault:
    xcoord = float(station[0])/10.
    zcoord = -float(station[1])/10.
    xpt, ypt, zpt = p.find_nearest_point((xcoord, 0., zcoord), known='y', knownloc=ny)
    for fld, fn in zip(fields, fname):
        p.add_output(fdfault.output('faultst'+station[0]+'dp'+station[1]+'-'+fld, fn, 0, nt, 1, xpt, xpt, 1,
                                    ypt, ypt, 1, zpt, zpt, 1))

# off fault stations

offfault = []

st1 = ['-150', '000', '150']
ac1 = ['-150', '150']
dp1 = ['000', '024']

for st in st1:
    for ac in ac1:
        for dp in dp1:
            offfault.append((st, ac, dp))

st1 = ['-200', '200']
ac1 = ['000']

for st in st1:
    for ac in ac1:
        for dp in dp1:
            offfault.append((st, ac, dp))

st1 = ['-200', '-100', '000', '100', '200']
ac1 = ['-090', '-030', '030', '090']

for st in st1:
    for ac in ac1:
        for dp in dp1:
            offfault.append((st, ac, dp))

fields = ['h-vel', 'v-vel', 'n-vel']
fname = ['vx', 'vz', 'vy']

for station in offfault:
    xcoord = float(station[0])/10.
    ycoord = float(station[1])/10.
    zcoord = -float(station[2])/10.
    xpt, ypt, zpt = p.find_nearest_point((xcoord, ycoord, zcoord))
    for fld, fn in zip(fields, fname):
        p.add_output(fdfault.output('body'+station[1]+'st'+station[0]+'dp'+station[2]+'-'+fld, fn, 0, nt, 1, xpt, xpt, 1,
                                    ypt, ypt, 1, zpt, zpt, 1))

#p.add_output(fdfault.output('vfault', 'V', 0, nt, 10, 0, nx-1, 1, ny, ny, 1, 0, nz-1, 1))

p.set_front_output(True)

p.write_input()
