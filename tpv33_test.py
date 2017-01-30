import fdfault
import numpy as np

# create problem

p = fdfault.problem('tpv33')

# set rk and fd order

p.set_rkorder(4)
p.set_sbporder(4)

# set time step info

nt = 10

p.set_nt(nt)
p.set_dt(0.004294)
p.set_ninfo(5)

p.set_ndim(3)

# set number of blocks and coordinate information

refine = 1

nx = 1000*refine+1

ny2 = 384*refine+1
nz = 200*refine+1

p.set_nblocks((1,2,2))
p.set_nx_block(([nx], [ny2, ny2], [nz, nz]))

# set block dimensions

p.set_block_lx((0,0,0),(50., 19.2, 10.))

p.set_block_lx((0,1,0),(50., 19.2, 10.))

p.set_block_lx((0,0,1),(50., 19.2, 10.))

p.set_block_lx((0,1,1),(50., 19.2, 10.))

p.set_domain_xm((-25., -20., -20.))

# set block boundary conditions

p.set_bounds((0,0,0),['absorbing', 'absorbing', 'absorbing', 'none', 'absorbing', 'none'])
p.set_bounds((0,1,0),['absorbing', 'absorbing', 'none', 'absorbing', 'absorbing', 'none'])

p.set_bounds((0,1,0),['absorbing', 'absorbing', 'none', 'absorbing', 'absorbing', 'free'])
p.set_bounds((0,1,0),['absorbing', 'absorbing', 'none', 'absorbing', 'absorbing', 'free'])


# set side surfaces

##B = -1.323
##
##xi = np.linspace(0., 1., ny2)
##y = np.tanh(B*xi)/np.tanh(B)*9.2-10.
##z = np.linspace(-14., 0., nz)
##
##xgrid = np.ones((ny2, nz))*-16.
##ygrid, zgrid = np.meshgrid(y, z, indexing='ij')
##
##surf = fdfault.surface(ny2, nz, 'x', xgrid, ygrid, zgrid)
##
##p.set_block_surf((0,0,0), 0, surf)
##
##xgrid = np.ones((ny2, nz))*16.
##
##surf = fdfault.surface(ny2, nz, 'x', xgrid, ygrid, zgrid)
##
##p.set_block_surf((0,0,0), 1, surf)
##
##x = np.linspace(-16., 16., nx)
##zgrid = -14.*np.ones((nx, ny2))
##xgrid, ygrid = np.meshgrid(x, y, indexing='ij')
##
##surf = fdfault.surface(nx, ny2, 'z', xgrid, ygrid, zgrid)
##
##p.set_block_surf((0,0,0), 4, surf)
##
##zgrid = np.zeros((nx, ny2))
##
##surf = fdfault.surface(nx, ny2, 'z', xgrid, ygrid, zgrid)
##
##p.set_block_surf((0,0,0), 5, surf)
##
##B = -B
##
##y = (1.+np.tanh(B*(xi-1.))/np.tanh(B))*9.2+0.8
##z = np.linspace(-14., 0., nz)
##
##xgrid = np.ones((ny2, nz))*-16.
##ygrid, zgrid = np.meshgrid(y, z, indexing='ij')
##
##surf = fdfault.surface(ny2, nz, 'x', xgrid, ygrid, zgrid)
##
##p.set_block_surf((0,3,0), 0, surf)
##
##xgrid = np.ones((ny2, nz))*16.
##
##surf = fdfault.surface(ny2, nz, 'x', xgrid, ygrid, zgrid)
##
##p.set_block_surf((0,3,0), 1, surf)
##
##x = np.linspace(-16., 16., nx)
##zgrid = -14.*np.ones((nx, ny2))
##xgrid, ygrid = np.meshgrid(x, y, indexing='ij')
##
##surf = fdfault.surface(nx, ny2, 'z', xgrid, ygrid, zgrid)
##
##p.set_block_surf((0,3,0), 4, surf)
##
##zgrid = np.zeros((nx, ny2))
##
##surf = fdfault.surface(nx, ny2, 'z', xgrid, ygrid, zgrid)
##
##p.set_block_surf((0,3,0), 5, surf)

# set material

rho = 2.67

cs = 3.248
cp = 5.626

p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,0,0))

cs = 2.165
cp = 3.75

p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,1,0))
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,1,1))
p.set_material(fdfault.material('elastic', rho, rho*(cp**2-2.*cs**2), rho*cs**2), (0,0,1))


# turn on artificial dissipation

#p.set_cdiss(0.1)

# set interface type

