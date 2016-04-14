"""
Return an enumerate object. sequence must be a sequence, an iterator, or some other object whcih supports
iteration. The next() method of the iterator returned by enumerate() returns a tuple containing a count
(from start which defaults to 0) and the values obtained from iterating over sequence
"""

if __name__ == '__main__':
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    print (list(enumerate(seasons)))
    # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    print list(enumerate(seasons, start=1))
    # [(3, 'Spring'), (4, 'Summer'), (5, 'Fall'), (6, 'Winter')]

"""
The above method is equivalent to the below code

def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
"""
