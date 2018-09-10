#!/usr/bin/env python

import telnetlib
import time

IP_ADDR = '184.105.247.70'
TELNET_PORT = 23
TELNET_TIMEOUT = 6
username = 'pyclass'
password = '88newclass'
command = 'show ip interface brief'

def main():

	remote_conn = telnetlib.Telnet(IP_ADDR, TELNET_PORT, TELNET_TIMEOUT)
	output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
	#print output
	output = remote_conn.write(username + '\n')
	#print output
	output = remote_conn.read_until("assword:", TELNET_TIMEOUT)
	#print output
	output = remote_conn.write(password + '\n')
	#print output
	time.sleep(1)
	output = remote_conn.write('term len 0' + '\n')
	#print output
	time.sleep(1)
	output = remote_conn.write(command + '\n')
	print output
	time.sleep(1)
	output = remote_conn.read_very_eager()	
	print output
	remote_conn.close()

##############
#Main Program
##############

if __name__ == "__main__":
	print '\n## Script started\n'
	main()
	print '\n## Script finished\n'
