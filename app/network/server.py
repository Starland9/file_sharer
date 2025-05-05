import socket
import threading
import os
import json


class FileReceiverServer:
    def __init__(self, host="0.0.0.0", port=5000, save_dir="received_files"):
        """
        Create a FileReceiverServer instance.

        Parameters
        ----------
        host : str
            The address to bind to. Defaults to 0.0.0.0 (all available network interfaces)
        port : int
            The port to bind to. Defaults to 5000
        save_dir : str
            The directory to put received files in. Defaults to "received_files"
        """
        self.host = host
        self.port = port
        self.save_dir = save_dir
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        os.makedirs(self.save_dir, exist_ok=True)

    def start(self):
        """
        Start the server.

        This method will block until a KeyboardInterrupt is received (i.e. Ctrl+C is pressed).
        When this happens, the server will shut down cleanly.
        """
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Listening on {self.host}:{self.port}")

        try:
            while True:
                client_socket, client_address = self.server_socket.accept()
                threading.Thread(target=self.handle_client, args=(
                    client_socket, client_address)).start()
        except KeyboardInterrupt:
            print("❌ Server stopped")
        finally:
            self.stop()

    def stop(self):
        """
        Stop the server.

        This method will cleanly shut down the server, closing the server socket.

        It is not necessary to call this method explicitly, as it is called automatically
        when the start method receives a KeyboardInterrupt (i.e. Ctrl+C is pressed).
        """
        self.server_socket.close()

    def handle_client(self, client_socket: socket.socket, client_address):
        """
        Handle an incoming client connection.

        This method receives file metadata and file data from a client, saves the file
        to the specified directory, and sends a confirmation message back to the client.

        Parameters
        ----------
        client_socket : socket.socket
            The socket object representing the client connection.
        client_address : socket._RetAddress
            The address of the client.

        Exceptions
        ----------
        Exception
            If an error occurs during file reception or processing, it is caught and
            logged, and the client socket is closed.
        """
        print(f"Received connection from {client_address}")

        try:
            # Receive file metadata
            header = client_socket.recv(1024).decode("utf-8")
            metadata = json.loads(header)
            filename = metadata["filename"]
            filesize = metadata["filesize"]

            # Receive file data
            print(f"Receiving {filename} ({filesize} bytes)")

            filepath = os.path.join(self.save_dir, filename)

            with open(filepath, "wb") as f:
                remaining = filesize
                while remaining > 0:
                    chunk = client_socket.recv(min(4096, remaining))
                    if not chunk:
                        break
                    f.write(chunk)
                    remaining -= len(chunk)

            print(f"File saved to {filepath}")
            client_socket.sendall(b"RECEIVED")
        except Exception as e:
            print(f"❌ Error with address {client_address} : {e}")
        finally:
            client_socket.close()
