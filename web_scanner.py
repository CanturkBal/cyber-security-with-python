import optparse

def getting_ip():
    object_parse = optparse.OptionParser()
    object_parse.add_option("--ip","--ipaddress",dest ="ip_address",help = ("changing the ip address you want to scan") )
    (user_input,arguements) = object_parse.parse_args()
    if not user_input.ip_address:
        print("enter a ip")
    return user_input

#adding input to choose a ip to scan

def scanning_network(ip):
    arp_request = scapy.ARP(pdst = ip)
    ##scapy.ls(scapy.ARP())
    #scanning the given ip 
    arp_broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #this broadcast request is for finding the mac addres that we want to find from ip. this basically searcher the ip's to find the specific mac address
    ##scapy.ls(scapy.ether())
    combined_packet = arp_broadcast / arp_request
    # combining the packets to one packet
    (answered_list, unanswered_list) = (scapy.srp(combined_packet, timeout=1))
    
    answered_list.summary()
 #making a broadcat and request packet,after that we combine them to see the mac and ip addresses
user_address = getting_ip()
scanning_network(user_address.ip_address)
#printing the result
