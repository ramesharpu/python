import struct

class Shape(object):
    def __dir__(self):
        return ['area', 'perimeter', 'location']

if __name__ == '__main__':
    # show the names in the module namespace
    # ['__builtins__', '__doc__', '__name__', 'struct']
    print dir()

    # show the names in the struct module
    # ['Struct', '__builtins__', '__doc__', '__file__', '__name__', '__package__',
    # '_clearcache', 'calcsize', 'error', 'pack', 'pack_into', 'unpack', 'unpack_from']
    print dir(struct)

    s = Shape()
    # Shows the __dir__ details
    print dir(s)