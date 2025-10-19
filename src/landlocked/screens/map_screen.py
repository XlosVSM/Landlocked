from kivy.graphics import Color, Rectangle, RoundedRectangle
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
            height = 120,
            pos_hint = {'top': 1}
        )

        with top_bar.canvas.before:
            Color(0.15, 0.15, 0.15, 0.7)
            self.top_bg = Rectangle(size = top_bar.size, pos = top_bar.pos)

        top_bar.bind(size = lambda i, v: setattr(self.top_bg, 'size', v))
        top_bar.bind(pos = lambda i, v: setattr(self.top_bg, 'pos', v))

        day_box = BoxLayout(
            orientation = "vertical",
            size_hint = (0.7, None),
            height = 80,
            pos_hint = {"center_x": 0.5, "top": 0.95},
            padding = 5,
            spacing = 2
        )

        with day_box.canvas.before:
            Color(1, 1, 1, 1)
            self.day_box_bg = RoundedRectangle(size = day_box.size, pos = day_box.pos, radius = [20])
        day_box.bind(size = lambda i, v: setattr(self.day_box_bg, 'size', v))
        day_box.bind(pos = lambda i, v: setattr(self.day_box_bg, 'pos', v))

        day_label = Label(
            text = "Day #/7",
            font_size = "20sp",
            color = (0, 0, 0, 1),
            bold = True
        )
        time_label = Label(
            text = "TIME LEFT TODAY: ##:##:##",
            font_size = "14sp",
            color = (0, 0, 0, 1)
        )

        day_box.add_widget(day_label)
        day_box.add_widget(time_label)

        # ===== Add reset button =====
        reset_button = Button(
            text = "Reset Game (Debug)",
            size_hint = (0.5, None),
            height = 40,
            pos_hint = {"center_x": 0.5, "y": 0.02},
            background_color = (0.3, 0.6, 1, 1),
            color = (1, 1, 1, 1)
        )

        top_bar.add_widget(day_box)
        top_bar.add_widget(reset_button)
        root.add_widget(top_bar)

        # ===== Add Place Monument button =====
        monument_box = BoxLayout(
            orientation = "vertical",
            size_hint = (1, None),
            height = 120,
            pos_hint = {"center_x": 0.5, "y": 0.12},
            spacing = 5
        )

        monument_label = Label(
            text = "Area Is Unclaimed!",
            font_size = "16sp",
            color = (1, 1, 1, 1),
            size_hint_y = None,
            height = 30
        )

        monument_button = Button(
            text = "Place Monument!",
            font_size = "18sp",
            size_hint = (0.8, None),
            height = 55,
            pos_hint = {"center_x": 0.5},
            background_color = (0.3, 0.6, 1, 1),
            color = (1, 1, 1, 1)
        )

        monument_box.add_widget(monument_label)
        monument_box.add_widget(monument_button)
        root.add_widget(monument_box)

        self.add_widget(root)
