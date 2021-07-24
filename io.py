#! /usr/bin/env python
import time

text = raw_input("ENter string ")
i = 0
while(i < len(text)):
    print (text[i])
    i = i + 1
    pass

print "Printing characters in reverse "
text[::-1]
for char in text[::-1]:
    print char,time.sleep(0.3)

