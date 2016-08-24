name = 'GlobalName'


def local_name():
    name = "LocalName"
    print('Local name is = {}'.format(name))


def global_name():
    print('Global name is = {}'.format(name))


local_name()
global_name()