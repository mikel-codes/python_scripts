from crypt import crypt
db ={}
class Registration():


    def __init__(self):
        self.db = {}
        self.salt = "93m./xa"
        pass
    
    
    def admin(self, pwd, salt):
        encrypted = crypt(pwd, salt)
        return encrypted


    def newUser(self):
        print "Registration required for login"
        while True:
            username = raw_input("Enter your username =< ")
            if (self.db).has_key(username):
                print "This username is not available"
                username = raw_input("Please try a different username ")
                pass
            else:
                break
            pass

        password = raw_input("Enter your password => ")
        valid = True
        while not valid:
            if len(password) < 6:
                print "passwords must be at least 6 characters long"
            else:
                valid = False
                pass
            pass

        self.db[username] = self.admin(password,self.salt)
        print "Welcome {0} you have been successfully registered{1}".format(username, password)
        pass
    
    
    def oldUser(self):
        print "************** Login Required *****************"
        user = raw_input("Enter your username")
        pwd = raw_input("Enter your password")
        if db.has_key(user):
            while 1:
                password =  db.get(user)
                if password == pwd:
                    print "welcome %s ...." % (user)
                    break
                else:
                    print " Login details is invalid "
                    print "try again"
                    continue
                    pass
                


    def ymenu(self):
        cisco = """

        ______User(M)enu______


        (N)ew User Login
        (E)xisting User Login
        (Q)uit
        Enter Choice::>  """


        while True:
            while True:
                prompt = raw_input(cisco).strip()[0].upper()
                if prompt not in "NEMMQ":
                    print "invalid selection"
                else:
                    break
                pass
            print "you selected {0}".format(prompt)
                 
            if prompt == "N":  self.newUser()
            if prompt == "E":  self.oldUser()
            if prompt == "Q":  break
            pass
        pass
    pass


if __name__ == '__main__':
    req = Registration()
    req.newUser()
    req.ymenu()

            
    

            
            





