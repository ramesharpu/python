import operator

def abc(operation, values=[]):
    if operation=='add':
	print sum(values)
	print reduce(operator.__add__,values)
    elif operation=='sub':
	print (values[0]-sum(values[1:]))
	print reduce(operator.__sub__,values)
    elif operation=='mul':
	print reduce(operator.__mul__,values)
    else:
	print (reduce(operator.__div__,values))

abc(operation='div', values=[10, 50])
