from datetime import datetime as dt
from time import ctime

class DateTime(object):

    def __init__(self):
        self._date = dt.now()
        print "the complete time and date today is ", str(self._date)
        pass

    def display(self):
        choice = raw_input(""" Select a display Format for time
                A) 'MDY'  => MM/DD/YY
                B) 'MDYY' => MM/DD/YYYY
                C) 'DMY'  => DD/MM/YY
                D) 'DMYY' => DD/MM/YYYY
                E) 'MODYY'=> Mon DD, YYYY
            """)
        if choice.capitalize() == "A":
            self._date = dt.__format__(self._date, '%m/ %d/ %y')
        elif choice.capitalize() == "B":
            self._date = dt.__format__(self._date, '%m/ %d/ %Y ')
        elif choice.capitalize() == "C":
            self.date = dt.__format__(self._date, '%d / %m / %y')
        elif choice.capitalize() == "D":
            self._date = dt.__format__(self._date, '%d/ %m/ %Y ')
        elif choice.capitalize() == "E":
            self._date = dt.__format__(self._date, '%m %d, %Y ')

            pass

            pass
        return self._date


    def __str__(self):
        return str(self._date)

    __repr__ = __str__

    def update(self):
        print " Do you care to update time and date? "
        line = raw_input(" Yes/No \n ")
        if line.lower() == "yes" :
            choice = {"year" : 0 ,"day" : 0, "month" : 0, "hr" : 0, "min" : 0, "sec" : 0}

            for key in choice:
                print "Enter your values for ", key, " "
                choice[key] =   (int) (raw_input())
                pass
            now = dt(choice["year"], choice["day"] , choice["month"], choice["hr"], choice['min'], choice["sec"])
            self._date = str(now)
        elif line.lower() == "no":
            self._date = ctime()
        else:
            print "Please make a choice"
            self.update()
        return self._date


if __name__ == '__main__':
    dte = DateTime()
    print dte.display()
    print dte.update()

