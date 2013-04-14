#!/usr/bin/python

import os
import time

import ConfigParser

config = ConfigParser.SafeConfigParser()
config.optionxform = str
config.read('hlds_check.conf')

base_dir = config.get('main', 'base_dir')
server_list = config.items('servers')

print '\033[33mHLDS Check is running...\033[0m'

while 1:
    for name, address in server_list:
        p = os.popen('qstat -hla2s %s -nh' % address, "r")
        line = p.readline().strip()
        chunks = line.split()
        if chunks[1] == 'DOWN' or chunks[1] == 'no':
            kill_command = 'screen -S %s -X quit' % name
            start_command = './%s' % name
            os.chdir(name)
            print 'Current directory is: '
            os.system('pwd')
            print 'killing server with %s ' % kill_command
            os.system(kill_command)
            print 'starting server with %s ' % start_command
            os.system(start_command)
            os.chdir(base_dir)
    time.sleep(10)