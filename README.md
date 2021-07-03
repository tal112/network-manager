# It Safe Python Course Final Project  
## Author: Tal Sperling


Network manager with 2 sections:                                                      *
 - Communication Server using sockets that allows access to the clients        
 and runs commands from the server (SocketConnection.py)                   
 - Network scanner that scans for all clients connected to the network (Scanner.py)



## Features

Socket Communications Server:
- Automatically checks for connected clients
- Option to run system commands on all clients or 1 chosen client

Network Scanner:
- Scans the network for all connected machines by pinging from 1 - 254 on the subnet mask of the network


## Tech

The project was written in Python using the following libraries

- flask
- threading
- json
- time
- socket
- os


## Running The App

The project requires [Python](https://www.python.org/) v3+ to run.

the server is run on localhost on port: 5000
In order to start the flask server the following command is used



```sh
python app.py
```

Run the app in a browser

```sh
http://localhost:5000/
```

Run the clients on the client machines

```sh
python client.py
```
