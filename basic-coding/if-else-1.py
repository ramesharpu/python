#!/usr/bin/python

# Decisioning making, branching, conditional logic
"""
if <test condition>:
	<statement block>
elif <test condition>:
	<statement block>
else: #optional
	<statement block>

operators ==, !=, <. >, <=, >=, and, or, not
"""
num = input("Enter an integer: ")
num = int(num)

if num<0:
	print("The absolute value of ", num, "is", -num)
else:
	print("The absolute value of ", num, "is", num)
