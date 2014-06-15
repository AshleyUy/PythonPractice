from random import randint

class Actions (object):

	choice = ["ROCK", "PAPER", "SCISSORS"]

	def accept (self):
		print "Welcome, Duelsit! What aret thou weapon of choice?"
		print choice
		print "Choose wisely, for thus determines thy fate of all Middle Kingdom!"
		ans=raw_input(">")
		ans.upper()

	def generate (self):
		print "Thy oponent hasth chosen!"
		gen=Actions.choice[randint(o,len(self.choice)-1)]
		print "%s hasth been drawn!" %gen

	def compare (self):
		user = Actions.accept.ans
		bot = Actions.generate.gen

Actions.accept()
Actions.generate()
Actions.compare()

print Actions.compare.user
print Actions.compare.bot