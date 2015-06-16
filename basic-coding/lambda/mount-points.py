import commands

mount = commands.getoutput('mount -v')
lines = mount.splitlines()
points = map(lambda line: line.split()[2], lines)

print "\n", points

print "\n"
print "Printing in single line"
print map(lambda x: x.split()[2], commands.getoutput('mount -v').splitlines())
