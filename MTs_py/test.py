import threading
class K:
    def __init__(self, func):
        self.func = func
    def __call__(self):
        apply(self.func)
    pass

def lord():
    print "This is it"

if __name__ == '__main__':
    c = K(lord)
    print threading.Thread(target=c).start()


