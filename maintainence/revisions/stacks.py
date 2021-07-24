
class Stackers(object):
    def __init__(self):
        self.stack = []
        pass
    def push(self):
        x = raw_input("  add your data to stack menu --) ")
        self.stack.append(x)
        pass

    def pop(self):
        if len(self.stack) > 0:
            print "removing %s from stack " % (str(stack.pop()))
        print "stack is empty".capitalize()
        pass

    def viewstack(self):
        print str(self.stack)
        pass

    def showmenu(self):
        options = """
        \t\tStack Menu
        (v)iew  > v
        p(u)sh  > u
        p(o)p   > o
        e(x)it  > x

        Enter Choice:-  """

        done = 0
        while not done:
            choice = 0
            while not choice:
                try:
                    x = raw_input(options).strip()[0]
                except Exception as e:
                    x = 'x'
                    break

                if x not in "vuox":
                    print "invalid selection"
                else:
                    print "you selected ", x
                    choice = 1
                    break
                pass
            if x == "v": self.viewstack()
            if x == "u": self.push()
            if x == "o": self.pop()
            if x == "x": done = 1

            pass

if __name__ == "__main__":
    st = Stackers()
    st.showmenu()
    
    try:
        xp = int(raw_input("Enter the number of lines to read from this file  "))
    except (ValueError, NameError) as ve:
        print ve.message
        pass
    
    with open("testy.py") as t:
        from time import sleep
        
        count = len(t.readlines())
        print "total lines in file is", count
        
        print "Preparing to read ", xp , " lines from file"
        sleep(0.3)
       
        print t.readline(100)
        for line, xln in enumerate(t, 0):
            print xln
            pass
        pass
    t.close()


                    



            
        
