#! /usr/bin/env python

import crypt
db = {}

def newUser():
    # Register a new user
    prompt = "Login Required: "
    name = raw_input(prompt).strip()
    while True:
        if db.has_key(name):
            print "This username is no longer available"
            name = raw_input(prompt).strip()
        else:
            break
        pass
    pwd = raw_input("Enter your password ").strip()
    # set the name as key as value password
    print " Successfully registered as username [%s] and password [%s] " % (name, pwd)
    db[name] = pwd

def oldUser():
    # Recognise an registered member
    name = raw_input(" What is your username ").strip()
    password = raw_input(" Enter your password").strip()
    db.get(name)
    while True:
        if db.get(name):
            if password == db.get(name):
                print "Welcome back User[==%s==]" % db[name]
                break
            else:
                print "Login Error .... Try again"
                password = raw_input("eNTER yoUr PasSwOrD : ")
        else:
            print "Login Error..."
            name = raw_input(" What is your username ")
            password = raw_input(" Enter your password")


def admin():
    crypt(word)

def userMenu():
    # overview of users in login dictionary mutable sequence
    prompt = """ Please Note (Highlighted)
    (N)ew User Login
    (E)xisting User Login
    User(M)enu
    (Q)uit
    Enter Choice; """
    while True:
        while True:
            try:
                # do this for any input
                choice = raw_input(prompt).strip()[0].lower()
            except(EOFError,KeyboardInterrupt):
                # Note any special key characters and set these to defaults below
                choice = 'q'
            if choice in 'neq':
                # check for input in this sequence
                print "Your chose [***%s***] " % choice.upper()
                break
            else:
                print "Invalid choice ... Try again"
                pass
            pass
        try:
            if choice == 'n': newUser()
            if choice == 'e': oldUser()
            if choice == 'q': break
        except(EOFError,KeyboardInterrupt):
            choice = 'q'

if __name__ == "__main__":
    userMenu()





