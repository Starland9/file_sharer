import argparse
import os
from app.network.client import FileSenderClient
from app.network.server import FileReceiverServer
from tqdm import tqdm
import threading

def run_server(host="0.0.0.0", port=5000):
    server = FileReceiverServer(host=host, port=port)
    server.start()

def run_client(ip, filepath):
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    client = FileSenderClient(ip)
    client.send_file(filepath)

def main():
    parser = argparse.ArgumentParser(description="File Transfer Utility CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Send
    send_parser = subparsers.add_parser("send", help="Send a file to a server")
    send_parser.add_argument("ip", help="IP address of the server")
    send_parser.add_argument("file", help="Path to the file to send")

    # Server
    server_parser = subparsers.add_parser("serve", help="Start a file server")
    server_parser.add_argument("--host", default="0.0.0.0", help="Host address to bind to")
    server_parser.add_argument("--port", default=5000, type=int, help="Port to bind to")

    args = parser.parse_args()
    if args.command == "send":
        run_client(args.ip, args.file)
    elif args.command == "serve":
        run_server(args.host, args.port)

if __name__ == "__main__":
    main()