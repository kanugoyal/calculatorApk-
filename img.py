from kivy.app import App
from kivy.uix.image import Image

class MainApp(App):
    def build(self):
        img = Image(source = 'img.jpg',size_hint= (2, .5), pos_hint= {'center_x': .9, 'center_y': .2})

        return img

if __name__ == '__main__':
    app = MainApp()
    app.run()
