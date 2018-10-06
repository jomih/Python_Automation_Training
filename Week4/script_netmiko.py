#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

"""

5. Use Netmiko to enter into configuration mode on pynet-rtr2. Also use Netmiko to verify your state (i.e. that you are currently in configuration mode).


6. Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.


7. Use Netmiko to change the logging buffer size (logging buffered <size>) on pynet-rtr2.


8. Use Netmiko to change the logging buffer size (logging buffered <size>) and to disable console logging (no logging console) from a file on both pynet-rtr1 and pynet-rtr2 (see 'Errata and Other Info, item #4).

"""

pynet_rtr1 = {
    'device_type' : 'cisco_ios',
    'ip' : '184.105.247.70',
    'port' : '22',
    'username' : 'pyclass',
    'password' : '88newclass',
}

pynet_rtr2 = {
    'device_type' : 'cisco_ios',
    'ip' : '184.105.247.71',
    'port' : '22',
    'username' : 'pyclass',
    'password' : '88newclass',
}

pynet_vsrx = {
    'device_type' : 'juniper',
    'ip' : '184.105.247.76',
    'port' : '22',
    'username' : 'pyclass',
    'password' : '88newclass',    
}

def connect_router(connection_data):
    rtr_connect = ConnectHandler(**connection_data)
    return(rtr_connect)

def check_prompt(rtr_connect):
    output = rtr_connect.find_prompt()
    print 'prompt is:', output
    rtr_connect.config_mode()
    output = rtr_connect.check_config_mode()
    print 'Config mode?', output
    rtr_connect.exit_config_mode()
    return(1)

def send_command(rtr_connect, command):
    output = rtr_connect.send_command(command)
    print command,':\n', output
    return (output)

def config_change (rtr_connect, config_command):
    output = rtr_connect.send_config_set(config_command)
    return(1)

def main():
    print '\nConnecting to pynet_rtr1'
    rtr_connect = connect_router(pynet_rtr1)
    
    check_prompt(rtr_connect)

    command = 'show arp'
    output = send_command (rtr_connect, command)
    rtr_connect.disconnect()

    print '\nConnecting to pynet_rtr2'
    rtr_connect = connect_router(pynet_rtr2)
    output = send_command (rtr_connect, command)
    rtr_connect.disconnect()

    print '\nConnecting to pynet_vsrx'
    rtr_connect = connect_router(pynet_vsrx)
    output = send_command (rtr_connect, command)
    rtr_connect.disconnect()

    print '\nConnecting to pynet_rtr2. Changing config'
    rtr_connect = connect_router(pynet_rtr2)
    config_command = 'logging buffered 9999'
    output = config_change (rtr_connect, config_command)
    command = 'show run | include logging'
    output = send_command (rtr_connect, command)
    rtr_connect.disconnect()

if __name__ == "__main__":
    main()
