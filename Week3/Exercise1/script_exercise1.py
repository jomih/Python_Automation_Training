#!/usr/bin/env python

import snmp_helper
import time

"""
1. Using SNMPv3 create a script that detects router configuration changes.
If the running configuration has changed, then send an email notification to yourself identifying the router that changed and the time that it changed

"""

DEVICE = ('184.105.247.71', '161') #pynet-rtr2 (Cisco 881)
OID = '1.3.6.1.4.1.9.9.43.1.1.1.0'  #ccmHistoryRunningLastChanged = 
SNMP_USER = ('pysnmp', 'galileo1', 'galileo1') #username, auth_key, encrypt_key


def send_mail(recipient, subject, message, sender):
    '''
    Simple function to help simplify sending SMTP email

    Assumes a mailserver is available on localhost
    '''

    import smtplib
    from email.mime.text import MIMEText

    message = MIMEText(message)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = recipient

    # Create SMTP connection object to localhost
    smtp_conn = smtplib.SMTP('localhost')

    # Send the email
    smtp_conn.sendmail(sender, recipient, message.as_string())

    # Close SMTP connection
    smtp_conn.quit()
    return True

def main():
	previous_changed_seconds = 0
	changes = 0
	while (1):
		snmp_output = snmp_helper.snmp_get_oid_v3(DEVICE, SNMP_USER, oid=OID)
		print 'Raw output:', snmp_output
		current_changed_seconds = snmp_helper.snmp_extract(snmp_output)
		print '\nFormatted output:', current_changed_seconds
		print 'changes is', changes
		if (not(int(previous_changed_seconds) == int(current_changed_seconds))):
			if (changes):
				print '\nConfig changed (\#', str(changes),')', str(int(current_changed_seconds)/100),'secs ago'
				message_sender = 'lab@msn.com'
				message_subject = 'config changed'
				message_recipient = 'jomih@msn.com'
				message_content = 'Config of router has recently changed'
				email_result = send_mail(message_recipient, message_subject, message_content, message_sender)
				if (email_result):
					print 'Email sent'
				else:
					print 'Error sending email'
			changes = changes + 1
			previous_changed_seconds = current_changed_seconds
		else:
			print 'Nothing changed:'
			print '  previous_changed_seconds', previous_changed_seconds
			print '  current_changed_seconds', current_changed_seconds
			print '  changes', changes
		time.sleep(310)


##############
#Main Program
##############

if __name__ == "__main__":
	print '\n## Script started\n'
	main()
	print '\n## Script finished\n'
