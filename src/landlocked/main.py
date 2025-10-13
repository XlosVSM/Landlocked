import json, os, sys
from PySide6.QtCore import Qt, QStandardPaths, QUrl
from PySide6.QtGui import QPalette
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from typing import Union

#####################
# Declare constants #
#####################
PHONESIZE = (360, 640)
PROJECTROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))

##################
# Data functions #
##################
def read_file(file_path: str) -> Union[dict, str]:
    path = os.path.join(PROJECTROOT, file_path)

    if file_path.endswith(".geojson"):
        with open(path, "r") as f:
            return json.load(f)

    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def get_user_settings_path() -> str:
    app_data_path = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.AppDataLocation)
    os.makedirs(app_data_path, exist_ok = True)
    
    return os.path.join(app_data_path, "settings.json")

def load_settings() -> dict[str, bool]:
    path = get_user_settings_path()
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    
    return {"darkMode": False}

def save_settings(settings):
    path = get_user_settings_path()
    
    try:
        with open(path, "w") as f:
            json.dump(settings, f)
            
    except Exception as E:
        print(f"Error saving settings: {E}")

################
# Main classes #
################
class MainWindow(QWidget):
    """
    Main application
    """
    
    def __init__(self, app_instance):
        super().__init__()
        self.app = app_instance
        self.setWindowTitle("Landlocked!")
        self.setFixedSize(*PHONESIZE)
        
        layout = QVBoxLayout()
        button_stylesheet = "border: 1px solid black; padding: 4px 8px; color: black; background-color: #f0f0f0;"
        
        # ===== Add interactive map =====
        self.mapView = QWebEngineView(self)
        mapHTMLPath = os.path.abspath(os.path.join(PROJECTROOT, "assets/html/index.html"))
        self.mapView.load(QUrl.fromLocalFile(mapHTMLPath))
        self.mapView.setGeometry(0, 0, *PHONESIZE)
        
        # ===== Add date display =====
        date_label = QLabel()
        
        date_label.setStyleSheet("border: 1px solid black; padding: 4px 8px; font-size: 18px; font-weight: bold; color: black; background-color: #f0f0f0;")
        date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        date_label.setText("""
        Day #/7<br>
        <span style="font-size:10px;">Time Left Today: #:##:##</span>
        """)
        date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        date_layout = QHBoxLayout()
        date_layout.addStretch()
        date_layout.addWidget(date_label)
        date_layout.addStretch()
        date_label.setFixedWidth(PHONESIZE[0] // 2)
        
        layout.addLayout(date_layout)
        
        # ===== Add reset debug button =====
        reset_button = QPushButton("Reset Game (Debug)")
        
        reset_button.setSizePolicy(
            reset_button.sizePolicy().horizontalPolicy(),
            reset_button.sizePolicy().verticalPolicy()
        )
        reset_button.setStyleSheet(button_stylesheet)
        
        reset_layout = QHBoxLayout()
        reset_layout.addStretch()
        reset_layout.addWidget(reset_button)
        reset_layout.addStretch()
        reset_button.setFixedWidth(PHONESIZE[0] // 2)
        
        reset_button.clicked.connect(lambda: self.button_clicked("Reset"))
        
        layout.addLayout(reset_layout)
        
        # ===== Add place monument button =====
        layout.addStretch()     # Push buttons to bottom
        
        place_monument_button = QPushButton("Place Monument")
        
        place_monument_button.setSizePolicy(
            place_monument_button.sizePolicy().horizontalPolicy(),
            place_monument_button.sizePolicy().verticalPolicy()
        )
        place_monument_button.setStyleSheet(button_stylesheet)
        
        place_monument_button.clicked.connect(lambda: self.button_clicked("Place Monument"))
        
        layout.addWidget(place_monument_button)
        
        # ===== Add bottom row screen selection buttons =====
        screen_selection_button_row = QHBoxLayout()
        screen_selection_button_row.setContentsMargins(0, 0, 0, 0)
        screen_selection_button_row.setSpacing(0)
        
        # Create buttons
        self.activityButton = QPushButton("Activity")
        self.mapButton = QPushButton("Map")
        self.scoreButton = QPushButton("Score")
        
        # Connect buttons
        for button in (self.activityButton, self.mapButton, self.scoreButton):
            button.setSizePolicy(button.sizePolicy().horizontalPolicy(), button.sizePolicy().verticalPolicy())
            button.setStyleSheet(button_stylesheet)
        
        self.activityButton.clicked.connect(lambda: self.button_clicked("Activity"))
        self.mapButton.clicked.connect(lambda: self.button_clicked("Map"))
        self.scoreButton.clicked.connect(lambda: self.button_clicked("Score"))
        
        # Add buttons to row
        screen_selection_button_row.addWidget(self.activityButton)
        screen_selection_button_row.addWidget(self.mapButton)
        screen_selection_button_row.addWidget(self.scoreButton)
        
        layout.addLayout(screen_selection_button_row)
        
        # ===== Set main layout =====
        self.setLayout(layout)
        
    def button_clicked(self, selected_button: str):
        click_options = {
            "Reset": lambda: None,
            "Place Monument": lambda: None,
            "Activity": lambda: None,
            "Map": lambda: None,
            "Score": lambda: None,
        }
        
        click_options[selected_button]()

class LandlockedApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.window = MainWindow(self)
        
        self.darkMode = self.is_dark_mode()
        
        if self.darkMode:
            self.apply_dark_mode()
            
        else:
            self.apply_light_mode()
        
    def is_dark_mode(self) -> bool:
        palette = self.palette()
        color = palette.color(QPalette.ColorRole.Window)
        
        return color.value() < 128
        
    def apply_dark_mode(self):
        dark_mode = QPalette()
        
        self.setPalette(dark_mode)
        
    def apply_light_mode(self):
        self.setPalette(QPalette())

    def run(self):
        self.window.show()
        
        return self.exec()

if __name__ == "__main__":
    app = LandlockedApp(sys.argv)
    
    sys.exit(app.run())
