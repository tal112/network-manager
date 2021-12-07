"""

*********************************************************************************************************
*   Project: It Safe Python Course Final Project                                                        *
*   Author: Tal Sperling                                                                                *
*    Description: Network manager with 2 sections:                                                      *
*                 1) Communication Server using sockets that allows access to the clients               *
*                    and runs commands from the server (SocketConnection.py)                            *
*                 2) Network scanner that scans for all clients connected to the network (Scanner.py)   *
*                                                                                                       *
*                Each section has its own class                                                         *
*                The server is run from the flask file (app.py)                                         *
*********************************************************************************************************



"""




from flask import Flask, request, jsonify, render_template

from SocketConnection import *          #class that controls the socket connections
from Scanner import *                   #class that controls the scanning of the network
import threading
import json
import time

app = Flask("Tal Sperling - Network Manager", static_url_path="")


srv = SocketConnection("", 0, 0)
@app.before_first_request
def before_first_request():
    global srv
    srv = SocketConnection({Server I.P. Address}, 3333, 10)

@app.route('/scan_network')
def scan_network():
    return render_template('scan.html')

@app.route('/api/scan_network_ip')
def scan_network_ip():
    scanner = Scanner()
    scanner.get_local_ip_address()
    connected_machines = scanner.scan_network()

    return jsonify(connected_machines)

@app.route('/')
def index():
    t = threading.Thread(target=srv.client_manager, args=())
    t.start()
    #clients = srv.get_all_clients()

    return render_template('index.html')

@app.route('/api/run_command', methods=['POST'])
def run_command():
    global srv

    target = request.form.get("target")
    command = request.form.get("command")
    ip_address = request.form.get("ip-address")

    if target == "all":
        result = srv.run_command(target,command)
    else:
        result = srv.run_command(target, command, ip_address)


    return jsonify(result)



@app.route('/api/get_clients')
def get_clients():
    connected_clients = []

    global srv
    clients = srv.get_all_clients()


    for client in clients:
        now = time.time()
        connected_duration = client[2] - now

        connected_duration = str(connected_duration)
        clients_dict = {"client":client[1][0], "connected_duration": connected_duration}
        connected_clients.append(clients_dict)

    connected_clients = json.dumps(connected_clients)

    return jsonify(connected_clients)



debug = True
app.run(host='localhost', port=5000, debug=debug)
