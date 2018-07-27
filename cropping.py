#################################################################################
#Python script using astropy to load and crop  a certain portion of a FITS image#
# while preserving the WCS
#Behnam Javanmardi Dec 2017                                                   #
#################################################################################
from astropy.io import fits
from astropy.nddata.utils import Cutout2D
import matplotlib.pyplot as plt
from astropy import wcs
import numpy as np

size=300

x_cen, y_cen=np.genfromtxt("x_y.txt",unpack=True)



data=fits.open('NGC.fits')
header=data[0].header
w = wcs.WCS(header)
scidata=data[0].data

for i in range(len(x_cen)):
	cropped=Cutout2D(scidata, (x_cen[i],y_cen[i]), size=size, wcs=w, mode='trim')
	hdu=fits.PrimaryHDU(data=cropped.data, header=cropped.wcs.to_header())
	if x_cen[i] < size/2.0 or y_cen[i] < size/2.0 or x_cen[i] > scidata.shape[1]-size/2.0 or y_cen[i] > scidata.shape[0]-size/2.0:
		name='dw'+str(i+1)+'_edge.fits'
		hdu.writeto(name, overwrite=True)
	name='dw'+str(i+1)+'.fits'
	hdu.writeto(name, overwrite=True)


