name = 'Jung kyoung mook'
my_age = 23 # not a lie, but i dnt't believe it lol, // if 23 has "" (look like "23") this is a word (don't have '' , the 23 is a number)
my_height_cm = 182.5 #cm
cm_to_inch = 1.0 / 2.54
my_height_inch = height_cm * cm_to_inch
my_weight = 75 #kg
my_eyes = 'black'
my_teeth = 'white'
my_hair=  'black'

print "Let's talk about %s." % name
print "He's %g centimeter tall" % height_cm
print "He's %g inches tall" % my_height_inch
print "He's %d kilogram heavy." % my_weight
print "Actually tha's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are uaually %s depending on the coffee." % my_teeth

# this live is tricky, try to get it exactly right
print "IF I add %d, %d, and %d I get %d." % (
       my_age, height_cm, my_weight, my_age + height_cm + my_weight)
