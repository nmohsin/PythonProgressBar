#! /usr/bin/env python

import sys
import time

from progresswidgets import SimpleBar 

def restart_line():
    sys.stdout.write('\r')
    sys.stdout.flush()
    

def old():
    for i in range(100):
        print "Download progress [%d%%]\r" % i,
        time.sleep(0.5)
        restart_line()
    print

def main():
    b = SimpleBar("Download progress {0}%")
    for i in range(10):
        b.update(10 * i)
        time.sleep(2)
    print


if __name__ == '__main__':
    main()
        
