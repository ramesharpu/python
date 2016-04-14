# Example 1
i = iter([1, 2, 3])
print i.next()
print i.next()
print i.next()

#Example 2
with open('test_file_for_compile_example.py') as fp:
    for line in iter(fp.readline, ''):
        print line[0]