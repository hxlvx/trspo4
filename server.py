import socket
import logging

# Налаштовуємо логування
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[logging.StreamHandler()]
)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(('127.0.0.1', 65432))
        server_socket.listen(1)
        logging.info("Сервер запущений і чекає на підключення...")

        conn, addr = server_socket.accept()
        logging.info(f"Підключено до клієнта: {addr}")

        while True:
            data = conn.recv(1024)
            if not data:
                logging.info("Клієнт закрив з'єднання.")
                break
            logging.info(f"Отримано від клієнта: {data.decode('utf-8')}")
            response = f"Сервер отримав: {data.decode('utf-8')}"
            conn.sendall(response.encode('utf-8'))

    except Exception as e:
        logging.error(f"Помилка сервера: {e}")
    finally:
        conn.close()
        server_socket.close()
        logging.info("Сервер завершив роботу.")

if __name__ == "__main__":
    start_server()
