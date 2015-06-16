#!/usr/bin/python

# To add two numbers
var1 = input("Enter the first number : ")
var2 = input("Enter the second number : ")

var1, var2 = var2, var1

print "Swapped numbers are {0} and {1}".format(var1, var2)
