import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

PHONESIZE = (360, 640)

def createWindow():
    window = QWidget()
    window.setWindowTitle("Landlocked!")

    layout = QVBoxLayout()  # Phone layout

    label = QLabel("Hello World")
    layout.addWidget(label)
    
    button = QPushButton("Click Me!")
    button.clicked.connect(lambda: label.setText("Button Clicked!"))
    layout.addWidget(button)

    window.setLayout(layout)
    
    # Phone size for testing
    window.setFixedSize(*PHONESIZE)
    
    return window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = createWindow()
    
    window.show()
    sys.exit(app.exec())
