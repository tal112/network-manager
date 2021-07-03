import os
import threading

#Class that scans the network for all connected machines
class Scanner:
    def __init__(self):
        self.connected_machines = []



    def get_local_ip_address(self):
        ip_address = "I.P. Address Not Found"
        ipcon = os.popen("ipconfig")

        for line in ipcon.readlines():
            if "IPv4 Address. . . . . . . . . . ." in line:
                line_split = line.split(":")
                ip_address = line_split[1]
                ip_address = ip_address[:-1]

        ip_address = ip_address.replace(" ", "")
        self.ip_address = ip_address
        ip_template = ".".join(ip_address.split('.')[0:-1]) + '.'

        self.ip_template = ip_template

    def pinger(self, ip_address, lock):

        result = os.popen("ping {0} -n 1".format(ip_address)).read()

        if "TTL" in result:
            with lock:
                print(ip_address)
                if ip_address != self.ip_address:
                    machines_dict = {"ip_address": ip_address}
                    self.connected_machines.append(machines_dict)


    def scan_network(self):

        self.connected_machines.clear()

        threads = []

        lock = threading.Lock()

        for i in range(254):
            ip_address = self.ip_template + str(i)
            t = threading.Thread(target=self.pinger, args=(ip_address, lock))
            threads.append(t)
            t.start()

        for thread in threads:
            thread.join()

        return self.connected_machines