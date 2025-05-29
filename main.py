from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image


import beginning
from Aty2 import BScreen
from Atyrau import pAScreen
from port import FourthScreen
from sea import DScreen
from street import ThirdScreen
from map import Map
global levels
levels=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()
        LabelBase.register(name='CustomFont', fn_regular='DRKrapkaRhombus-FontSize10px.ttf')

        # Load the background image
        background_image = Image(source='photo_5190922462521579832_y.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        # Load the logo image
        logo_image = Image(source='assets/logo11.png', size_hint=(0.35, 0.35), size=(250, 250),
                           pos_hint={'center_x': 0.5, 'center_y': 0.75})
        layout.add_widget(logo_image)

        # Create a button to transition to the second screen

        button1 = Button( font_name='CustomFont', size_hint=(0.25, 0.15),
                         pos_hint={'x': 0.375, 'y': 0.4})
        # Set the background image of the button
        button1.background_normal = 'assets/start.png'
        # Bind the button's on_press event
        button1.bind(on_press=self.switch_to_second_screen)


        layout.add_widget(button1)

        button2 = Button( font_name='CustomFont', size_hint=(0.25, 0.15),
                         pos_hint={'x': 0.375, 'y': 0.23})
        # Set the background image of the button
        button2.background_normal = 'assets/settings.png'
        # Bind the button's on_press event

        layout.add_widget(button2)
        button3 = Button( font_name='CustomFont', size_hint=(0.25, 0.15),
                         pos_hint={'x': 0.375, 'y': 0.06})
        # Set the background image of the button
        button3.background_normal = 'assets/contact.png'
        # Bind the button's on_press event

        layout.add_widget(button3)
        self.add_widget(layout)

    def switch_to_second_screen(self, instance):
        self.manager.current = 'second_screen'

    def switch_to_map(self, instance):
        self.manager.current = 'map'


class FirstApp(App):
    def build(self):
        screen_manager = ScreenManager()

        first_screen = FirstScreen(name='first_screen')  # Set the name here
        screen_manager.add_widget(first_screen)

        second_screen = beginning.SecondScreen(name='second_screen')  # Set the name here
        screen_manager.add_widget(second_screen)

        third_screen = ThirdScreen(name='third_screen')
        screen_manager.add_widget(third_screen)
        fourth_screen = FourthScreen(name='fourth_screen')
        screen_manager.add_widget(fourth_screen)
        d_screen = DScreen(name='d_screen')
        screen_manager.add_widget(d_screen)
        b_screen = pAScreen(name='b_screen')
        screen_manager.add_widget(b_screen)
        a_screen = BScreen(name='a_screen')
        screen_manager.add_widget(a_screen)


        map= Map(name='map')  # Set the name here
        screen_manager.add_widget(map)

        return screen_manager


if __name__ == '__main__':
    FirstApp().run()
