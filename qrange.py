import getopt, sys, configobj, numpy

from StringIO import StringIO

sys.path.append('L:/software/apparatus3/bin')
import parse_rangeWIN


def qrange(dir,range,keys):
    fakefile=""
    shots=parse_rangeWIN.main(range)
    #print shots
    errmsg=''
    rawdat='#%s%s\n' % ('SEC:shot\t',keys.replace(' ','\t'))
    
    for shot in shots:
        
        
        report=dir+'report'+shot+'.INI'
        from configobj import ConfigObj
        report=ConfigObj(report)
        if report == {}:
            errmsg=errmsg + "...Report #%s does not exist in %s!\n" % (shot,dir)
            continue
        
        fakefile = fakefile + '\n'
        rawdat = rawdat + '\n%s\t\t' % shot
        line=''
        line_=''
        err=False
        for pair in keys.split(' '):
            sec = pair.split(':')[0]
            key = pair.split(':')[1]
            try:
                val = report[sec][key]
                line  = line  + val + '\t'
                fval = float(val)
                if fval > 1e5 or fval < 1e5:
                    lstr = '%.3e\t\t' % fval
                else:
                    lstr = '%.4f\t\t' % fval
                line_ = line_ + lstr
            except KeyError:
                err = True
                errstr = '...Failed to get %s:%s from #%s\n' % (sec,key,shot)
                errmsg = errmsg + errstr
        if not err:
            fakefile = fakefile + line
            rawdat = rawdat + line_
                
    a=numpy.loadtxt(StringIO(fakefile))
    print errmsg
    return a, errmsg, rawdat

    