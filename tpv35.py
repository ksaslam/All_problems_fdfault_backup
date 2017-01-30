import fdfault
import numpy as np

# create problem

p = fdfault.problem('tpv35')

# set rk and fd order

p.set_rkorder(4)
p.set_sbporder(4)

# set time step info

nt = 3028

p.set_nt(nt)
p.set_dt(0.004294)
p.set_ninfo(500)

p.set_ndim(3)

# set number of blocks and coordinate information

refine = 1

nx = 400*refine+1   # 400 *100 
ny1 = 100*refine+1
ny2 = 100*refine+1

# total depth is 16 km
nz0_1 = 10*refine+1
nz0_2=  10*refine+1
nz0_3=  10*refine+1
nz0_4=  5*refine+1
nz0_5= 23*refine+1
nz0_6= 83*refine+1
nz0_7= 30*refine+1
nz0_8= 33*refine+1

nz1_9= temp*refine+1
#
nz1_1 = 10*refine+1
nz1_2=  8*refine+1
nz1_3=  3*refine+1
nz1_4=  13*refine+1
nz1_5= 5*refine+1
nz1_6= 44*refine+1
nz1_7= 44*refine+1
nz1_8= 48*refine+1
nz1_9= 28*refine+1

nz1_10= temp*refine+1


p.set_block_lx((0,0,0),(4.,10.,1))
p.set_block_lx((0,0,1),(40.,10.,1.))
p.set_block_lx((0,0,2),(40.,10.,1.))
p.set_block_lx((0,0,3),(40.,10.,.5))
p.set_block_lx((0,0,4),(40.,10.,2.3))
p.set_block_lx((0,0,5),(40.,10.,8.3))
p.set_block_lx((0,0,6),(40.,10.,3.))
p.set_block_lx((0,0,7),(40.,10.,3.3))
p.set_block_lx((0,0,7),(40.,10.,.1))


p.set_block_lx((0,1,0),(40.,20.,1))
p.set_block_lx((0,2,0),(40.,20.,.8))
p.set_block_lx((0,3,0),(40.,20.,.3))
p.set_block_lx((0,3,0),(40.,20.,1.3))
p.set_block_lx((0,3,0),(40.,20.,.5))
p.set_block_lx((0,3,0),(40.,20.,4.4))
p.set_block_lx((0,3,0),(40.,20.,4.4))
p.set_block_lx((0,3,0),(40.,20.,4.8))
p.set_block_lx((0,3,0),(40.,20.,2.8))
p.set_block_lx((0,3,0),(40.,20.,.2))

