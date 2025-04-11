from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
import sys

def main():
    app = QApplication(sys.argv)
    win = QWidget()
    win.setWindowTitle("Laporte CARS Utility")
    layout = QVBoxLayout()
    layout.addWidget(QLabel("Laporte CARS Utility Loaded"))
    win.setLayout(layout)
    win.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
