#!/usr/bin/python3

import subprocess


class FExpress:
    def connect(self):
        disconnect = subprocess.run(
            ["expressvpn", "connect"], capture_output=True)
        disco = disconnect.stdout
        dance = disco.split(b"[")
        hall = len(dance)
        if hall > 2:
            print("Connected")
            return "0"
        elif hall == 1:
            print("AlreadyConnected")
            return "1"

    def disconnect(self):
        disconnect = subprocess.run(
            ["expressvpn", "disconnect"], capture_output=True)
        disco = disconnect.stdout
        dance = disco.split(b"[")
        hall = len(dance)
        if hall == 5:
            print("Disconnected")
            return "0"
        elif hall == 1:
            print("NotConnected")
            return "1"

    def status(self):
        status = subprocess.run(["expressvpn", "status"], capture_output=True)
        ace = status.stdout
        spade = ace.split(b"[")
        lspade = len(spade)
        if lspade == 3:
            print("Disconnected")
            return "1"
        elif lspade == 5:
            print("Connected")
            return "0"
        else:
            return "-1"

# if __name__ == "__main__":
#     fe = FExpress()
#     fe.disconnect()
