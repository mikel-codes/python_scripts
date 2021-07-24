#!usr/bin/env python
'''This is a simple python script that looks into converting bytes to text and vice versa using unicode as codec'''
CODEC = 'UTF-8'
FILE = 'example.txt'

codec_out = u'Hello World\n'
bytes_out = codec_out.encode(CODEC)

f = open(FILE, "w")
f.write(bytes_out)
f.close()

f = open(FILE,"r")
bytes_in = f.read()
f.close()

codec_in = bytes_in.decode(CODEC)
print codec_in

