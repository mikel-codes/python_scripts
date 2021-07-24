class MoneyFmt(object):
    def __init__(self, val=0.0):
        assert isinstance(val, float), "use a floating point value"
        val = float(val)
        self.__val = val

    def dollarize(self, sign=''):
         self.__val = '%s${0:,.2f}'.format(self.__val) % (sign)
         return self.__val

    def __str__(self):
        return self.dollarize()
    __repr__ = __str__

    def update(self, val1):
        print 'updated amount successfully'
        self.__val = val1

    def __non_zero__(self, val):
        if not isinstance(val, int):
            print "can return bool for"
        x = cmp(self.__val, val)
        if x > 0:
            print "its positive"
        else:
            print "its negative"


from time import ctime, time
import crypt
class Db(object):
    def __init__(cls, name, bases,attr):
        super(Db, cls).__init__(name, bases, attr)

class usersDb(object):
    choice = """
             A) Add a New user
             B) Update an Existing User
             C) Delete a user
             D) Exit this Program
             """
    users = {}
    username = raw_input("Enter your username").strip()
    pword    = raw_input("Enter your password").strip()
    if len(pword) < 6:
        print "password must be at least 6 characters"
        pword = raw_input("Enter your password").strip()

    users[username] = pword

    def __init__(self, username="", pword=""):
        self.login = username
        self.password = pword
        self.__ctime = ctime()

    def __set__(self, obj, passw):
        if (db.has_key(username)):
            db.get(pword)
        print "updating user password"
        self.__ctime = ctime()
        self.password = passw
        print "password updated successfully at ", self.__ctime


    def __get__(self, obj, type=None):
        if db.has_key(username):
            db.get(login)

        pass

    def __del__(self):
        pass


if __name__ == '__main__':
    fm = MoneyFmt(39338.9)
    print fm
    fm.__non_zero__()
