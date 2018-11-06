#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib
import re

host = "142.93.117.193"   # IP address or URL
port = 7331  # port

regex1 = re.compile('sha\d{1,3} | md\d')
regex2 = re.compile('\w*\W*$')
regex3 = re.compile('CMSC389R.*')

continueLooping = True
# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# receive some data
data = s.recv(1024).decode()

while continueLooping:

    alg = regex1.search(data)
    alg = alg.group().strip()

    username = regex2.search(data)
    username = (username.group().split())[0]

    h = hashlib.new(alg, username.encode())

    digest = h.hexdigest()
    s.send(digest.encode())
    s.send("\n".encode())
    data = s.recv(1024).decode()

    if "Correct!" not in data:
        continueLooping = False
    elif "You win!" in data:
        flag = regex3.search(data).group().strip()
        print(flag)
        continueLooping = False

# close the connection
s.close()
