import socket
import logging

# Налаштовуємо логування
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[logging.StreamHandler()]
)

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('127.0.0.1', 65432))
        logging.info("Підключено до сервера.")

        while True:
            message = input("Введіть повідомлення для сервера (або 'exit' для виходу): ")
            if message.lower() == 'exit':
                logging.info("Завершення роботи клієнта.")
                break

            client_socket.sendall(message.encode('utf-8'))
            data = client_socket.recv(1024)
            logging.info(f"Відповідь сервера: {data.decode('utf-8')}")

    except ConnectionError as e:
        logging.error(f"Помилка з'єднання: {e}")
    except Exception as e:
        logging.error(f"Помилка клієнта: {e}")
    finally:
        client_socket.close()
        logging.info("Клієнт завершив роботу.")

if __name__ == "__main__":
    start_client()
