def __safe_float__(objx):

    '''carries out the conversions to float safely'''
    try:
        retval = float(objx)
    except (TypeError, ValueError), e:
        retval = str(e)
    return retval


def main():
    """ This does all the major processing """
    log = open("cardIog.txt", "w")
    try:
        xx = open("cardInfo.txt", 'r')
    except IOError:
        log.write("no transactions this month")
        log.close()
        return

    txns = xx.readlines()
    xx.close()
    total = 0.00
    log.write(" Account summanry for Transactions \n")

    for eachTxn in txns:
        result = __safe_float__(eachTxn)
        if isinstance(result, float):
            total += result
            log.write( "info... processed\n")
        else:
            log.write("ignored %s \n" % result )
    print "Total amount processed is %.2f" % total

    log.close()


def assertion(expr, args):
    if __debug__ and not expr:
        raise AssertionError, args
    else:
        print "successful"


if __name__ == '__main__':
    main()
    assertion(1==10, "Hello world")
