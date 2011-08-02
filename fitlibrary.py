from scipy import optimize
import numpy
import matplotlib.pyplot as plt

def gaus1d(a0,data):
    #print a0
    p0=(a0[0],a0[1],a0[2],a0[3])
    datax=data[:,0]
    datay=data[:,1]
    # Target function
    fitfunc = lambda p, x: p[0]*numpy.exp(-((x-p[1])/p[2])**2)+p[3]
    # Error function
    errfunc = lambda p, x, dat: fitfunc(p,x)-dat
    # Fit
    p1,success = optimize.leastsq(errfunc,p0[:],args=(datax,datay))
    p1 = numpy.append(p1,[0.0]).reshape(5,1)
    return p1
    
def gaus1d_fun( a, datax):
    p=(a[0],a[1],a[2],a[3])
    ay=numpy.array([])
    datax = numpy.sort(datax)
    ax=numpy.linspace(numpy.min(datax), numpy.max(datax), 100)
    for x in ax:
        ay=numpy.append(ay, p[0]*numpy.exp(-((x-p[1])/p[2])**2)+p[3])
    return ax,ay
    

def sine(a0,data):
    p0=(a0[0],a0[1],a0[2],a0[3])
    datax=data[:,0]
    datay=data[:,1]
    # Target function
    fitfunc = lambda p, x: p[0]*numpy.sin( p[1]*x-p[2] ) + p[3]
    # Error function
    errfunc = lambda p, x, dat: fitfunc(p,x)-dat
    # Fit
    p1,success = optimize.leastsq(errfunc,p0[:],args=(datax,datay))
    p1 = numpy.append(p1,[0.0]).reshape(5,1)
    
    #~ print "--Sine Fit Results---"
    #~ print datax
    #~ print datay
    #~ print p1
    
    return p1
    
def sine_fun( a, datax):
    p=(a[0],a[1],a[2],a[3])
    ay=numpy.array([])
    datax = numpy.sort(datax)
    ax=numpy.linspace(numpy.min(datax), numpy.max(datax), 100)
    for x in ax:
        ay=numpy.append(ay, p[0]*numpy.sin( p[1]*x-p[2] ) + p[3])
    return ax,ay
    
    
def expsine(a0,data):
    p0=(a0[0],a0[1],a0[2],a0[3],a0[4])
    datax=data[:,0]
    datay=data[:,1]
    # Target function
    fitfunc = lambda p, x: p[0]*numpy.sin( p[1]*x-p[2] )*numpy.exp(-x*p[3]) + p[4]
    # Error function
    errfunc = lambda p, x, dat: fitfunc(p,x)-dat
    # Fit
    p1,success = optimize.leastsq(errfunc,p0[:],args=(datax,datay))
    
    #~ print "--Sine Fit Results---"
    #~ print datax
    #~ print datay
    #~ print p1
    
    return p1
    
def expsine_fun( a, datax):
    p=(a[0],a[1],a[2],a[3],a[4])
    ay=numpy.array([])
    datax = numpy.sort(datax)
    ax=numpy.linspace(numpy.min(datax), numpy.max(datax), 100)
    for x in ax:
        ay=numpy.append(ay, p[0]*numpy.sin( p[1]*x-p[2] )*numpy.exp(-x*p[3]) + p[4])
    return ax,ay
    
    
if __name__ == "__main__":
    print ""
    print "------ Testing fitlibrary.py ------"
    
    print ""
    print " * gaus1d"
    # generate random gaussian data
    p = [10, 5, 2, 4]
    ax=numpy.linspace(0,10,100)
    ax,dat = gaus1d_fun( p, ax)
    ay = numpy.array(dat)
    noise = 2*numpy.random.rand(100)-1
    noisydat = ay+noise-1
    # fit noisy data with gaussian, starting from a random p0
    p0 = p + numpy.random.rand(4)-1
    pFit = gaus1d( p0, numpy.transpose(numpy.array((ax,noisydat))) )
    # Get a plot of the fit results
    fitX,fitY=gaus1d_fun(pFit , ax)
    # Show the plot on screen 
    plt.plot(ax, noisydat,'.')
    plt.plot(fitX,fitY,'-')
    plt.show()
    
    print ""
    print " * sine"
    # generate random sine data
    p = [10, 5, 2, 4]
    ax=numpy.linspace(0,10,100)
    ax,dat = sine_fun( p, ax)
    ay = numpy.array(dat)
    noise = 0.4*(numpy.random.rand(100))
    noisydat = ay+noise-1
    # fit noisy data,starting from a random p0
    p0 = p + 0.2*(numpy.random.rand(4)-1)
    pFit = sine( p0, numpy.transpose(numpy.array((ax,noisydat))) )
    # Get a plot of the fit results
    fitX,fitY=sine_fun(pFit , ax)
    # Show the plot on screen 
    plt.plot(ax, noisydat,'.')
    plt.plot(fitX,fitY,'-')
    plt.show()
    
    
    
    print ""
    print " * expsine"
    # generate random gaussian data
    p = [10, 5, 2, 1,1]
    ax=numpy.linspace(0,10,100)
    ax,dat = expsine_fun( p, ax)
    ay = numpy.array(dat)
    noise = 0.1*numpy.random.rand(100)-1
    noisydat = ay+noise-1
    # fit noisy data with gaussian, starting from a random p0
    p0 = p + numpy.random.rand(5)-1
    pFit = expsine( p0, numpy.transpose(numpy.array((ax,noisydat))) )
    # Get a plot of the fit results
    fitX,fitY=expsine_fun(pFit , ax)
    # Show the plot on screen 
    plt.plot(ax, noisydat,'.')
    plt.plot(fitX,fitY,'-')
    plt.show()
    
    
    