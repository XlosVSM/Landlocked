from kivy.uix.screenmanager import Screen
from kivy_garden.mapview import MapView, MapMarker

class MapScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        mapview = MapView(zoom=12, lat=-41.2865, lon=174.7762)
        marker = MapMarker(lat=-41.2865, lon=174.7762)
        mapview.add_marker(marker)
        self.add_widget(mapview)
