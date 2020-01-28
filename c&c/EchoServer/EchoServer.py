from time import sleep
import threading
import socket


class EchoServer:

    def __init__(self, port : int = 54321):
        self.address = ('localhost', port)
        self.socket = socket.create_server(self.address)
        self.running = False

    def is_running(self) -> bool:
        return self.running

    def get_port(self) -> int:
        return self.address[1]

    def start(self) -> None:

        def speak_with(cl):
            while True:
                sleep(0.01)   # CPU usage ~100% and insane temperatures on my laptop without this line
                data = cl.recv(48).decode("utf-8").strip()
                if data != "":
                    cl.send(f"{data}\n".encode("utf-8"))
                    if data == "disconnect":
                        cl.close()
                        break

        def look_for_connect():
            while self.running:
                cl, addr = self.socket.accept()
                # cl.send("EchoServer, input 48:\n".encode("utf-8"))
                thr = threading.Thread(target=speak_with, args=(cl,))
                thr.start()

        self.running = True
        self.socket.listen(5)

        main = threading.Thread(target=look_for_connect, daemon=True)
        main.start()
        out = input("Write 'stop' to stop echo: ")
        if out.lower() == "stop":
            self.stop()

    def stop(self) -> None:
        self.running = False
        self.socket.close()


if __name__ == "__main__":
    server = EchoServer()
    print(server.is_running())
    server.start()
    server.is_running()
    server.stop()
    server.is_running()

# EchoServer
# При запуске сервер начинает слушать заданный TCP-порт. При подключении клиента следует принять соединение
# и затем в цикле выполнять следующую последовательность:
# - считать из сокета полученные данные
# - отправить их обратно в неизменном виде
# Продолжаем этот цикл до самостоятельного отключения клиента или получения команды "disconnect\n".
# При получении команды "disconnect\n" сервер должен закрыть клиентский сокет.
# Проверить корректную работу сервера при помощи команды telnet.
# Проверить, что сервер успешно обслуживает более одного одновременного соединения.
#
# CODE
# class EchoServer {
#    public EchoServer() {
#        this(DEFAULT_PORT);
#    }
#    public EchoServer(int port);
#    public boolean isRunning();
#    public int getPort();
#    public void start();
#    public void stop();
# }
#
#
# Usage:
# CODE
# EchoServer server = new EchoServer();
#
# server.isRunning();      // false
# server.getPort();        // value of DEFAULT_PORT
#
# server.start();
# server.isRunning()      // true
# server.stop()
# server.isRunning()      // false
#
# server = new EchoServer(54321);
# server.getPort()        // 54321
# server.isRunning()      // false
# server.start()
