import os


def m1(file_name):
    f = open(file_name, "r")
    with f:
        lines_value = [line.rstrip('\n') for line in f]
    for value in lines_value:
        # put ur code and delete the print value line
        print value
    f.close()
    return 0


def m2():
    test = m1(file_name="test_file_1.txt")


if __name__ == '__main__':
    m2()
