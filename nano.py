
#!/usr/bin/env python
debug = True
class Foo:
    """ This class is for coding analysis """
    def cxe():
        """ comparing two files """
        with open("/root/Desktop/output.txt") as fp:
            with open("/root/Desktop/pass.txt") as gp:
                pli = fp.readline()
                lio = gp.readline()
                for num, line in enumerate(fp, 1):
                    for num, line in enumerate(gp, 1):
                        if pli != lio:
                            print "Files dissimilar on ", num, line
                gp.close()
            fp.close()

    if __name__ == "__main__":
        cxe()
