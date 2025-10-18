###############################################
# Adjust Kivy window settings for development #
###############################################
from kivy.config import Config

PHONESIZE = (360, 640)
Config.set('graphics', 'width', str(PHONESIZE[0]))
Config.set('graphics', 'height', str(PHONESIZE[1]))
Config.set('graphics', 'resizable', '0')

###########
# Imports #
###########
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy_garden.mapview import MapView, MapMarker

# ===== Import screens =====
from screens.activity_screen import ActivityScreen
from screens.map_screen import MapScreen
from screens.score_screen import ScoreScreen

###########
# Screens #
###########
class MapApp(App):
    def build(self):
        root = BoxLayout(orientation = 'vertical')

        # Screen Manager
        self.sm = ScreenManager()
        self.sm.add_widget(ActivityScreen(name = "activity"))
        self.sm.add_widget(MapScreen(name = "map"))
        self.sm.add_widget(ScoreScreen(name = "score"))
        self.sm.current = "map"

        # Bottom button bar
        button_bar = BoxLayout(size_hint_y = 0.1)
        activity_btn = Button(text = "Activity")
        map_btn = Button(text = "Map")
        score_btn = Button(text = "Score")

        # Switch screens
        activity_btn.bind(on_press = lambda x: setattr(self.sm, 'current', "activity"))
        map_btn.bind(on_press = lambda x: setattr(self.sm, 'current', "map"))
        score_btn.bind(on_press = lambda x: setattr(self.sm, 'current', "score"))

        button_bar.add_widget(activity_btn)
        button_bar.add_widget(map_btn)
        button_bar.add_widget(score_btn)

        # Add widgets to root
        root.add_widget(self.sm)
        root.add_widget(button_bar)

        return root


if __name__ == "__main__":
    MapApp().run()
