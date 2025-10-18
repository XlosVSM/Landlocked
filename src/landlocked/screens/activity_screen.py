from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button

class ActivityScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text="Activity Screen", font_size=20))
