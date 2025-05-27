import threading

from PySide6.QtCore import QRunnable, Slot, Signal, QThreadPool, QObject
from PySide6.QtWidgets import QMainWindow, QFileDialog

from ui.main_window_ui import Ui_MainWindow
from network.client import FileSenderClient
from network.server import FileReceiverServer

class ServerWorker(QRunnable, QObject):
    server_started = Signal()

    def __init__(self, server: FileReceiverServer):
        QObject.__init__(self)
        QRunnable.__init__(self)
        self.server = server

    @Slot()
    def run(self):
        self.server_started.emit()
        self.server.start()

class ClientWorker(QRunnable, QObject):
    progressUpdated = Signal(int, int)
    file_sent = Signal()

    def __init__(self, client: FileSenderClient, selected_file: str):
        QObject.__init__(self)
        QRunnable.__init__(self)
        self.client = client
        self.selected_file = selected_file

    @Slot()
    def run(self):
        self.client.send_file(filepath=self.selected_file, progress_callback=self.update_progress)
        self.file_sent.emit()

    def update_progress(self, received, total):
        self.progressUpdated.emit(received, total)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.server = None
        self.setupUi(self)

        self.is_server_running = False
        self.selected_file = None
        self.threadpool = QThreadPool()

        self.ipAddressLineEdit.setText("127.0.0.1")
        self.portLineEdit.setText("5000")
        self.sendBtn.setEnabled(False)
        self.progressBar.setValue(0)

        self.startServerBtn.clicked.connect(self.toggle_server)
        self.selectFileBtn.clicked.connect(self.select_file)
        self.sendBtn.clicked.connect(self.send_file)

    def toggle_server(self):
        if not self.is_server_running:
            self.server = FileReceiverServer(self.ipAddressLineEdit.text())
            worker = ServerWorker(self.server)
            worker.server_started.connect(self.start_server)
            self.threadpool.start(worker)
        else:
            self.stop_server()


    def update_progress(self, received, total):
        self.progressBar.setValue((received / total) * 100)

    def start_server(self):
        self.log("Server started")
        self.log(f"Listening on {self.server.host}:{self.server.port}")
        self.is_server_running = True
        self.startServerBtn.setText("Stop Server")

    def stop_server(self):
        if self.server:
            self.log("Stopping server...")
            self.server.stop()
            self.server = None
        self.is_server_running = False
        self.startServerBtn.setText("Start Server")
        self.log("Server stopped")

    def select_file(self):
        self.selected_file, _ = QFileDialog.getOpenFileName()
        if self.selected_file:
            self.filePathLineEdit.setText(self.selected_file)
            self.log(f"Selected file: {self.selected_file}")
            self.sendBtn.setEnabled(True)

    def send_file(self):
        client = FileSenderClient(self.ipAddressLineEdit.text(), int(self.portLineEdit.text()))
        worker = ClientWorker(client, self.selected_file)
        worker.progressUpdated.connect(self.update_progress)
        self.threadpool.start(worker)

    def log(self, text: str):
        self.logsTextBrowser.append(text)