"""
For example you have an object person, that has several attributes: name, gender, etc.
One can access these attributes(be it methods or data objects) usually writing:
    person.name, person.gender, person.the_method(), etc
But what if you don't know the attribute's name at the time you write the program?
For eg., you have attribute's name stored ina variable called attr_name
"""

class person():
    name = "Ramesh"

    def say(self, msg):
        print (self.name, msg)


if __name__ == '__main__':
    attr_name = 'name'
    p = person()
    print "Attribute name : " + getattr(p, attr_name)
    print getattr(p, 'say')('Hello')