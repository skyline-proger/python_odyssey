# street.py
import time

from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen


class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        LabelBase.register(name='CustomFont', fn_regular='DRKrapkaRhombus-FontSize10px.ttf')
        background_image = Image(source='photo_5190922462521579853_y (1).jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)
        ai_image = Image(source='image_2024-03-25_11-48-46.png', size_hint=(None, None), size=(200, 200),
                         pos=(750, 155))
        layout.add_widget(ai_image)
        dialog_image = Image(source='93586-box-angle-brand-game-video-dialog-mother.png', size_hint=(None, None),
                             size=(1300, 1000), pos=(-169, -340))
        layout.add_widget(dialog_image)
        self.label111 = Label(text='', font_size='20sp', font_name='CustomFont',
                              pos_hint={'center_x': 0.5, 'center_y': 0.1})
        layout.add_widget(self.label111)
        self.label12 = Label(text='A.I.', font_size='20sp', pos_hint={'center_x': 0.14, 'center_y': 0.255})
        layout.add_widget(self.label12)

        self.add_widget(layout)

    def on_enter(self):
        # Schedule the typing animation when the screen is entered
        Clock.schedule_interval(self.type_text, 0.1)

    def type_text(self, dt):
        # Define the text to be typed
        target_text = "print() әр түрлі жолдармен қолданылуы мүмкін: жол мәндері үшін\n print("") / print(''), қойындылар үшін /t \nжәне жаңа жолдар үшін /n."

        # Get the current text of the label
        current_text = self.label111.text

        # Check if all letters are typed
        if len(current_text) < len(target_text):
            # Add one letter to the label text
            self.label111.text = target_text[:len(current_text) + 1]
        else:
            # Stop the typing animation
            Clock.unschedule(self.type_text)
            # Replace the text of label11 with a new one


            # Start the typing animation for the new text
            Clock.schedule_once(self.switch_to_fourth_screen, 3)
            self.label111.text = ""
    def switch_to_fourth_screen(self, dt):
        self.manager.current = 'fourth_screen'
class ThirdApp(App):
    def build(self):
        return ThirdScreen()


if __name__ == '__main__':
    ThirdApp().run()
