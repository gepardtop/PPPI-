import socket
import threading

class ChessServer:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.clients = []
    
    def handle_client(self, client_socket, addr):
        """Обработка клиента"""
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            # Broadcast хода всем игрокам
            for client in self.clients:
                client.send(data.encode())