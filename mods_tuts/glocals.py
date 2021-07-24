class PhoneEntry:
    def __init__(self, nm, ph):
        self.name = nm
        self.phone = ph
        print "Created instance for ", self.name
        pass
    def __updatephone__(self, ph):
        self.phone = ph
        print "update phone number for ", self.name, " is ", self.phone
        pass

p = PhoneEntry('Joe','512-53334-223')

class EmailAddrBook(PhoneEntry):
    def __init__(self, nm, ph, em, id):
        PhoneEntry.__init__(self,nm, ph)
        self.email = em
        self.id = id
        print "subclassed and now  assigned email for ", self.email
        pass

p = EmailAddrBook("Joe", "030-0303-343", "joe@kings.com",'323242')
p.__updatephone__('8484-2233-2324')
def Foo():
    print "\calling Foo"
    aString = "bar"
    aInt = 33
    print "Foo's globals ", globals().keys()
    print "Foo's locals ", locals().keys()

print "__main__'s globals", globals().keys()
print "__main__'s locals ", locals().keys()
Foo()
