# This example creates sqaures upto the given input using a list comprehension and generator
# i.e., [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

''' Using List Comprehension '''
def square_list(number):
    myList = [x*x for x in range(1, number)]
    print myList

''' Using Generators '''
def square_generator(number):
    mygenerator = (x*x for x in range(1, number))
    print list(mygenerator)

def test():
    abc

if __name__ == '__main__':
    # Print square of numbers till 10
    square_list(11)
    square_generator(11)


map(str, mylist)