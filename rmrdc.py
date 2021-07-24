#!/usr/bin/env  python
def getPassword():
    try:
        with open("rmrdcPass.txt", 'w') as x:
            for i in range(1, 200):
                line = "rmrdc%s\n" % str(i)
                x.write(line)
                pass
            x.close()
            pass
        pass
    except IOError as io:
        print io.message

if __name__ == "__main__":
    getPassword()
