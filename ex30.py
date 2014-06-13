people = 30
cars = 40
buses = 15


if cars > people:
    print "We should take the cars."
#ELIF IS ELSE IF :D
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."

if cars>people and buses>cars:
	print "The rich people have many cars and other commute"
else:	
	print "MACHINES RULE THE WORLD"
