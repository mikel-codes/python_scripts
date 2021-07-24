#! /usr/bin/env python
# This scripts checks input and compares to see whether an identtifier or a
# keyword
import string
alphas = string.letters + '_'
nums = string.digits
alphanums = alphas + nums

iden = raw_input("Enter an identifier to check ")
if len(iden) > 0:
    if iden[0] not in alphas:
        print "starting character must be an alphabet or underscore"
    else:
        if len(iden) > 1:
            # make sure the other variables are in line
            for eachar in iden[1:]:
                if eachar not in alphanums:
                    print "Invalid character entered ", eachar
                    print "Hint: Other characters must be alphanumeric"
                    break
                else:
                    # do complete comparison to full keyword
                    import keyword
                    if iden not in keyword.kwlist:
                        print "ok, found an identifier"
                    else:
                        print "Invalid entry, this is a keyword"
        else:
            print "No entries for identifier check"
