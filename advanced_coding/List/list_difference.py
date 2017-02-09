list1 = ['a', 'b', 'c', 'd']
list2 = ['a', 'e', 'c', 'f']

list(set(list1)-set(list2))
# output ==> ['b', 'd']

list(set(list2)-set(list1))
# output ==> ['e', 'f']
