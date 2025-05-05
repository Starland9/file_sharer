# app/ui/main_view.py

from pathlib import Path
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication
from app.core.backend import Backend


class MainView:
    def __init__(self):
        self.app = QApplication([])
        self.engine = QQmlApplicationEngine()

        # Crée le backend métier et l'expose au QML
        self.backend = Backend()
        self.engine.rootContext().setContextProperty("backend", self.backend)

        # Charge le fichier QML
        qml_path = Path(__file__).resolve().parent / "Main_window.qml"
        self.engine.load(str(qml_path))

        if not self.engine.rootObjects():
            raise RuntimeError("❌ Failed to load QML interface")

    def run(self):
        self.app.exec()
