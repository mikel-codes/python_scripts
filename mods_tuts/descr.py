import os
import sys
import pickle

class FileDescr(object):
    """This is a descriptor b/c (its contains a ^^get/set/delete^^)"""
    saved = []

    def __init__(self, name=None):
        self.name = name

    def __get__(self, obj, typ=None):
        if self.name not in FileDescr.saved:
            raise AttributeError , " %r used before assignment" % (self.name)
        try:
            __filehandler = open(self.name, 'r')
            __val = pickle.load(__filehandler)
            __filehandler.close()
            return __val
        except (IOError, pickle.UnpicklingError, IndexError, AttributeError, EOFError, ImportError), e:
            raise AttributeError, "could not read %r : %s " % (self.name), e
        pass

    def __set__(self, obj, val):
        __filehandler = open(self.name, 'w')
        try:  # U can never merge try-except & try-finally
            try:
                pickle.dump(val, __filehandler)
                FileDescr.saved.append(__filehandler)
            except (IOError, AttributeError, ImportError,TypeError, pickle.PicklingError), e:
                raise TypeError, "File style format not understood", e
        finally:
            __filehandler.close()
        pass

    def __delete__(self, obj):
        try:
            os.unlink(self.name)  # removes file from file system
            FileDescr.saved.remove(self.name)  # removes the object from the list
        except (IOError, OSError), e:
            print "Errors :" , e

class useFileDescr(object):
    d = FileDescr('loops')
    p = FileDescr('bbc')
    pass

if __name__ == '__main__':
    xp = useFileDescr()
    xp.bbc = "loops"
    print xp.bbc
