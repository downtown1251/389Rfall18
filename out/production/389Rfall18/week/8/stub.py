#!/usr/bin/env python2

import sys
import struct
import binascii
import datetime


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


def print_header(item):
    itemPrint = ''
    count = 1
    for i in item:
        if offset == 8 and count == 1:
            itemPrint += str(datetime.datetime.fromtimestamp(i)) + " "
        elif (offset == 8 and count == 2) or (offset == 16 and count == 1):
            stripped = str(hex(i)).strip("0x")
            s = binascii.unhexlify(stripped)
            itemPrint += s[::-1] + " "
        elif (offset == 16 and count == 2):
            itemPrint += str(int(i)) + " "
        count += 1
    return itemPrint


def print_section_header(item):
    itemPrint = ""
    for i in item:
        itemPrint += str(int(i)) + " "
    return itemPrint


def print_ascii(length, offset, size):
    ascii = ""
    totalBytes = 0
    while totalBytes <= len(str(length)):

        item = struct.unpack(f, data[offset:size])
        for i in item:
            stripped = str(hex(i)).strip("0x")
            if len(stripped) % 2 != 0:
                stripped += "0"
            s = binascii.unhexlify(stripped)
            ascii += s[::-1]
            totalBytes += len(s)

        offset = size
        size += struct.calcsize(f)
        totalBytes = len(ascii)
        print(totalBytes)


    print(ascii)
    return size





# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
f = "<LL"
offset = 0
size = int(struct.calcsize(f))
sizeOfFile = len(data)
start = True
header = ""
numSections = 0

while start:
    s = print_header(struct.unpack(f, data[offset:size]))
    offset = size
    size = size + struct.calcsize(f)
    header += s.strip("\n")

    if size >= 32:
        start = False
        print(header)
        numSections = header[len(header) - 2]

start = True
while start:
    s = print_section_header(struct.unpack(f, data[offset:size]))
    offset = size
    size += struct.calcsize(f)

    if size >= 40:
        start = False
        section_length = s.split()[1]
        print(s)

s = print_ascii(section_length, offset, size)
offset = s
size = s + 8


s = print_section_header(struct.unpack(f, data[offset:size]))
offset = size
size += struct.calcsize(f)
print(s)






