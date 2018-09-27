#!/usr/bin/env python

"""Use Paramiko to retrieve the entire 'show version' output."""
from __future__ import print_function, unicode_literals
import paramiko
import time
from getpass import getpass

"""

1. Use Paramiko to retrieve the entire 'show version' output from pynet-rtr2. 


2. Use Paramiko to change the 'logging buffered <size>' configuration on pynet-rtr2. This will require that you enter into configuration mode.

pynet-rtr2 = 184.105.247.71
    username = pyclass
    password = 88newclass

"""

ip_addr = '184.105.247.71'
port = 22
username = 'pyclass'
password = '88newclass'
command = ('term len 0', 'conf term', 'logging buffered 7777', 'end')
MAX_BUFFER = 65535

def clear_buffer(remote_conn):
    """Clear any data in the receive buffer."""
    if remote_conn.recv_ready():
        return remote_conn.recv(MAX_BUFFER).decode('utf-8', 'ignore')


def disable_paging(remote_conn, cmd='terminal length 0'):
    """Disable output paging (i.e. --More--)."""
    cmd = cmd.strip()
    remote_conn.send(cmd + '\n')
    time.sleep(1)
    clear_buffer(remote_conn)


def send_command(remote_conn, cmd='', delay=1):
    """Send command down the channel. Retrieve and return the output."""
    if cmd != '':
        cmd = cmd.strip()
    remote_conn.send(cmd + '\n')
    time.sleep(delay)

    if remote_conn.recv_ready():
        return remote_conn.recv(MAX_BUFFER).decode('utf-8', 'ignore')
    else:
        return ''


def main():
    """Use Paramiko to retrieve the entire 'show version' output."""
    
    #try:
    #    ip_addr = raw_input("Enter IP address: ")
    #except NameError:
    #    ip_addr = input("Enter IP address: ")

    ip_addr = '184.105.247.71'
    username = 'pyclass'
    #password = getpass()
    password = '88newclass'
    port = 22

    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    remote_conn_pre.connect(ip_addr, port=port, username=username, password=password,
                            look_for_keys=False, allow_agent=False)
    remote_conn = remote_conn_pre.invoke_shell()

    time.sleep(1)
    clear_buffer(remote_conn)
    disable_paging(remote_conn)

    for item in command:
    	output = send_command(remote_conn, cmd=item)
    	print('\n>>>>')
    	print(output)
    	print('>>>>\n')


if __name__ == "__main__":
    main()
