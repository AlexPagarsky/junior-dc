import socket
import argparse
from time import sleep


def wazzup(address : str, port : int):
    sock = socket.socket()
    sock.settimeout(3)
    sock.connect((address, port))
    sock.send("Wazzup!".encode("utf-8"))
    while True:
        data = sock.recv(48).decode("utf-8").strip()
        if not data:
            break
        print(data)
        sock.send(data.encode("utf-8"))
        sleep(0.01)
    sock.close()


# call with 'python3 WazzupClient.py address --port'
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Write address and port to WAZZUUUUUUUUUUP!')
    parser.add_argument('address', type=str, help='address to connect and WAZZZUUUUUUP!')
    parser.add_argument('--port', type=int, default=54321, help='port to connect and WAZZUUUUUUUP!')
    args = parser.parse_args()

    wazzup(args.address, args.port)

# WazzupClient
# Интерфейсы и наименование идентификаторов в этой задаче лежит на вашей совести.
# Написать консольное приложение.
# Нужно присоединиться по указанной паре адрес + порт, отправить "Wazzup!" и выводить все,
# что приходит в ответ до разрыва соединения. По разрыву соединения завершить приложение.
# Протестировать при помощи задачи EchoServer.
