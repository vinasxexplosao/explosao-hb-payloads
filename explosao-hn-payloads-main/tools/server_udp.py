import socket
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def start_udp():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', 9021))
    logging.info("Servidor UDP rodando na porta 9021")

    while True:
        data, addr = sock.recvfrom(1024)
        logging.info(f"Pacote UDP de {addr}: {data.decode()}")

if __name__ == '__main__':
    start_udp()
