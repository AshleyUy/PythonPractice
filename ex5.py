name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
heightcm=height * 2.54
weightkilo=weight/2.20462


print "Let's talk about %s." % name
#format of ex4
print "He's" , height ,"inches or %.2f centimeters tall." %heightcm
print "He's %d pounds or %.2f kilos heavy." % (weight, weightkilo)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)