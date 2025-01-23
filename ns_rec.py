import socket
import sys



name = input("Please input a website: ")# retrieves input from user
host_IP = socket.gethostbyname(name)

print(name + " IP address: " + host_IP) # prints IP address

