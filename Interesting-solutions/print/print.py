from __future__ import print_function

def print_with_newline():
    print ("first")
    print ("second")

def print_multiple_values_in_sameline():
    print('first', 'second', 'third')

def print_using_end_in_sameline():
    print('first', end=' ')
    print("second")


if __name__ == '__main__':
    print_with_newline()
    print_multiple_values_in_sameline()
    print_using_end_in_sameline()
