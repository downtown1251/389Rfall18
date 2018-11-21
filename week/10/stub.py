#!/usr/bin/env python2
# from the git repo
import md5py
import socket
import time
#####################################
### STEP 1: Calculate forged hash ###
#####################################

host = "142.93.118.186" # IP address here
port = 1234  # Port here
message = "Country Kitchen Buffet"   # original message here

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
s.connect((host, port))
d = s.recv(1024)
s.send('1\n')
d = s.recv(1024)
s.send(message+'\n')
d = s.recv(1024)
time.sleep(1)
l = (d.split('Your hash: '))
legit = l[1].strip('\n')
print(legit)
d = s.recv(1024)


# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.decode('hex'))

malicious = "South Park"  # put your malicious message here

# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()
print(fake_hash)


#############################
### STEP 2: Craft payload ###
#############################

# secret is <redacted> bytes long (48 bits)
# each block in MD5 is 512 bits long
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a byte with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits

# Calculate Necessary Lengths Padding
numEndian = 8
totalLength = 64
multipler = 2
for i in range(1, 1000):
    print("Using Secret Length: " + str(i))
    lenSecret = i
    if lenSecret + len(message) + 9 > totalLength:
        totalLength = 64 * multipler
        multipler += 1
    numBitOne = 1
    numZeroes = totalLength - lenSecret - len(message) - numBitOne - numEndian
    paddingLength = totalLength - lenSecret - len(message)

    # Create Padding
    padding = '\x80'
    print("The length of the message: " + str(len(message)))
    print("The number of zeroes being appended: " + str(numZeroes))
    for x in range(0, numZeroes):
        padding += '\x00'

    padding += ('\xb0\x00\x00\x00\x00\x00\x00\x00')
    print("Total Length of padding: " + str(len(padding)))
    print("The total length of Secret + Message + Padding: " + str(lenSecret + len(message) + len(padding)))


    # payload is the message that corresponds to the hash in `fake_hash`
    # server will calculate md5(secret + payload)
    #                     = md5(secret + message + padding + malicious)
    #                     = fake_hash

    payload = message + padding + malicious
    s.send('2'+'\n')
    d = s.recv(1024)
    s.send(fake_hash+'\n')
    d = s.recv(1024)
    s.send(payload+'\n')
    time.sleep(1)
    d = s.recv(1024)
    print(d)
    if 'Hmm...' not in str(d):
        print(d)
        s.close()


s.close()
# send `fake_hash` and `payload` to server (manually or with sockets)
# REMEMBER: every time you sign new data, you will regenerate a new secret!
