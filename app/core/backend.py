# app/core/backend.py

from PySide6.QtCore import QObject, Slot


class Backend(QObject):
    def __init__(self):
        super().__init__()

    @Slot()
    def start_server(self):
        print("🟢 Server started (simulation)")

    @Slot()
    def send_file(self):
        print("📤 Sending file (simulation)")
