from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.utils import platform
import socket
import os



from kivy.uix.button import Button
from kivy.uix.label import Label

if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

class MyWidget(BoxLayout):
    s = socket.socket()
    host = '192.168.1.186'
    port = 3000
    s.connect((host, port))
    print("connected")
    def selected(self, filename):
        try:
            self.ids.image.source = filename[0]
        except:
            pass
    def recognise(self):
        with open(self.ids.image.source, "rb") as file:
            file_data = file.read(4096)
            while file_data:
                self.s.send(file_data)
                file_data = file.read(4096)
                if not file_data: break
                # if len(file_data) == 0:
                #     self.s.send("1".encode())
                #     print("lol")
        reply = self.s.recv(4096).decode()
        str_reply = str(reply)
        self.ids.label.text = str_reply



class MyApp(App):
    def build(self):
        Window.clearcolor = (200/255,200/255,200/255,1)
        return MyWidget()


if __name__ == "__main__":
    window = MyApp()
    window.run()