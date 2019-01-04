x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s" % (binary, do_not)
print x
print y
print "i said %r" % x
print "i also said '%s'" % y

hilarious = False
joke_evaluation = "isnt that joke so funny? %r" 

print joke_evaluation % hilarious

w = "Left "
e = "right "
print w+e

print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10  # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
# The comma allows the line to wrap
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

formatter = "%r %r %r %r"
print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)


#Heres some strange stuff type it exactly
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSept\nOct\nNov\nDec"
print "here are the days ", days
print "here are the months", months
print "here are the months %r" % months
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#while True:
 #   for i in ["/","-","|","\\","|"]:
  #      print "%s\r" % i,
