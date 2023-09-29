#!/usr/bin/env python3
import subprocess
import threading
import argparse
import os
import time
parser = argparse.ArgumentParser()
parser.add_argument('--leech', dest='leech', action='store_true', help='Configure i2p to be a leech client rather than contribute to the network. (Not recommended but useful if integration time is slow.)')

#   Test clean environment without nix installs

args = parser.parse_args()

class browser():
    def browserProc():
        subprocess.call(['mullvad-browser', '-P', 'i2pbrowser', '127.0.0.1:7070'])
        subprocess.call(['pkill', 'i2pd'])
    browser = threading.Thread(target=browserProc)
    
class i2p():
    def i2pProc():
        if args.leech == True:
            subprocess.Popen(['i2pd', '--notransit', '--socksproxy.enabled', '0', '--i2pcontrol.enabled', '1', '--i2cp.enabled', '1', '--httpproxy.outproxy', 'http://outproxy.acetone.i2p:3128', '--httpproxy.inbound.length', '1', '--httpproxy.outbound.length', '1', '--http.showTotalTCSR', '1'])
        subprocess.Popen(['i2pd', '--bandwidth', 'O', '--socksproxy.enabled', '0', '--i2pcontrol.enabled', '1', '--i2cp.enabled', '1', '--httpproxy.outproxy', 'http://outproxy.acetone.i2p:3128', '--httpproxy.inbound.length', '1', '--httpproxy.outbound.length', '1', '--http.showTotalTCSR', '1'])
    i2p = threading.Thread(target=i2pProc)

def startup():
    browser.browser.start()
    i2p.i2pProc()

startup()
