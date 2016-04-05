#!/usr/bin/python

forms = ['animal', 'mineral', 'vegetable']
answer = input("Are you a animal, mineral or vegetable")

if answer == forms[0]:
	print("You are an animal. Grrr!!!")
elif answer == forms[1]:
	print("You are a mineral. You must be healthy")
elif answer == forms[2]:
	print("You are a vegetable.")
else:
	print("You did not give a valid response")
