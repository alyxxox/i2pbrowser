#!/usr/bin/env python3
import subprocess
import threading
import argparse
import os
import time
import signal 

parser = argparse.ArgumentParser()
parser.add_argument('--leech', dest='leech', action='store_true', help='Configure i2p to be a leech client rather than contribute to the network. (Not recommended but useful if integration time is slow.)')
parser.add_argument('--ifname', dest='ifname', action='store_true')
parser.add_argument('--socks', dest='socks', action='store_true')
parser.add_argument('-v', '--version', dest='version', action='store_true')
parser.add_argument(dest='stdinn', action='append', nargs='?')

args = parser.parse_args()
class CliParser:
    def __init__(self, stdinn):
        self.stdinn = stdinn

    def clean_input(self):
        cleaned_input = str(self.stdinn).strip('[]\'')
        return cleaned_input


cli_parser = CliParser(args.stdinn)
specin = cli_parser.clean_input()
class env_vars():
    ifname = 'tun0' # CHANGE ME FOR DEFAULT
    startpage = '127.0.0.1:7070' # Standard i2pd webconsole address. Replace with any site you wish.
    bandwidth = 'O' # Standard options are: L, O, P, and X
    http_outproxy = 'http://outproxy.acetone.i2p:3128' # CHANGE ME FOR DEFAULT
    leech = False
    socks = True

class browser():

    def browserProc():

        launch_browser = ['mullvad-browser', '-P', 'i2pbrowser', '{}'.format(env_vars.startpage)]
        kill_i2pProc = ['pkill', '--signal', 'SIGTERM', 'i2pd']

        subprocess.call(launch_browser)
        subprocess.call(kill_i2pProc)
    browser = threading.Thread(target=browserProc)
    
class network():

    socksproxy = '0'

    if env_vars.socks == True or args.socks == True:

        socksproxy = '1'

    if args.ifname == True:
        
        env_vars.ifname = '{}'.format(specin)

    def i2pProc():

        # change to launch_i2pd.extend(['--notransit])
        launch_i2pd_leech = [
            'i2pd', 
            '--notransit', 
            '--ifname', 
            '{}'.format(env_vars.ifname), 
            '--bandwidth', 
            '{}'.format(env_vars.bandwidth), 
            '--socksproxy.enabled', 
            '{}'.format(network.socksproxy), 
            '--httpproxy.outproxy', 
            '{}'.format(env_vars.http_outproxy), 
            '--httpproxy.inbound.length', 
            '1', 
            '--httpproxy.outbound.length', 
            '1', 
            '--http.showTotalTCSR', 
            '1'
            ]

        launch_i2pd = [
            'i2pd', 
            '--ifname', 
            '{}'.format(env_vars.ifname), 
            '--bandwidth', 
            '{}'.format(env_vars.bandwidth), 
            '--socksproxy.enabled', 
            '{}'.format(network.socksproxy), 
            '--httpproxy.outproxy', 
            '{}'.format(env_vars.http_outproxy), 
            '--httpproxy.inbound.length', 
            '1', 
            '--httpproxy.outbound.length', 
            '1', 
            '--http.showTotalTCSR', 
            '1'
            ]
        
        if args.leech == True or env_vars.leech == True:
            i2pd_proc = subprocess.Popen(launch_i2pd_leech)

        else:
            i2pd_proc = subprocess.Popen(launch_i2pd)

    i2p = threading.Thread(target=i2pProc)

def startup():
    browser.browser.start()
    network.i2p.start()

if args.version == True:
    print('I2P-Browser version 1.12')

else:
    startup()
