import time

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

import street
import openai  # Install using: pip install openai

# Set up your OpenAI API key
openai.api_key = 'API-KEY-HERE'  # Replace with your actual OpenAI API key



levels=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global layout
        layout = FloatLayout()
        LabelBase.register(name='CustomFont', fn_regular='DRKrapkaRhombus-FontSize10px.ttf')
        background_image = Image(source='photo_5190922462521579832_y.jpg', allow_stretch=True, keep_ratio=False)
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
        target_text = "Сіз ояңдыңызба? Уақыт келді."

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
            self.label11.text = ""
            time.sleep(1.5)
            # Start the typing animation for the new text
            Clock.schedule_interval(self.type_new_text, 0)

    def type_new_text(self, td):
        # Define the text to be typed
        target_text = "Мен Ж.И. көмекшімін. Менің мақсатым-саған осы әлемде жайлы болуға\n және елорда астанасына жетуге көмектесу. Технология маңызды рөл\n атқарады және Мен сізді бағдарламалауға мүдделі екеніңізді білемін.\n Қарапайымнан бастайық. Балықшыға барыңыз. Ол сізге осы\n сапардың алғашқы қадамын жасауға көмектеседі."

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
        target1_text = "... сізге шығу керек. \nЕң басты функция - print(),бұл сіздің босату жолыңыз болады.\n Осыны жазыңыз..."

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

    def switch_to_third_screen(self, dt):
        self.manager.current = 'third_screen'
    def hint(self, td):
            target1_text = td

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
    def on_answer(self, instance):
        user_answer = instance.text
        answer = 'print()'
        if user_answer == 'print()':

            self.remove_widget(self.user_input)
            background_image = Image(source='1640159735_57_abrakadabra_fun_p_chisto_chernie_oboi_na_telefon_64.jpg',
                                         allow_stretch=True, keep_ratio=False, opacity=0.75)
            layout.add_widget(background_image)
            self.success_image = Image(source='4dcf7dbe-2d63-4f6c-bd88-f6a8b6d9a55f [problembo.com].png',
                                           size_hint=(None, None), size=(Window.width * 0.8, Window.height * 0.3),
                                           pos_hint={'center_x': 0.5, 'center_y': 0.5}, opacity=0)
            self.add_widget(self.success_image)  # Create and start the fade-in animation
            anim = Animation(opacity=0.7, duration=1.5)
            anim.start(self.success_image)
            Clock.schedule_once(self.switch_to_third_screen, 3)
            levels[0]=1

        else:
            prompt = f"Напиши подсказку на казахском языке для следующего кода {user_answer}, вот правильный код: {answer}, при этом не выводи правильный ответ, а просто укажи на синтаксические и логические ошибки"
            response = openai.Completion.create(
                    engine="gpt-3.5-turbo-instruct",
                    prompt=prompt,
                    temperature=0.7,
                    max_tokens=100,
                    n=1,
                    stop=None,
                )

            self.label11.text = response.choices[0].text.strip()





class SecondApp(App):
    def build(self):

        return SecondScreen()


if __name__ == '__main__':
    SecondApp().run()
