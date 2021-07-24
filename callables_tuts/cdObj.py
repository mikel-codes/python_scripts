dashes = '\n' + '^' * 25

exec_dict = { 'f' : """
             for %s in %s:
              print %s
             """,
             'n' : """
             %s = 0
             %s = %s
             while %s < len(%s):
              print %s[%s]
              %s += 1
             """,
             'd' : """
             %s = %d
             while %s < %d:
              print %s
              %s = %s + %d
             """}

def main():
    ltype = raw_input("Enter your loop type For/While")
    rtype = raw_input("Enter data type Number/Sequence")

    if rtype == 'd':
        start = input("Enter a starting value")
        stop =  input("Enter an ending value")
        step =  input("Enter a step amount")
        seq =   str(range(start, stop, step))
    else:
        seq = raw_input("Enter any sequence")
        
    var = raw_input("Enter an iterative variable name")

    if ltype == 'f':
        exec_str = exec_dict['f'] % (var, seq, var)  # call the associated value to this key and assign
    elif ltype == 'w':
        if dtype == 's':


