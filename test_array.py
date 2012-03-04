import numpy
import sys, math
sys.path.append('L:/software/apparatus3/seq/utilspy')
sys.path.append('L:/software/apparatus3/convert')

#~ from wfm import OdtpowConvert

import matplotlib.pyplot as plt

volt_a=numpy.array([])
phys_a=numpy.array([])

#~ for phys in numpy.arange(0,10.0,0.1):
    #~ volt_a=numpy.append(volt_a,OdtpowConvert(phys))
    #~ phys_a=numpy.append(phys_a,phys)
    
data = numpy.loadtxt('PD_AOM.dat')


data=data[:5,:]
print data

l=[]

for point in data:
    print point
    if point[0] > -7.52:
        print 'gotit'
        l.append([point[0],point[1]])


print numpy.asarray(l)