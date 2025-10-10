import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

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
        
    def run(self):
        self.window.show()
        
        return self.exec()

if __name__ == "__main__":
    app = LandlockedApp(sys.argv)
    
    sys.exit(app.run())
