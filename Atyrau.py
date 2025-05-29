
import time

import openai
from kivy.animation import Animation
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
from kivy.uix.textinput import TextInput




openai.api_key = 'API-KEY-HERE'  # Replace with your actual OpenAI API key
levels=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

class pAScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global layout
        layout = FloatLayout()
        LabelBase.register(name='CustomFont', fn_regular='DRKrapkaRhombus-FontSize10px.ttf')
        background_image = Image(source='daniilnossov_pixel_art_Atyrau_city_billboard_about_oil_industry_f71c1703-faed-4a0c-adf5-2d75c089041b.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)
        ai_image = Image(source='image_2024-03-25_11-48-46.png', size_hint=(None, None), size=(200, 200),
                         pos=(750, 155))
        layout.add_widget(ai_image)
        dialog_image = Image(source='93586-box-angle-brand-game-video-dialog-mother.png', size_hint=(None, None),
                             size=(1300, 1000), pos=(-169, -340))
        layout.add_widget(dialog_image)
        self.label11 = Label(text='', font_size='20sp', font_name='CustomFont',
                             pos_hint={'center_x': 0.5, 'center_y': 0.1})
        layout.add_widget(self.label11)
        self.label12 = Label(text='A.I.', font_size='20sp', pos_hint={'center_x': 0.14, 'center_y': 0.255})
        layout.add_widget(self.label12)

        self.add_widget(layout)

    def on_enter(self):
        # Schedule the typing animation when the screen is entered
        Clock.schedule_interval(self.type_text, 0)

    def type_text(self, dt):
        # Define the text to be typed
        target_text = "Біз Қазақстанның мұнай өнеркәсібінің \nорталығы Атырауға жүзіп келдік. \nБұл қала бюджет кірісінің 40%-ға жуығын қамтамасыз етіп, \nел экономикасында орасан зор рөл атқарады."

        # Get the current text of the label
        current_text = self.label11.text

        # Check if all letters are typed
        if len(current_text) < len(target_text):
            # Add one letter to the label text
            self.label11.text = target_text[:len(current_text) + 1]
        else:
            # Stop the typing animation
            Clock.unschedule(self.type_text)
            # Replace the text of label11 with a new one
            self.label11.text = "IIUGIGO"
            time.sleep(1.5)
            # Start the typing animation for the new text
            Clock.schedule_interval(self.type_new_text, 0)

    def type_new_text(self, td):
        # Define the text to be typed
        target_text = "20 ғасырда Атырау Қазақстанның мұнай астанасы болды. \n Мұнда мұнай өндіріледі, одан газ\  "

        # Get the current text of the label
        current_text = self.label11.text

        # Check if all letters are typed
        if len(current_text) < len(target_text):
            # Add one letter to the label text
            self.label11.text = target_text[:len(current_text) + 1]
        else:
            # Stop the typing animation
            Clock.unschedule(self.type_new_text)
            self.label11.text = ""
            time.sleep(1.5)
            # Start the typing animation for the new text
            Clock.schedule_interval(self.type_2new_text, 0)

    def type_2new_text(self, td):
        target1_text = ".Алдымен, көлік бөлісетін компанияны тауып, қолайлы көлікті таңдайық. \n Көлікті таңдаңыз: 1-Лада 2-Кия 3-Мерседес."

        # Get the current text of the label
        current1_text = self.label11.text

        # Check if all letters are typed
        if len(current1_text) < len(target1_text):
            # Add one letter to the label text
            self.label11.text = target1_text[:len(current1_text) + 1]
        else:
            # Stop the typing animation
            Clock.unschedule(self.type_2new_text)
            self.user_input = TextInput(size_hint=(0.8, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                        multiline=False)
            self.user_input.bind(on_text_validate=self.on_answer)
            self.add_widget(self.user_input)

    def switch_to_b_screen(self, dt):
        self.manager.current = 'b_screen'

    def on_answer(self, instance):
        user_answer = instance.text

        if user_answer.startswith("print('") and user_answer.endswith("')"):
            self.remove_widget(self.user_input)
            # Create a success label
            background_image = Image(source='1640159735_57_abrakadabra_fun_p_chisto_chernie_oboi_na_telefon_64.jpg',
                                     allow_stretch=True, keep_ratio=False, opacity=0.75)
            layout.add_widget(background_image)
            self.success_image = Image(source='4dcf7dbe-2d63-4f6c-bd88-f6a8b6d9a55f [problembo.com].png',
                                       size_hint=(None, None), size=(Window.width * 0.8, Window.height * 0.3),
                                       pos_hint={'center_x': 0.5, 'center_y': 0.5}, opacity=0)
            self.add_widget(self.success_image)  # Create and start the fade-in animation
            anim = Animation(opacity=0.7, duration=1.5)
            anim.start(self.success_image)
            Clock.schedule_once(self.switch_to_b_screen, 3)
            # Extract content within single quotes

        elif user_answer.startswith('print("') and user_answer.endswith('")'):
            # Extract content within double quotes

            self.remove_widget(self.user_input)
            # Create a success label
            background_image = Image(source='1640159735_57_abrakadabra_fun_p_chisto_chernie_oboi_na_telefon_64.jpg',
                                     allow_stretch=True, keep_ratio=False, opacity=0.75)
            layout.add_widget(background_image)
            self.success_image = Image(source='4dcf7dbe-2d63-4f6c-bd88-f6a8b6d9a55f [problembo.com].png',
                                       size_hint=(None, None), size=(Window.width * 0.8, Window.height * 0.3),
                                       pos_hint={'center_x': 0.5, 'center_y': 0.5}, opacity=0)
            self.add_widget(self.success_image)  # Create and start the fade-in animation
            anim = Animation(opacity=0.7, duration=1.5)
            anim.start(self.success_image)
            Clock.schedule_once(self.switch_to_b_screen, 3)


        else:
            prompt = f"Напиши подсказку на казахском языке для следующего кода {user_answer}, при этом не выводи правильный ответ, а просто укажи на синтаксические и логические ошибки"
            response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",
                prompt=prompt,
                temperature=0.7,
                max_tokens=100,
                n=1,
                stop=None,
            )

            self.label11.text = response.choices[0].text.strip()


class pAApp(App):
    def build(self):
        return pAScreen()


if __name__ == '__main__':
    pAApp().run()

