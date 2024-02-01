import socket
import threading

class BridgeServer:
    def __init__(self, bridge_host, bridge_port):
        self.bridge_host = bridge_host
        self.bridge_port = bridge_port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((bridge_host, bridge_port))
        self.server_socket.listen(5)
        print(f"Bridge Server started on {bridge_host}:{bridge_port}")

    def start(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection established from {client_address}")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                # Gelen veriyi işleyebilir ve diğer taraftaki cihaza iletebilirsiniz.
                print(f"Received data: {data.decode()}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()

if __name__ == "__main__":
    bridge_host = "0.0.0.0"  # Tüm arayüzleri dinle
    bridge_port = 5555  # Bridge Server'ın dinlediği port

    bridge_server = BridgeServer(bridge_host, bridge_port)
    bridge_server.start()
