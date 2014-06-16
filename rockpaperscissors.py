from random import randint

class Actions (object):

	choice = {1 : "ROCK", 2 : "SCISSORS", 3 : "PAPER"}

	def accept (self):
		print "Welcome, Duelsit! What art thou weapon of choice?"
		'''
		x = 0
		for x in range(0,len(Actions.choice)):
			print Actions.choice[x],
		'''
		print "\n[1]ROCK\t[2]SCISSORS\t[3]PAPER"
		print "\nChoose wisely, for thus determines thy fate of all Middle Kingdom!"
		ans=int(raw_input(">"))
		if ans > 4 or ans < 0:
			print "\nILLITERATE PIG!\n"
			Actions().accept();
		else:
			print "You have drawn the %s!" %Actions.choice[ans]
			#print Actions.choice[ans.upper()]
			return ans

	def generate (self):
		print "\nThy oponent hasth chosen!"
		random = randint(1,len(self.choice))
		gen=Actions.choice[random]
		print "%s hasth been drawn!" %gen
		return random

	def compare (self, user, bot):
		print "\n"
		if user == bot:
			print "IT IS A DRAW"
		elif user == 1 and bot ==2:
			print "YOU HAVE PREVAILED!"
		elif user == 2 and bot ==3:
			print "YOU HAVE PREVAILED!"	
		elif user == 1 and bot ==3:
			print "THOU BACKSIDE HAS BEEN ACQUIRED BY THINE OPPONENT!"
		elif user == 3 and bot ==1:
			print "YOU HAVE PREVAILED!"
		elif user == 2 and bot ==1:
			print "THOU BACKSIDE HAS BEEN ACQUIRED BY THINE OPPONENT!"	
		elif user == 3 and bot ==2:
			print "THOU BACKSIDE HAS BEEN ACQUIRED BY THINE OPPONENT!"
		else:
			print "THOU BACKSIDE HAS BEEN ACQUIRED BY THINE OPPONENT!"

	def play(self):
		
		action=Actions()
		my = action.accept()
		bot = action.generate()
		result = action.compare(my, bot)

	def again(self):

		print "\nDost thou desire to duel again?"
		print "[1]YES\t[2]NO"
		again = int(raw_input(">"))
		if again < 3 or again > 0:
			if again == 1:
				Actions().play()
			else:
				quit()
		else:
			print "ILLITERATE PIG!"
			Actions().again() 

Actions().play()
Actions().again()



