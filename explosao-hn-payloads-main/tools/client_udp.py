import socket

def send_udp(message="Payload de teste UDP"):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode(), ('127.0.0.1', 9021))
    print(f"Pacote UDP enviado: {message}")

if __name__ == '__main__':
    send_udp()
