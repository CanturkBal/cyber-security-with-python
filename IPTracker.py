
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput 
from kivy.uix.image import Image 
from kivy.uix.button import Button 
from kivy.core.window import Window
import time
import os as os
import folium
import pyfiglet
import geocoder


Window.size = (720,600)
class Ip_tracker(MDApp):
    def build(self):
        self.icon = "iconfinder-dedicatedipaddress-4263513_117864.ico"
        layout = MDRelativeLayout(md_bg_color = [0,0,0])

        self.image = Image(source='ip.png',size_hint=(.3,.3),pos_hint={'center_x':0.5,"center_y":0.87})
        self.Title = Label(text="Ip Tracker ", size_hint=(.5,.5),pos_hint={"center_x":0.5,"center_y":0.70},font_size=20)
        self.entry=  TextInput(text="",pos_hint={"center_x":0.5,"center_y":0.50},height=48,size_hint=(0.5,0.1),font_size=29)
        self.button = Button(text="Find Ip",size_hint=(0.15,0.15),pos_hint = {"center_x":0.5,"center_y":0.30},background_color=(34/255,139/255,34/255))
        self.button.bind(on_release=self.get_address)
        layout.add_widget(self.image)
        layout.add_widget(self.Title)
        layout.add_widget(self.entry)
        layout.add_widget(self.button)



        return layout
    def get_address(self,button):
        try:

            input_value = self.entry.text
            print(input_value)
            g = geocoder.ip(input_value) #==> gets your ip address or put an ip address

            myaddress = g.latlng
            
            
            print(myaddress)
            my_map1 = folium.Map(location=myaddress,zoom_start=12)
            folium.CircleMarker(location=myaddress,radius=50,popup="Yorkshire").add_to(my_map1)
            my_map1.save("my_map.html")
        except:
            print("Error has occured")









if __name__ == '__main__':
    Ip_tracker().run()