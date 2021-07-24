#! /usr/bin/env python

'''create data structure'''
stack = []

def pushit():
    # lets update the data stack
    stack.append(raw_input("Enter a raw string:"))
    pass


# removes last-in element from stack
def popit():
    if(len(stack) == 0):
        print " Stack is empty "
        pass
    print 'Removed [', stack.pop(), ']'
    pass

def viewstack():
    # This print the contents of stack to the screen
    print str(stack)
    pass

def showmenu():
    # This overall menu is used to manipulate stack

    prompt = """
    p(U)sh
    p(O)p
    (V)iew

    (Q)uit
    Enter choice: """
    done = 0
    while not done:
        chosen = 0
        while not chosen:
            try:
                # take the first option for any entry
                choice = raw_input(prompt)[0]
            except(EOFError,KeyboardInterrupt):
                choice = 'q'
                pass
            print "Your chose [%s]" % choice
            if choice not in 'uovq':
                print "Invalid choice ... Try again"
            else:
                chosen = 1
                pass
            if choice == 'q': done = 1
            if choice == 'o': popit()
            if choice == 'u': pushit()
            if choice == 'v': viewstack()

if __name__ == '__main__':
    showmenu()