p.set_iftype(0,'slipweak')

# set slip weakening parameters

p.add_pert(fdfault.swparam('constant',0., 0., 0., 0., 0., 0.18, 0.55, 0.45),0)


#data = np.loadtxt("y_fault.out")
# create load file

# sigman = -60.*np.ones((nx, nz))
# tauh = np.zeros((nx,nz))
# tauv = np.zeros((nx,nz))

# x = np.linspace(-25., 25., nx)
# y = np.linspace(20., 0., nz)

# for i in range(nx):
#     for j in range(nz):
#         if x[i] < -9.8:
#             Rx = (-x[i]-9.8)/10.
#         elif x[i] > 1.1:
#             Rx = (x[i]-1.1)/10.
#         else:
#             Rx = 0.
#         if y[j] < 2.3:
#             Ry = (-y[j]+2.3)/10.
#         elif y[j] > 8.:
#             Ry = (y[j]-8.)/10.
#         else:
#             Ry = 0.
#         Rt = np.minimum(1., np.sqrt(Rx**2+Ry**2))
#         r = np.sqrt((x[i]+6.)**2+(y[j]-6.)**2)
#         if r <= 0.55:
#             tnucl = 3.15
#         elif r <= 0.8:
#             tnucl = 1.575*(1.+np.cos(np.pi*(r-0.55)/0.25))
#         else:
#             tnucl = 0.
#         tauh[i,j] = 30.*(1.-Rt)+tnucl

# p.set_loadfile(1, fdfault.loadfile(nx, nz, sigman, tauh, tauv))

#add output units

#on fault stations

onfault = []
st1 = ['-100', '-080', '-060', '-040', '-020', '000', '020']
dp1 = ['120', '040', '060', '080']

for st in st1:
    for dp in dp1:
        onfault.append((st, dp))

fields = ['h-slip', 'h-slip-rate', 'h-shear-stress', 'v-slip', 'v-slip-rate', 'v-shear-stress', 'n-stress']
fname = ['Ux', 'Vx', 'Sx', 'Uz', 'Vz', 'Sz', 'Sn']

for station in onfault:
    xcoord = float(station[0])/10.
    zcoord = -float(station[1])/10.
    xpt, ypt, zpt = p.find_nearest_point((xcoord, 0., zcoord), known='y', knownloc=ny2)
    for fld, fn in zip(fields, fname):
        p.add_output(fdfault.output('faultst'+station[0]+'dp'+station[1]+'-'+fld, fn, 0, nt, 1, xpt, xpt, 1, ypt, ypt, 1, zpt, zpt, 1))

# # off fault stations

# offfault = []

# st1 = ['-120', '-040', '040']
# ac1 = ['-100', '-050', '050', '100']
# dp1 = ['000']

# for st in st1:
#     for ac in ac1:
#         for dp in dp1:
#             offfault.append((st, ac, dp))

# st1 = ['-060', '040', '080', '120']
# ac1 = ['-016', '-012', '-008', '-004', '000', '004', '008', '012', '016']

# for st in st1:
#     for ac in ac1:
#         for dp in dp1:
#             offfault.append((st, ac, dp))

# st1 = ['040', '080', '120']
# ac1 = ['-016', '-012', '-008', '-004', '000', '004', '008', '012', '016']
# dp1 = ['060']

# for st in st1:
#     for ac in ac1:
#         for dp in dp1:
#             offfault.append((st, ac, dp))

# st1 = ['000']
# ac1 = ['-016', '-012', '-008', '-004', '-001', '001', '004', '008', '012', '016']

# for st in st1:
#     for ac in ac1:
#         for dp in dp1:
#             offfault.append((st, ac, dp))

# fields = ['h-vel', 'v-vel', 'n-vel']
# fname = ['vx', 'vz', 'vy']

# for station in offfault:
#     xcoord = float(station[0])/10.
#     ycoord = float(station[1])/10.
#     zcoord = -float(station[2])/10.
#     xpt, ypt, zpt = p.find_nearest_point((xcoord, ycoord, zcoord))
#     for fld, fn in zip(fields, fname):
#         p.add_output(fdfault.output('body'+station[1]+'st'+station[0]+'dp'+station[2]+'-'+fld, fn, 0, nt, 1, xpt, xpt, 1,
#                                     ypt, ypt, 1, zpt, zpt, 1))

# #p.add_output(fdfault.output('vfault','V', 0, nt, 10, 0, nx-1, 2, ny1+ny2, ny1+ny2, 1, 0, nz-1, 2))

# p.set_front_output(True)

p.write_input()
