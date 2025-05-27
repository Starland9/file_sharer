# app/main.py
from PySide6.QtWidgets import QApplication

from app.style.style import get_style
from app.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(get_style())
    window = MainWindow()
    window.show()
    app.exec()
