#!/usr/bin/env python3
import subprocess
import threading
import argparse
import os
import time
parser = argparse.ArgumentParser()
parser.add_argument('--leech', dest='leech', action='store_true', help='Configure i2p to be a leech client rather than contribute to the network. (Not recommended but useful if integration time is slow.)')
parser.add_argument('--ifname', dest='ifname', action='store_true')
parser.add_argument('--outproxy', dest='outproxy', action='store_true')
parser.add_argument('--socks', dest='socks', action='store_true')
parser.add_argument(dest='stdinn', action='append', nargs='?')

args = parser.parse_args()
class cliParser():
    initarg = '{}'.format(args.stdinn)
    noLbracket = initarg.replace('[', '')
    noRbracket = noLbracket.replace(']', '')
    noQuotes = noRbracket.replace("'", "")
    specin = noQuotes

class env_vars():
    ifname = '' # CHANGE ME FOR DEFAULT
    startpage = '127.0.0.1:7070' # Standard i2pd webconsole address. Replace with any site you wish.
    bandwidth = 'O' # Standard options are: L, O, P, and X
    tor_outproxy = 'socks://localhost:9050'
    acetone_outproxy = 'http://outproxy.acetone.i2p:3128'
    off_outproxy = '0.0.0.0'
    http_outproxy = acetone_outproxy # CHANGE ME FOR DEFAULT
    leech = False
    socks = False

class browser():
    def browserProc():
        subprocess.call(['mullvad-browser', '-P', 'i2pbrowser', '{}'.format(env_vars.startpage)])
        subprocess.call(['pkill', 'i2pd'])
        if env_vars.http_outproxy == env_vars.tor_outproxy:
            subprocess.call(['pkill', 'tor'])
    browser = threading.Thread(target=browserProc)
    
class network():
    socksproxy = '0'
    if env_vars.socks == True or args.socks == True:
        socksproxy = '1'
    if args.ifname == True:
        env_vars.ifname = '{}'.format(cliParser.specin)
    if args.outproxy == True:
        if cliParser.specin == 'tor':
            env_vars.http_outproxy = env_vars.tor_outproxy
        elif cliParser.specin == 'acetone':
            env_vars.http_outproxy = env_vars.acetone_outproxy
        elif cliParser.specin == 'off':
            env_vars.http_outproxy = env_vars.off_outproxy
    def i2pProc():
        if args.leech == True or env_vars.leech == True:
            subprocess.Popen(['i2pd', '--notransit', '--ifname', '{}'.format(env_vars.ifname), '--bandwidth', '{}'.format(env_vars.bandwidth), '--socksproxy.enabled', '{}'.format(network.socksproxy), '--httpproxy.outproxy', '{}'.format(env_vars.http_outproxy), '--httpproxy.inbound.length', '1', '--httpproxy.outbound.length', '1', '--http.showTotalTCSR', '1'])
        else:
            subprocess.Popen(['i2pd', '--ifname', '{}'.format(env_vars.ifname), '--bandwidth', '{}'.format(env_vars.bandwidth), '--socksproxy.enabled', '{}'.format(network.socksproxy), '--httpproxy.outproxy', '{}'.format(env_vars.http_outproxy), '--httpproxy.inbound.length', '1', '--httpproxy.outbound.length', '1', '--http.showTotalTCSR', '1'])
    def torProc():
        os.system('tor')
    tor = threading.Thread(target=torProc)
    i2p = threading.Thread(target=i2pProc)

def startup():
    browser.browser.start()
    if env_vars.http_outproxy == env_vars.tor_outproxy:
        network.tor.start()
    network.i2pProc()

startup()
