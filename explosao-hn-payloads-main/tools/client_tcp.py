import socket

def send_payload(message="Payload de teste TCP"):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9090))
    client.send(message.encode())
    client.close()
    print(f"Mensagem enviada: {message}")

if __name__ == '__main__':
    send_payload()
