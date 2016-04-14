# name = input("Enter the name : ")
name = raw_input("Enter the name : ")
age = raw_input("Enter the age : ")
print "Name entered is : {}".format(name)
print "{} age is : {}".format(name, age)

# Becareful with this thing
a = eval(raw_input("what is 2+2 = "))
print a == 4