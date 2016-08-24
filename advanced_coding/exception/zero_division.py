def div(num, div_by):
    # type: (object, object) -> object
    try:
        return num / div_by
    except ZeroDivisionError:
        print('Invalid operation, divide by zero')


if __name__ == '__main__':
    print(div(24, 6))
    print(div(24, 0))  # returns output as "Invalid operation, divide by zero" and also the return value i.e, "None"
