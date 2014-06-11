#am I doing this right
from sys import argv

print "First Name:"
fname = raw_input()
print "Last Name:"
lname = raw_input()
print "Age:"
age = raw_input()
print "Address:"
ad = raw_input()
print "Gender:"
sex = raw_input()


script, first, second = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print fname + lname + age + ad + sex