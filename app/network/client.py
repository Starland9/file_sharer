import socket
import os
import json

from tqdm import tqdm


class FileSenderClient:
    def __init__(self, server_ip, server_port=5000):
        self.server_ip = server_ip
        self.server_port = server_port

    def send_file(self, filepath, progress_callback=None):
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")

        filename = os.path.basename(filepath)
        filesize = os.path.getsize(filepath)

        try:
            # Connect to server
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((self.server_ip, self.server_port))
                print(f"Connected to {self.server_ip}:{self.server_port}")

                # Send file metadata
                metadata = {"filename": filename, "filesize": filesize}
                client_socket.sendall(json.dumps(metadata).encode("utf-8"))

                # Send file data
                with open(filepath, "rb") as f, tqdm(total=filesize, unit="B", unit_scale=True, unit_divisor=1024, desc=filename) as progress_bar:
                    while True:
                        chunk = f.read(4096)
                        if not chunk:
                            break
                        client_socket.sendall(chunk)
                        progress_bar.update(len(chunk))
                        if progress_callback:
                            progress_callback(progress_bar.n, progress_bar.total)

                # Confirm file reception
                response = client_socket.recv(1024).decode("utf-8")
                if response == "RECEIVED":
                    print(f"✅ File {filename} sent successfully")
                else:
                    print(f"⚠️ No confirmation received from server")

        except Exception as e:
            print(f"❌ Error sending file: {e}")
