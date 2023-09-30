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
class env_vars():
    ifname = 'eth0' # Please replace eth0 with the network interface you want to connect with (if it does not work, try eno1)
    startpage = '127.0.0.1:7070' # Standard i2pd webconsole address. Replace with any site you wish.
    bandwidth = 'O' # Standard options are: L, O, P, and X
    http_outproxy = 'http://outproxy.acetone.i2p:3128' # Change to 0.0.0.0 to ignore 
    leech = False
    
class browser():
    def browserProc():
        subprocess.call(['mullvad-browser', '-P', 'i2pbrowser', '{}'.format(env_vars.startpage)])
        subprocess.call(['pkill', 'i2pd'])
    browser = threading.Thread(target=browserProc)
    
class i2p():
    def i2pProc():
        if args.leech == True or env_vars.leech == True:
            subprocess.Popen(['i2pd', '--notransit', '--socksproxy.enabled', '0', '--i2pcontrol.enabled', '1', '--i2cp.enabled', '1', '--httpproxy.outproxy', 'http://outproxy.acetone.i2p:3128', '--httpproxy.inbound.length', '1', '--httpproxy.outbound.length', '1', '--http.showTotalTCSR', '1'])
        else:
            subprocess.Popen(['i2pd', '--ifname', '{}'.format(env_vars.ifname), '--bandwidth', '{}'.format(env_vars.bandwidth), '--socksproxy.enabled', '0', '--i2pcontrol.enabled', '1', '--i2cp.enabled', '1', '--httpproxy.outproxy', '{}'.format(env_vars.http_outproxy), '--httpproxy.inbound.length', '1', '--httpproxy.outbound.length', '1', '--http.showTotalTCSR', '1'])
    i2p = threading.Thread(target=i2pProc)

def startup():
    browser.browser.start()
    i2p.i2pProc()

startup()
