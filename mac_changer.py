import subprocess
import optparse
import re
def getting_input():
    object_parse = optparse.OptionParser()
    object_parse.add_option("-i", "--interface", dest="interface", help="interface to change")
    object_parse.add_option("-m", "--mac", dest="mac_address", help="type your new mac address")
    return object_parse.parse_args()
#creating the inputs to change your mac address with optparse

def change_mac(user_interface,user_mac):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac])
    subprocess.call(["ifconfig", user_interface, "up"])
# using subprocces library to write some commands to change the mac address
def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
    if new_mac:
        return(new_mac.group(0))
    else:
        return None
#checking the new mac if its changed with re library
(user_input,arguements) = getting_input()
print("mac changer started")
change_mac(user_input.interface,user_input.mac_address)
finalized_mac = control_new_mac(str(user_input.interface))
if finalized_mac == user_input.mac_address:
    print("Success")
else:
    print("error")
