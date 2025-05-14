# app/core/backend.py
from PySide6.QtCore import QObject, Signal, Slot
import socket
import threading

class Backend(QObject):
    progressUpdated = Signal(float)  # Signal pour mettre à jour la barre de progression
    transferCompleted = Signal(str)  # Signal pour notifier la fin d'un transfert

    def __init__(self):
        super().__init__()
        self.server = None
        self.server_thread = None
        self.is_server_running = False

    @Slot(str, int)
    def startServer(self, host: str, port: int):
        if not self.is_server_running:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((host, port))
            self.server_thread = threading.Thread(target=self._run_server)
            self.server_thread.start()
            self.is_server_running = True

    @Slot()
    def stopServer(self):
        if self.is_server_running:
            self.is_server_running = False
            if self.server:
                self.server.close()
            if self.server_thread:
                self.server_thread.join()

    @Slot(str)
    def sendFile(self, filepath: str):
        # Implémentation de l'envoi de fichier
        # Utilisez self.progressUpdated.emit() pour mettre à jour la progression
        # Utilisez self.transferCompleted.emit() quand le transfert est terminé
        pass

    def _run_server(self):
        self.server.listen(5)
        while self.is_server_running:
            try:
                client, addr = self.server.accept()
                # Gérer la réception du fichier
            except:
                break