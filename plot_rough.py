from rough import generate_profile
import matplotlib.pyplot as plt
import numpy as np

y = np.linspace(0., 32., 1601)
y1,k1,amp1=generate_profile(1601, 32, 10**-2,20, h = 1, seed=None)
y2,k2,amp2=generate_profile(1601, 32, 10**-3,20, h = 1, seed=None)

x1 = 12.*np.ones(1601)+ y1
x2= 12.*np.ones(1601)+ y2
#plt.logl12.*np.ones(1601)+ y2og(k1, (amp1)**2 )

plt.loglog(k2, (amp2)**2,linewidth=3.0 )

plt.xticks([10**-1,10**-.5, 1, 5, 10,10**.5,10**1], fontsize = 26)
plt.yticks([10**-3,10**-2,10**-1,1,10,10**1,10**2, 10**3], fontsize = 26)
plt.ylabel('Power Spectral Density',fontsize=27, color='black')
plt.xlabel('Wave number',fontsize=26,color='black')
plt.axis([10**-1, 2*10**1, 10**-3, 3*10**3])
plt.title('Power spectral density plot ',fontsize=26,color='black')
plt.grid()
#plt.savefig('Power_spectrum.pdf')
plt.show()
plt.plot(y,x1,linewidth=3.0, label='RMS height/wavelength=0.01')
plt.xticks([5,10,15,20,25,30], fontsize = 26)
plt.yticks([7,9,11,13,15], fontsize = 26)
plt.plot(y,x2,linewidth=3.0, label='RMS height/wavelength=0.001')
plt.axis([0, 32, 7, 16])
plt.xlabel('Position along strike (km)',fontsize=26, color='black')
plt.ylabel('Position across fault (km)',fontsize=26,color='black')
plt.title('Fault profiles',fontsize=26,color='black')
plt.legend( loc='upper right')


plt.show()
#plt.savefig('together_RMS.pdf')


#plt.plot(y,x1,linewidth=3.0)

#plt.axis([0, 32, 8, 16])
#plt.xlabel('Position along strike (km)',fontsize=20, color='black')
#plt.ylabel('Position across fault (km)',fontsize=20,color='black')
#plt.title('Fault profiles (RMS height to wavelength ratio =$10**{-2}$) ',fontsize=16,color='black')

#plt.show()


#plt.plot(y,x2,linewidth=2.0)

#plt.axis([0, 32, 11, 13])
#plt.xlabel('Position along strike (km)',fontsize=20, color='black')
#plt.ylabel('Position across fault(km)',fontsize=20,color='black')
#plt.title('Fault profiles (RMS height to wavelength ratio =$10**{-3}$) ',fontsize=20,color='black')

#plt.show()