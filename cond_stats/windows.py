import re
import sys
import string
from string import Template
details = []
limit = 0
N = (int)(raw_input(" Enter the number of lines to read "))
s = Template('$who likes $what')
s.substitute(who='h4k3r',what='pyFu')

""" The redefined python program """


def loop():
    limit = 0
    fh = open("words.txt")
    abc = fh.readlines()
    for line in abc:
        if limit == N:
            break
        print line,
        limit += 1

    fh.close()
    bc = 0
    Foo = open(raw_input('Enter the name of a file '))
    if Foo is not None:
        for line in Foo:
            bc += 1
            print bc,

def pager():
    """ Yje new pager program """
    File = open(raw_input( "Enter any file name for reading ") )
    if File is not None:
        prompt = raw_input("Do you wanna read the contents now... y / n ")
        counter = 1
        delimiter = 1
        m = re.search(r'y|Yes|yes|y', prompt)
        if m:
            for line in File:
                if  (counter / delimiter) == 10:
                    delimiter += 1
                    prompted = raw_input("Do you wish to continue")
                    x = re.search(r'y|Yes|YES|yes', prompted)
                    if x:
                        print line,
                print line,
                counter += 1


def file_len(abc):
    with open(abc) as f:
        for i, l in enumerate(f):
            pass
    return i, l

def Format(text, dic):
    text = []
    for x, y in enumerate(dic):
        text.append(y)
    return text

def FileFormat():
    inputFile = open("/root/Desktop/trial.txt")
    outputFile = open("test.csv", 'w+')
    for line in inputFile:
        outputFile.writelines(Format(line, inputFile))
    inputFile.close()
    outputFile.close()
    d = dict(who="havj",what="hacking")
    print s.safe_substitute(d)
    pass

class Finance(object):
    """This section of the app manages a home based finance"""
    balance = 0
    amount = 0
    def __init__(self):
        self.balance = balance
        self.amount = amount

    def Deposit(self):
        N = (int)(raw_input(" Enter the amount you intend to deposit ") )
        self.amount = N
        return self.amount

    def Withdrawal(self):
        """looking into a view"""
        self.amount = (int)(raw_input (" Enter your withdrawal amount "))
        return self.amount

    def Credit(self):
        """Add to what is given"""
        self.Deposit()
        self.balance += self.amount
        print "balance credited"
        print " Total balance =",self.balance
        return self.balance

    def Debit(self):
        """withdraw effectively"""
        self.Withdrawal()
        self.balance -= self.amount
        print "balance debited"
        print "Total balance =", self.balance
        return self.balance

    def UserMenu(self):
        """Authentic manipulation of transactions"""
        prompt = """
        (CD) Certificate of Deposit
        (MM) Money Market
        (MS) Money Savings
         (C) Checking
        Enter Account Type: """
        done = 0
        while not done:
            choice = 0
            while not choice:
                try:
                    option = raw_input(prompt).strip().upper()
                    m = re.search(r'CD|MM|MS|C',option)
                    if m:
                        print " Your preferred account type is ",option
                        prompt2 = """
                        (=>) WithDrawal
                        (<=) Deposit
                        (-) Debit
                        (+) Credit
                        Enter Choice :"""
                    else:
                        print "Invalid Transaction"
                except(EOFError, KeyboardInterrupt):
                    option = 'C'
                if option == 'E':
                    choice = 1
                try:
                    option1 = raw_input(prompt2).strip().upper()
                except(KeyboardInterrupt, EOFError):
                    option1 = 'E'
                m1 = re.search(r'=>|<=|-|+',option1)
                if not m1:
                    print "Invalid option.. Try again"
                else:
                    choice = 1
                if option1 == '=>': self.Deposit()
                if option1 == '<=': self.Withdrawal()
                if option1 == '-': self.Debit()
                if option1 == '+': self.Credit()
                if option1 == 'E': done = 1



with open("words.txt") as f:
    length = len( [x.strip() for x in f] )
    print length
    pools = f.readlines()

    for line in f:
        if limit == N:
            break
        print line,
        limit += 1
    for z in pools:
        if N > length:
            if limit == length:
                print "File limit value "
                break
        print z,
        limit += 1
print string.join(details)

if __name__ == '__main__':
    fm = Finance()
    fm.UserMenu()
    pager()
    file_len('words.txt')
    FileFormat()
