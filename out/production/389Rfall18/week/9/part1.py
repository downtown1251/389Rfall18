#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist = open("probable-v2-top1575.txt", 'r')
wordlist = [x.strip("\n") for x in wordlist.readlines()]

# Get list of hashes found
h = open("hashes", "r")
hashes = [x for x in h.readlines()]

# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase

passwords = []

for salt in salts:
    if len(hashes) != 0:
        for pwd in wordlist:
            s = salt + pwd
            digest = hashlib.sha512(s).hexdigest()

            for h in hashes:
                if h.strip("\n") == digest:
                    passwords.append("Hash: " + digest + "\n" + "Salt: " + salt + " Password: " + pwd )
                    hashes.remove(h)

    else:
        print("<===== Passwords =====>")
        for x in passwords:
            print(x)
        break




