#!/usr/bin/env python3
import subprocess
import threading
import argparse
import os
import time
parser = argparse.ArgumentParser()
parser.add_argument('--verbose', dest='verbose', action='store_true', help='Open terminal output for browser and i2pd router')


args = parser.parse_args()
class browser():
    def browserProc():
        subprocess.call(['i2p-browser', 'localhost:7070'])
    browser = threading.Thread(target=browserProc)
    
class i2p():
    def i2pProc():
        #os.system('starti2pd')
        subprocess.Popen(['/home/alyx/.nix-profile/bin/i2pd', '--ifname', 'tun0', '--bandwidth', 'X', '--httpproxy.outproxy', 'http://outproxy.acetone.i2p:3128', '--httpproxy.inbound.length', '1', '--httpproxy.outbound.length', '1', '--http.showTotalTCSR', '1'])
    i2p = threading.Thread(target=i2pProc)

def startup():
    #i2p.i2p.start()
    #browser.browser.start()
    browser.browser.start()
    #time.sleep(7)
    i2p.i2pProc()
# close i2p with browser close... 

startup()