import time

import openai
from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput


class FourthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global layout
        layout = FloatLayout()
        LabelBase.register(name='CustomFont', fn_regular='DRKrapkaRhombus-FontSize10px.ttf')

        # Set the background image
        background = Image(source='port.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        # Create the dialog image
        dialog_image = Image(source='93586-box-angle-brand-game-video-dialog-mother.png',
                             size_hint=(None, None), size=(1300, 1000), pos=(-169, -340))
        layout.add_widget(dialog_image)

        # Create the initial image
        self.initial_image = Image(source='Upscales.ai_1711358277323.png', allow_stretch=True, keep_ratio=True,
                                   size_hint=(None, None), size=(250, 250), pos=(750, 139))
        layout.add_widget(self.initial_image)

        # Create the label for typing text
        self.label1111 = Label(text='', font_size='20sp',  font_name='CustomFont',  pos_hint={'center_x': 0.5, 'center_y': 0.1})
        layout.add_widget(self.label1111)
        self.label12 = Label(text='Балықшы', font_size='20sp',  font_name='CustomFont',  pos_hint={'center_x': 0.14, 'center_y': 0.255})
        layout.add_widget(self.label12)

        # Schedule the appearance of the new label after 3 seconds

        self.add_widget(layout)

        # Start typing animation
    def on_enter(self):
        # Schedule the typing animation when the screen is entered
        Clock.schedule_interval(self.type_text, 0)
        Clock.schedule_once(lambda dt: self.add_new_label(), 3)
    def add_new_label(self):
            # Create a new label text
        self.label13 = Label(text='', font_size='15sp', pos_hint={'center_x': 0.5, 'center_y': 0.875},
                                 color=(0, 0, 0, 1))
        layout.add_widget(self.label13)

            # Start typing animation for the delayed text
        Clock.schedule_interval(self.type_delayed_text, 0.1)

    def type_delayed_text(self, dt):
        target_text = "Python тілінде print() функциясын қалай \nқолданатынымызды есте сақтаңыз. Бірақ '' туралы\n ұмытпаңыз, себебі сіз str деректер түрін жазып жатырсыз."
        current_text = self.label13.text
        if len(current_text) < len(target_text):
            self.label13.text = target_text[:len(current_text) + 1]
        else:
            Clock.unschedule(self.type_delayed_text)
            self.user_input = TextInput(size_hint=(0.8, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                        multiline=False)
            self.user_input.bind(on_text_validate=self.on_answer)
            layout.add_widget(self.user_input)

    def on_answer(self, instance):
        user_answer = instance.text.strip()
        if user_answer.startswith("print('") and user_answer.endswith("')"):
            # Extract content within single quotes
            user_input_text = user_answer[7:-2]
            self.handle_valid_input(user_input_text)
        elif user_answer.startswith('print("') and user_answer.endswith('")'):
            # Extract content within double quotes
            user_input_text = user_answer[7:-2]
            self.handle_valid_input(user_input_text)

        else:
            prompt = f"Напиши подсказку на казахском языке для следующего кода {user_answer} при этом не выводи правильный ответ, а просто укажи на синтаксические и логические ошибки"
            response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",
                prompt=prompt,
                temperature=0.7,
                max_tokens=100,
                n=1,
                stop=None,
            )

            self.label13.text = response.choices[0].text.strip()

    def handle_valid_input(self, user_input_text):
        # Remove the TextInput widget
        layout.remove_widget(self.user_input)

        # Remove the question label text
        self.label1111.text = ""

        # Display the new text after successful input
        if user_input_text:
            Clock.schedule_once(lambda dt: self.display_new_text(user_input_text), 1)
        else:
            print("Invalid input. Content inside print() should not be empty.")

    def display_new_text(self, user_input_text):
        # Create and display the new text label
        new_text_label = Label(
            text=f"Сәлем {user_input_text} Мәссаған! Бұл жаңалық...\n Бірақ сіз білесіз бе? Менде ешкімге керек емес\n ескі ағаш қайық болды. Сіз оны алып, сапарыңызда \nсізге қызмет етуге рұқсат ете аласыз",
            font_size='15sp',  font_name='CustomFont',  pos_hint={'center_x': 0.5, 'center_y': 0.1})
        layout.add_widget(new_text_label)



        self.manager.current = 'd_screen'

    def type_text(self, dt):
        target_text = "Сен кімсің? Саған не керек? \n Мен жай ғана балықшымын..."
        current_text = self.label1111.text
        if len(current_text) < len(target_text):
            self.label1111.text = target_text[:len(current_text) + 1]
        else:
            Clock.unschedule(self.type_text)
            time.sleep(1)

            # Schedule the appearance of new images and start typing new text
            Clock.schedule_once(self.add_new_image, 1)
            Clock.schedule_once(self.update_target_text, 1)  # Add this line to update the label text

    def add_new_image(self, dt):
        # Create the new image
        new_image = Image(source='image_2024-03-25_11-48-46.png', allow_stretch=True, keep_ratio=True,
                          size_hint=(None, None), size=(200, 200), pos=(60, 550))
        layout.add_widget(new_image)

        # Create the new image1
        new_image1 = Image(source='cbc429aa4c976ac.png', allow_stretch=True, keep_ratio=True,
                           size_hint=(None, None), size=(600, 600), pos=(200, 350))
        layout.add_widget(new_image1)

    def update_target_text(self, dt):
        # Update the label text with the original target text
        self.label1111.text = "Сен кімсің? Саған не керек? \n Мен жай ғана балықшымын..."


class FourthApp(App):
    def build(self):
        return FourthScreen()


if __name__ == '__main__':
    FourthApp().run()