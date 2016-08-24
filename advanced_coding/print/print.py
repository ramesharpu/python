from __future__ import print_function


def print_with_newline():
    print ("first")
    print ("second")


def print_multiple_values_in_same_line():
    print('first', 'second', 'third')


def print_using_end_in_same_line():
    print('first', end=' ')
    print("second")


def print_using_seperator():
    print('one', 'two', 'three', sep=', ')


if __name__ == '__main__':
    print_with_newline()
    print_multiple_values_in_same_line()
    print_using_end_in_same_line()
    print_using_seperator()
