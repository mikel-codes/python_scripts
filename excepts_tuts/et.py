def gloworldApp():
    "Just a measure of exception interaction"
    try:
        coo = open("aptitude",'r')
        for line in coo:
            print line,
    except (KeyboardInterrupt, SystemExit), e:
        print e
    except IOError, e:
        print e





class Foo:
    aList = []
    dict = {'seter':"client", "dorge":"toyata"}

    def Teaser():
        try:
            aList = []
            aList[7]
            dict['server']
            with open('aptitd','r') as f:
                for line in f:
                    print line,
        except (KeyError, Exception) ,e:
            print "Errors found", e
            pass


    def safe_float(obj):
        try:
            retVal = float(obj)
        except ValueError:
            retVal = "could nor convert string to float"
            pass
        return retVal

foo = Foo()
foo.safe_float('mx')
