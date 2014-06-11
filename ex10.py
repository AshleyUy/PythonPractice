#this is a tab! 
tabby_cat = "\tI'm tabbed in."
#one slash is like \n
persian_cat = "I'm split\non a line."
#double jus tmakes one print 
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
print "Extra points:\n"
print '%r' % (fat_cat)
print '%s' % (fat_cat)