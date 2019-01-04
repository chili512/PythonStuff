# _*_ coding: utf8 _*_
# a comment
print "Hello World!"
# another comment
print "Hello Again"
print "I like typing this."
print "This is fun."
print 'Yay! Printing.'
print "I'd much rather you 'not'."
print 'I "said" do not touch this.'

print "I will now count my chickens"
print "Hens:", 25+30/6
print "Roosters", 100.0-25.0*3%4
print "now i count the eggs"
print 3+2+1-5+4%2-1/4+6
print "is it true that 3+2<5-7?"
print 3+2<5-7
print "what is 3+2?",3+2
print "what is 5-7?",5-7
print "thats why its false"
print "how about some more"
print "is it greater?",5>-2
print "is it greater or equal?",5>=-2
print "is it les or equal",5<=2

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180.12 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "lets talk about %s" % my_name
print "hes %d inches tall" % my_height
print "hes %d pounds heavy" % my_weight
print "hes %f pounds heavy" % round(my_weight,1)
print "hes hot %s eyes and %s hair" % (my_eyes, my_hair)
print "if i add %d, %d and %d i get %d" % (my_age, my_weight, my_height, (my_age+my_height+my_weight))
