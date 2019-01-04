from sys import argv

script, filename = argv

txt = open(filename)

print "file %r" % filename

print "\n\n\n\n\n"
print txt.read()
print "\n\n\n\n\n"


file_again = raw_input("> ")
txt_again = open(file_again)
print txt_again
