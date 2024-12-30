import socket

def start_client():
    # Створюємо сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 65432))  # Підключаємося до сервера

    try:
        while True:
            message = input("Введіть повідомлення для сервера (або 'exit' для виходу): ")
            if message.lower() == 'exit':
                break
            client_socket.sendall(message.encode('utf-8'))  # Надсилаємо дані серверу
            data = client_socket.recv(1024)  # Отримуємо відповідь від сервера
            print(f"Відповідь сервера: {data.decode('utf-8')}")
    finally:
        client_socket.close()
        print("Клієнт завершив роботу.")

if __name__ == "__main__":
    start_client()
