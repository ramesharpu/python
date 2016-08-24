def spam():
    eggs = 99
    bacon ()
    print (eggs) # this code print 99 and not 0 because it is not going to use the next functions local variable


def bacon():
    ham = 101
    eggs = 0

spam()