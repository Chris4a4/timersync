import socket
import time
import threading


def main():
    with open('settings.txt', 'r') as s:
        s.readline()
        host_ip = s.readline()[:-1]
        s.readline()
        num_timers = int(s.readline())
        s.readline()
        update_freq = int(s.readline())
        s.readline()
        base_port = int(s.readline())

    host = [None] * num_timers
    local = [None] * num_timers
    for i in range(num_timers):
        host[i] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host[i].connect((host_ip, base_port + i))
        print(f'Connected to host timer #{i + 1}')

        local[i] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        local[i].connect(("localhost", base_port + i))
        print(f'Connected to local timer #{i + 1}')

    Sender(host, local, update_freq).start()
    Receiver(host, local).start()


class Sender(threading.Thread):
    def __init__(self, host, local, update_freq):
        threading.Thread.__init__(self)
        self.host = host
        self.local = local
        self.update_freq = update_freq

    def run(self):
        while True:
            for h, l in zip(self.host, self.local):
                h.send(b"getcurrentgametime\r\n")

            time.sleep(1 / self.update_freq)


class Receiver(threading.Thread):
    def __init__(self, host, local):
        threading.Thread.__init__(self)
        self.host = host
        self.local = local

    def run(self):
        while True:
            for h, l in zip(self.host, self.local):
                data = h.recv(4096).decode('UTF-8')[:-2]

                l.send(f"setgametime {data}\r\n".encode('UTF-8'))


if __name__ == "__main__":
    main()
