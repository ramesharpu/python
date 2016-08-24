def spam():
    egg = 124
    print egg

spam()
#t he below line will not print eggs value as its local variable
# print egg
''' the above code will throw NameError
Traceback (most recent call last):
  File "local_variable.py", line 7, in <module>
    print egg
NameError: name 'egg' is not defined
'''