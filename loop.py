#! /usr/bin/env python

import thxhxhime

def showMaxF(num):
    # Total count
    count = num / 2
    while count > 1:
        if num % count == 0:
            print "The largest possible factor of ", num , "is", count,time.sleep(0.05)
            break
        count -= 1
        pass
    else:
        print num , " is prime"
        pass
    pass

if __name__ == '__main__':
    for eachNum in range(10,20):
        showMaxF(eachNum)
    p = ['Koler', 'Resurgence', 'Total', 'AgbamiChevron']
    valid  = False
    count = 3
    while count > 0:
        input = raw_input("Your password: ")
        for eachpass  in p:
            if input == eachpass:
                valid = True
                print "Welcome password ", input
                break
            pass
        if not valid:
            print "Invalid input"
            print "Maximum Tries left ...", count
            count -= 1
            pass
        else:
            break
        pass
    Trilogy = ['Games','Niggas','Play']
    i = iter(Trilogy)
    while True:
        try:
            fetch = i.next()
            print fetch
        except(StopIteration):
            print "Limit of sequence is reached"
            break


