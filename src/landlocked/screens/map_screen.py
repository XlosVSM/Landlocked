from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy_garden.mapview import MapView

class MapScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        root = FloatLayout()

        # ===== Load in map =====
        mapview = MapView(zoom = 12, lat = -41.2865, lon = 174.7762)
        root.add_widget(mapview)

        # ===== Add top widgets =====
        top_bar = BoxLayout(
            orientation = 'vertical',
            size_hint = (1, None),
            height = 100,
            padding = (10, 10),
            spacing = 5,
            pos_hint = {'top': 1}
        )

        day_label_box = BoxLayout(size_hint_y=None, height=30)
        with day_label_box.canvas.before:
            Color(0, 0, 0, 0.6)  # translucent black
            self.day_bg = Rectangle(size=day_label_box.size, pos=day_label_box.pos)

        day_label_box.bind(size=lambda i, v: setattr(self.day_bg, 'size', v))
        day_label_box.bind(pos=lambda i, v: setattr(self.day_bg, 'pos', v))

        day_label = Label(
            text = "Day # / 7",
            font_size = "18sp",
            color = (1, 1, 1, 1),
            size_hint_y = None,
            height = 30
        )
        day_label_box.add_widget(day_label)

        time_label = Label(
            text = "Time Left Today: ##:##:##",
            font_size = "16sp",
            color = (1, 1, 1, 1),
            size_hint_y = None,
            height = 25
        )

        reset_button = Button(
            text = "Reset Game (Debug)",
            size_hint_y = None,
            height = 35
        )

        top_bar.add_widget(day_label_box)
        top_bar.add_widget(time_label)
        top_bar.add_widget(reset_button)
        root.add_widget(top_bar)

        # === Add Place Monument button ===
        place_button = Button(
            text="Place Monument",
            size_hint = (0.8, None),
            height = 50,
            pos_hint = {'center_x': 0.5, 'y': 0.05}
        )

        root.add_widget(place_button)
        self.add_widget(root)
