import os
from PySide6.QtGui import QPalette
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
import sys

#####################
# Declare constants #
#####################
PHONESIZE = (360, 640)
PROJECTROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))

################
# Main classes #
################
class MainWindow(QWidget):
    """
    Main application
    """
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Landlocked!")
        self.setFixedSize(*PHONESIZE)
        
        layout = QVBoxLayout()
        
        # ===== Add interactive map =====
        map_html = """
        <!DOCTYPE html>
        <html>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
                <style>
                    html, body { margin:0; padding:0; height:100%; }
                    #map { width:100%; height:100%; }
                </style>
            </head>
            <body>
                <div id="map"></div>
                <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
                <script>
                    var map = L.map('map', { zoomControl: false, attributionControl: false }).setView([-41.3, 174.8], 5);
                    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                        maxZoom: 19
                    }).addTo(map);
                </script>
            </body>
        </html>
        """
        
        self.mapView = QWebEngineView(self)
        
        self.mapView.setHtml(map_html)
        self.mapView.setGeometry(0, 0, *PHONESIZE)
        
        # ===== Add date display =====
        
        # ===== Add reset debug button =====
        resetButton = QPushButton("Reset Game (Debug)")
        
        resetButton.setSizePolicy(resetButton.sizePolicy().horizontalPolicy(), resetButton.sizePolicy().verticalPolicy())
        resetButton.setStyleSheet("border: 1px solid black; padding: 15px;")
        resetLayout = QHBoxLayout()
        resetLayout.addStretch()
        resetLayout.addWidget(resetButton)
        resetLayout.addStretch()
        resetButton.setFixedWidth(PHONESIZE[0] // 2)
        
        resetButton.clicked.connect(lambda: self.buttonClicked("Reset"))
        
        layout.addLayout(resetLayout)
        
        # ===== Add place monument button =====
        layout.addStretch()     # Push buttons to bottom
        
        placeMonumentButton = QPushButton("Place Monument")
        
        placeMonumentButton.setSizePolicy(placeMonumentButton.sizePolicy().horizontalPolicy(), placeMonumentButton.sizePolicy().verticalPolicy())
        placeMonumentButton.setStyleSheet("border: 1px solid black; padding: 15px;")
        
        placeMonumentButton.clicked.connect(lambda: self.buttonClicked("Place Monument"))
        
        layout.addWidget(placeMonumentButton)
        
        # ===== Add bottom row screen selection buttons =====
        screenSelectionButtonRow = QHBoxLayout()
        screenSelectionButtonRow.setContentsMargins(0, 0, 0, 0)
        screenSelectionButtonRow.setSpacing(0)
        
        # Create buttons
        self.activityButton = QPushButton("Activity")
        self.mapButton = QPushButton("Map")
        self.scoreButton = QPushButton("Score")
        
        # Connect buttons
        for button in (self.activityButton, self.mapButton, self.scoreButton):
            button.setSizePolicy(button.sizePolicy().horizontalPolicy(), button.sizePolicy().verticalPolicy())
            button.setStyleSheet("border: 1px solid black; padding: 15px;")
        
        self.activityButton.clicked.connect(lambda: self.buttonClicked("Activity"))
        self.mapButton.clicked.connect(lambda: self.buttonClicked("Map"))
        self.scoreButton.clicked.connect(lambda: self.buttonClicked("Score"))
        
        # Add buttons to row
        screenSelectionButtonRow.addWidget(self.activityButton)
        screenSelectionButtonRow.addWidget(self.mapButton)
        screenSelectionButtonRow.addWidget(self.scoreButton)
        
        layout.addLayout(screenSelectionButtonRow)
        
        # ===== Set main layout =====
        self.setLayout(layout)
        
    def buttonClicked(self, selectedButton: str):
        clickOptions = {
            "Reset": lambda: None,
            "Place Monument": lambda: None,
            "Activity": lambda: None,
            "Map": lambda: None,
            "Score": lambda: None,
        }
        
        clickOptions[selectedButton]()
    
class LandlockedApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.window = MainWindow()
        
        self.darkMode = self.isDarkMode()
        
        if self.darkMode:
            self.applyDarkMode()
            
        else:
            self.applyLightMode()
        
    def isDarkMode(self) -> bool:
        palette = self.palette()
        color = palette.color(QPalette.ColorRole.Window)
        
        return color.value() < 128
        
    def applyDarkMode(self):
        darkMode = QPalette()
        
        self.setPalette(darkMode)
        
    def applyLightMode(self):
        self.setPalette(QPalette())
        
    def run(self):
        self.window.show()
        
        return self.exec()

if __name__ == "__main__":
    app = LandlockedApp(sys.argv)
    
    sys.exit(app.run())
