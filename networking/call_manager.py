from __future__ import annotations
import socket


class CallManager:
    def __init__(self, host="0.0.0.0", port=5000):
        self.host, self.port = host, port
        self.sock = None

    def start(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)

    def accept_call(self):
        if self.sock is None:
            raise RuntimeError("CallManager is not started")
        return self.sock.accept()

    def close(self):
        if self.sock:
            self.sock.close()
            self.sock = None
