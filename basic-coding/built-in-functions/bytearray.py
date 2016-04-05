"""
bytearray is mutable as compared to byte or str
Return a new array of bytes. The bytearray class is a mutable sequence of integers in the range 0 <= x < 256.
It has most of the usual methods of mutable sequences, described in Mutable Sequence Types,
as well as most methods that the str type has, see String Methods.

The optional source parameter can be used to initialize the array in a few different ways:

If it is unicode, you must also give the encoding (and optionally, errors) parameters;
bytearray() then converts the unicode to bytes using unicode.encode().
# If it is an integer, the array will have that size and will be initialized with null bytes.
# If it is an object conforming to the buffer interface,
 a  read-only buffer of the object will be used to initialize the bytes array.
# If it is an iterable, it must be an iterable of integers in the range 0 <= x < 256,
which are used as the initial contents of the array.
Without an argument, an array of size 0 is created.
"""

def bytearrayexample():
    list = [100, 200, 0, 255, 150]
    print "Defined list : "
    for i in list:
        print i
    new_list = bytearray(list)

    # Modify the values
    new_list[0] = 50
    new_list[2] = 150
    print "New list : "
    for i in new_list:
        print i

if __name__ == '__main__':
    bytearrayexample()