from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.behaviors import ButtonBehavior

class MainApp(App):
    def build(self):
        img = AsyncImage(source='https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.pinimg.com%2Foriginals%2Faf%2F09%2F7f%2Faf097fe7649416b7f13dde2e597e0bae.jpg&imgrefurl=https%3A%2F%2Fin.pinterest.com%2Fpin%2F808255464344354810%2F&tbnid=57Qal4_6EUJimM&vet=12ahUKEwit2e7XgZDuAhVS3FkKHVjPCDkQMygCegUIARC2AQ..i&docid=0-qYbINFTv6HPM&w=1303&h=1301&q=smiley%20face&hl=en&ved=2ahUKEwit2e7XgZDuAhVS3FkKHVjPCDkQMygCegUIARC2AQ'),
                    size_hint=(1, .5),
                    pos_hint={'center_x':.5, 'center_y':.5})

        return img

if __name__ == '__main__':
    app = MainApp()
    app.run()
