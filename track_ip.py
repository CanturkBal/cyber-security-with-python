import geocoder
import folium
import codecs
import optparse
import pyfiglet
import time
def getting_input():
    object_parse = optparse.OptionParser()
    object_parse.add_option("-i", "--ip", dest="ip", help="ip to change,if you want to search your ip, just type `me`")
    return object_parse.parse_args()
[user_input,arguements] = getting_input()  

out = pyfiglet.figlet_format("IP TRACKER")


try:

    g = geocoder.ip(user_input.ip) #==> gets your ip address or put an ip address

    myaddress = g.latlng
    print(out)
    time.sleep(1)
    
    print(myaddress)
    my_map1 = folium.Map(location=myaddress,zoom_start=12)
    folium.CircleMarker(location=myaddress,radius=50,popup="Yorkshire").add_to(my_map1)

    folium.Marker(location=myaddress,popup="Yorkshire").add_to(my_map1)

    my_map1.save("my_map.html")
except:
    print("can not find the location of your IP!!!")
