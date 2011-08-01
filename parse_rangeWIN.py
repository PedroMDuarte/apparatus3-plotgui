import sys
import getopt
import math

def main(rangestr):

    shots=[] 

    l = rangestr.split(',')
    for token in l:
        if token.find(':') > -1:
            sh0 = int(token.split(':')[0])
            shf = int(token.split(':')[1])
            if shf < sh0:
                sys.stderr.write( "\n----------> RANGE ERROR: end of range is smaller than start of range\n\n")
                return
            for num in range(sh0,shf+1):
                numstr = "%04d" % num
                shots.append(numstr)
        elif token.find('-') == 0:
            l2 = token.split('-')[1:]
            for shot in l2:
                if shot in shots:
                    shots.remove(shot)
    return shots


if __name__ == '__main__':
    main(sys.argv[1])