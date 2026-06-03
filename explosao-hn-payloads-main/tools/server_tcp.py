import socket
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9090))
    server.listen(5)
    logging.info("Servidor TCP rodando na porta 9090")

    while True:
        conn, addr = server.accept()
        logging.info(f"Conexão recebida de {addr}")
        data = conn.recv(1024)
        if data:
            logging.info(f"Dados recebidos: {data.decode()}")
        conn.close()

if __name__ == '__main__':
    start_server()
