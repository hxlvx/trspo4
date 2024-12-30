import socket

def start_server():
    # Створюємо сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 65432))  # Прив'язуємо сокет до IP і порту
    server_socket.listen(1)  # Переходимо в режим очікування з'єднання
    print("Сервер запущений і чекає на підключення...")

    conn, addr = server_socket.accept()  # Приймаємо вхідне з'єднання
    print(f"Підключено до клієнта: {addr}")

    while True:
        data = conn.recv(1024)  # Отримуємо дані від клієнта
        if not data:
            break
        print(f"Отримано: {data.decode('utf-8')}")
        conn.sendall(data)  # Відправляємо дані назад клієнту

    conn.close()
    server_socket.close()
    print("Сервер завершив роботу.")

if __name__ == "__main__":
    start_server()
