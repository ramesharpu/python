# Using sort keyword
a = [5, 1, 4, 3]
print sorted(a)    ## [1, 3, 4, 5]


strs = ['aa', 'BB', 'zz', 'CC']
print sorted(strs)  ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
print sorted(strs, reverse=True) ## ['zz', 'aa', 'CC', 'BB']
print sorted(strs, key=str.lower)


list1 = [1, 3, 2]
print (list1.sort()) # Returns None, this is incorrect way tow using it
list1.sort()
print (list1) ## [1, 2, 3]

