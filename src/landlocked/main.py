import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtGui import QPalette

PHONESIZE = (360, 640)

class MainWindow(QWidget):
    """
    Main application
    """
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Landlocked!")
        self.setFixedSize(*PHONESIZE)
        
        layout = QVBoxLayout()
        
        self.label = QLabel("Hello World")
        layout.addWidget(self.label)
        
        self.button = QPushButton("Click Me!")
        self.button.clicked.connect(self.on_button_clicked)
        layout.addWidget(self.button)

        self.setLayout(layout)
        
    def on_button_clicked(self):
        """
        Handle button click
        """
        
        self.label.setText("Button Clicked!")
    
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
