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
    while totalBytes <= int(length):
        item = struct.unpack(f, data[offset:size])
        for i in item:
            stripped = str(hex(i)).strip("0x")
            if len(stripped) % 2 != 0:
                stripped += "0"
            s = binascii.unhexlify(stripped)
            totalBytes += int(len(s))
            if totalBytes > int(length):
                break
            ascii += s[::-1]

        if totalBytes > int(length):
            break
        offset = size
        size += 8

    print(ascii)

def print_array_of_words(length, offset, size):
    array = []
    totalBytes = 0
    while totalBytes <= int(length):
        item = struct.unpack(f, data[offset:size])

        for s in item:
            totalBytes += len(str(s))
            if len(array) >= int(length) / 4:
                break
            array.append(s)
        offset = size
        size += 8
    print(array)

def print_array_dwords(length, offset, size):
    array = []
    totalBytes = 0
    totalSize = len(data)
    while totalBytes <= int(length) and offset <= totalSize and size <= totalSize:
        item = struct.unpack(f, data[offset:size])
        i1 = item[0]
        i2 = item[1]
        array.append(i1 + i2)
        totalBytes += 8
        offset = size
        size += 8
    print(array)

def print_lat_long(length, offset, size):
    x = ""
    totalBytes = 0
    while totalBytes <= int(length):
        item = struct.unpack(f, data[offset:size])
        for i in item:
            totalBytes += 4
            if totalBytes > int(length):
                break
            x += str(float(i)) + " "
        offset = size
        size += 8

    print(x)

def print_section_ref(offset, size):
    counter = 1
    item = struct.unpack(f, data[offset:size])
    for s in item:
        if counter != 1:
            break
        counter += 1
        print(s)

def create_png(length, offset, size):
    fh = open("the picture.png", "wb")

    signature = b"\211PNG\r\n\032\n"

    totalBytes = 0
    while totalBytes <= int(length):
        item = struct.unpack(f, data[offset:size])
        for i in item:
            totalBytes += 4
            if totalBytes > int(length):
                break
            signature += binascii.b2a_base64(str(i))
        offset = size
        size += 8
    fh.write(signature)


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
size = 8
sizeOfFile = len(data)
start = True
header = ""
section_length = 0

while start:
    s = print_header(struct.unpack(f, data[offset:size]))
    offset = size
    size = size + 8
    header += s.strip("\n")

    if size >= 32:
        start = False
        print(header)
        numSections = header[len(header) - 2]


s = print_section_header(struct.unpack(f, data[offset:size]))
offset = size
size += 8
print("<===========Section 1==============>")
print(s)

print_ascii(s.split()[1], offset, size)
offset += int(s.split()[1])
size = offset + 8

s = print_section_header(struct.unpack(f, data[offset:size]))
offset = size
size += 8
print("<===========Section 2==============>")
print(s)

print_array_of_words(s.split()[1], offset, size)
offset += int(s.split()[1])
size = offset + 8

s = print_section_header(struct.unpack(f, data[offset:size]))
offset = size
size += 8
print("<===========Section 3==============>")
print(s)

print_lat_long(s.split()[1], offset, size)
offset += int(s.split()[1])
size = offset + 8

s = print_section_header(struct.unpack(f, data[offset:size]))
offset = size
size += 8
print("<===========Section 4==============>")
print(s)

print_section_ref(offset, size)
offset += int(s.split()[1])
size = offset + 8

s = print_section_header(struct.unpack(f, data[offset:size]))
offset = size
size += 8
print("<===========Section 5==============>")
print(s)

print_ascii(s.split()[1], offset, size)
offset += int(s.split()[1])
size = offset + 8

s = print_section_header(struct.unpack(f, data[offset:size]))
offset = size
size += 8
print("<===========Section 6==============>")
print(s)

print_ascii(s.split()[1], offset, size)
offset += int(s.split()[1])
size = offset + 8

s = print_section_header(struct.unpack(f, data[offset:size]))
offset = size
size += 8
print("<===========Section 7==============>")
print(s)

print_lat_long(s.split()[1], offset, size)
offset += int(s.split()[1])
size = offset + 8

s = print_section_header(struct.unpack(f, data[offset:size]))
offset = size
size += 8
print("<===========Section 8==============>")
print(s)

# Todo This is a PNG area
create_png(s.split()[1], offset, size)
offset += int(s.split()[1])
size = offset + 8

s = print_section_header(struct.unpack(f, data[offset:size]))
offset = size
size += 8
print("<===========Section 9==============>")
print(s)

print_ascii(s.split()[1], offset, size)
offset += int(s.split()[1])
size = offset + 8

s = print_section_header(struct.unpack(f, data[offset:size]))
offset = size
size += 8
print("<===========Section 10==============>")
print(s)

print_ascii(s.split()[1], offset, size)
offset += int(s.split()[1])
size = offset + 8

s = print_section_header(struct.unpack(f, data[offset:size]))
offset = size
size += 8
print("<===========Section 11==============>")
print(s)

print_array_dwords(s.split()[1], offset, size)












