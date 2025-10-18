from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button

class ScoreScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text="Score Screen", font_size=20))
