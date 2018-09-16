#!/usr/bin/env python

import snmp_helper
import time, pygal

"""
2. Using SNMPv3 create two SVG image files.  

The first image file should graph the input and output octets on interface FA4 on pynet-rtr1 every five minutes for an hour.  Use the pygal library to create the SVG graph file. Note, you should be doing a subtraction here (i.e. the input/output octets transmitted during this five minute interval).  

The second SVG graph file should be the same as the first except graph the unicast packets received and transmitted.

The relevant OIDs are as follows:

('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5')
('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5')
('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5')
('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5'),
('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5')

"""

DEVICE = ('184.105.247.70', '161') #pynet-rtr1 (Cisco 881)
ifDescr_fa4 = '1.3.6.1.2.1.2.2.1.2.5'
ifInOctets_fa4 = '1.3.6.1.2.1.2.2.1.10.5'
ifInUcastPkts_fa4 = '1.3.6.1.2.1.2.2.1.11.5'
ifOutOctets_fa4 = '1.3.6.1.2.1.2.2.1.16.5'
ifOutUcastPkts_fa4 = '1.3.6.1.2.1.2.2.1.17.5'
SNMP_USER = ('pysnmp', 'galileo1', 'galileo1') #username, auth_key, encrypt_key


def get_statistics_fa4(device, snmp_user, oid):

	snmp_output = snmp_helper.snmp_get_oid_v3(device, snmp_user, oid[0])
	#print 'OID=', oid[0]
	parsed_input_octets = snmp_helper.snmp_extract(snmp_output)
	#print 'Output:', parsed_input_octets, '\n'
	snmp_output = snmp_helper.snmp_get_oid_v3(device, snmp_user, oid[1])
	#print 'OID=', oid[1]
	parsed_output_octets = snmp_helper.snmp_extract(snmp_output)
	#print 'Output:', parsed_output_octets, '\n'

	return (int(parsed_input_octets), int(parsed_output_octets))

def main():

	packet_statistics = {}
	packet_statistics['Input octets'] = []
	packet_statistics['Output octets'] = []
	packet_statistics['Input packets'] = []
	packet_statistics['Output packets'] = []
	octets_oid = (ifInOctets_fa4, ifOutOctets_fa4)
	packets_oid = (ifInUcastPkts_fa4, ifOutUcastPkts_fa4)
	iterations = 0
	
	while (iterations < 20):

		#Grab octets info
		input_octets, output_octets = get_statistics_fa4(DEVICE, SNMP_USER, oid=octets_oid)

		packet_statistics['Input octets'].append(input_octets)
		packet_statistics['Output octets'].append(output_octets)

		#Grab packets info
		input_packets, output_packets = get_statistics_fa4(DEVICE, SNMP_USER, oid=packets_oid)

		packet_statistics['Input packets'].append(input_packets)
		packet_statistics['Output packets'].append(output_packets)

		iterations = iterations + 1
		time.sleep(300)

	#print 'packet_statistics[Input packets]', packet_statistics['Input packets']
	#print 'packet_statistics[Output packets]', packet_statistics['Output packets']

	# Creates SVG chart
	line_chart = pygal.Line()
	line_chart.title = ''
	line_chart.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']
	line_chart.add('InPackets', packet_statistics['Input packets'])
	line_chart.add('OutPackets', packet_statistics['Output packets'])
	line_chart.add('InOctets', packet_statistics['Input octets'])
	line_chart.add('OutOctets', packet_statistics['Output octets'])

	line_chart.render_to_file('test.svg')

##############
#Main Program
##############

if __name__ == "__main__":
	print '\n## Script started\n'
	main()
	print '\n## Script finished\n'
