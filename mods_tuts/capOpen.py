import types
class capFileOpener():
    def __init__(self, f_type, mode='r', buff=-1):
        self.mode = mode
        self.f_type = open(f_type, mode, buff)

    def capWriter(self, lines):
        self.f_type.writelines(lines.upper())

    def __str__(self):
        return str(self.f_type)

    __repr__ = __str__

    def __getattr__(self, attr):
        return getattr(self, attr)

if __name__ == '__main__':
    cpF = capFileOpener("/root/Desktop/house/eg.txt", 'w')
    cpF.capWriter("life is good")
    cpF.capWriter("how much is that")
    a = "looky"
    if type(a) == type(0):
        print "There is a match"
    if type("hello") == type("Hello World"):
        print "Strings"
    if type('yello') == types.IntType:
        print "ll"
    else:
        print "cools"
    if type(a) is type("jo"):
        print "Another match"

    if isinstance("8000", str):
        print "Ok"

