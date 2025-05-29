import time

from kivy.animation import Animation
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from street import ThirdScreen
import openai  # Install using:

import street
openai.api_key = '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'
levels=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
class Map(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global layout
        layout = FloatLayout()
        LabelBase.register(name='CustomFont', fn_regular='DRKrapkaRhombus-FontSize10px.ttf')
        background_image = Image(source='photo_5190922462521579832_y.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)





class MapApp(App):
    def build(self):
        return Map()


if __name__ == '__main__':
    MapApp().run()
