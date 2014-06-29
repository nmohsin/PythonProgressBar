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
    s = "Download progress: [{0}%]"
    messages = [(s + '.' * i) for i in range(4)]
    bar = SimpleBar()
    
    for i in range(40):
        percentage = i/4 * 10
        m = messages[i % 4]
        bar.update(m, percentage)
        time.sleep(.5)

    
    print


if __name__ == '__main__':
    main()
        
