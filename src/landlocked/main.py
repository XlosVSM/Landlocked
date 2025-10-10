import os
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PySide6.QtGui import QPalette
import sys

#####################
# Declare constants #
#####################
PHONESIZE = (360, 640)
PROJECTROOT = os.path.dirname(os.path.join(os.path.dirname(__file__), '../../..'))

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
        self.mapView = QWebEngineView(self)
        
        self.mapView.setUrl("https://www.openstreetmap.org")
        self.mapView.setGeometry(0, 0, *PHONESIZE)
        
        # ===== Add bottom row buttons =====
        layout.addStretch()     # Push buttons to bottom
        
        buttonRow = QHBoxLayout()
        buttonRow.setContentsMargins(0, 0, 0, 0)
        buttonRow.setSpacing(0)
        
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
        buttonRow.addWidget(self.activityButton)
        buttonRow.addWidget(self.mapButton)
        buttonRow.addWidget(self.scoreButton)
        
        layout.addLayout(buttonRow)
        
        # ===== Set main layout =====
        self.setLayout(layout)
        
    def buttonClicked(self, buttonName: str):
        """
        Handle button click
        """
        
        pass
    
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
        
    def applyLightMode(self):
        self.setPalette(QPalette())
        
    def run(self):
        self.window.show()
        
        return self.exec()

if __name__ == "__main__":
    app = LandlockedApp(sys.argv)
    
    sys.exit(app.run())
