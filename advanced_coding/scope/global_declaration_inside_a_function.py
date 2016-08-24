''' If you want to change a global declaration inside a method, use the global keyword'''

eggs = "ramesh"
print(eggs)  # this will print 'ramesh'


def spam():
    global eggs
    eggs = 'test'


eggs = 'global'
print(eggs)  # this will print 'global'
spam()
print(eggs)  # this will print 'test'
eggs = 'global_test'
print(eggs)  # this will print 'global_test'