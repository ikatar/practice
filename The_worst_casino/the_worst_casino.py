import random
import time



class Game:

	def __init__(self,money):
		self.money = money
		self.bet_amount = None
		self.money_borrowed = False
		self.legs_broken = False
		self.cheat = False

	def timing(self,amount):
		time.sleep(amount)

	def use_cheat(self):
		if self.cheat == False:
			print("Cheats are on!")
			self.cheat = True
		else:
			print("Cheats are off!")
			self.cheat = False
		#self.timing(2)

	def borrow_money(self):
		if self.money <= 10  and self.money_borrowed == False:
			print("\nOk, here's another 100 bucks. \
				\nIf you loose the next game I'll break your legs.")
			self.money+= 100
			self.money_borrowed=True
		elif self.money_borrowed == True:
			print("Wait what? I borrowed you money already. Go away until you have your legs!")
		else:
			print ("What do you want? Don't you have enough money anyway?")
		self.timing(2)

	def break_legs(self,lost):
		if lost == True and self.money_borrowed == True:
			print("Since you lost the game the dude broke your legs and you have no money left. GAME OVER")
			self.legs_broken = True
			return True
		else:
			return False

	def counter(self,to_print):
		counter = 3
		while counter !=0:
			print(f"{to_print} {counter}\n")
			time.sleep(1)
			counter-=1

	def roll_a_dice(self):
		value = random.randint(1,6)
		return value

	def prize(self):
		if int(self.bet_amount) == self.money:
			prize = int(self.bet_amount) * 4
		else:
			prize = int(self.bet_amount) * 2
		return prize

	def input_checker(self,user_range,text=None):
		if text == None:
			user_input = input("\nType in your answer:\n")
		else:
			user_input = input(f"{text}\n")

		while True:
			try:
				int(user_input)==int(user_input)
				if int(user_input) > int(user_range) or int(user_input) < 0:
					print(f"Values is out of range")
					user_input = input("Type in your answer:\n")				
				elif int(user_input) <= int(user_input) and int(user_input)>=0:
					break
			except ValueError:
				user_input = input("\nHas to be number only!\nPlease type in your new answer:\n")

		return user_input

	def bet(self):
		print(f"\nNow let's make a bet! How much you want to spend this time?\nYou have ${self.money}\n")
		self.bet_amount = self.input_checker(self.money)

		if int(self.bet_amount) == self.money:
			
			print("\nWow everybody! That's all-in right there!\n")
		elif int(self.bet_amount) == 0:
			print("Bet is zero! Skipping")
		else:
			pass

	def substract_money(self):
		if int(self.bet_amount)>int(self.money):
			print(f"You are broke my friend, you balance is {self.money}")
			return False
		
		else:
			self.money -= int(self.bet_amount)
			return True
		
	def roulette(self):
		starting_money = self.money
		ai_pick= random.randint(0,36)
		table = dict()
		table1 ={x:"Red" for x in range(1,36,2)}
		table2 ={x:"Black" for x in range(2,37,2)}
		for i,x in zip(table1.items(),table2.items()):
			table[i[0]]=i[1]
			table[x[0]]=x[1]

		print("\n\nLet's play roulette!\nYou pick a single number if you want x10 cash prize,\
			\nRed or Black goes for just a double reward,\
			\nYou can put as many bets as you would like.\n\
			\nTable has values from 0 to 36 as follows:\n")

		print(0,"Zero")
		for value in range(1,len(table)):
			if value%2 != 0:
				print(value,table[value],value+1, table[value+1])
			else:
				pass
		table[0]="Zero"

		bets={}
		if self.cheat == True:
			print("\nTO THE VICTORY!",ai_pick,table[ai_pick])
		else:
			pass
		while True:
			if len(bets)!=0:
				print("\nPlaced bets:")
				for i in bets.items():
					print(i[0],i[1])
			if self.money != 0:
				print("\nWhat do you want to do?\
					 \n1) Make a bet on a number\
					 \n2) Make a bet on a color\
					 \n3) Play")
				user_choice = self.input_checker(3)
				if int(user_choice) == 1:
					user_number = self.input_checker(36,"Pick a number to put a bet on:")
					self.bet()
					if self.substract_money() == True:
						print(f"You placed ${self.bet_amount} on number {user_number}")
						try:
							bets[int(user_number)]+=int(self.bet_amount)
						except KeyError:
							bets[int(user_number)]=int(self.bet_amount)
					else:
						pass
				elif int(user_choice) == 2:
					user_color = input("\nType in R for Red or B for Black\n")
					if user_color.lower() not in "rb":
						print("\nYou HAVE to type in 'R' or 'B', nothing else")
						continue
					elif user_color.lower() == "r":
						user_color = "Red"
					elif user_color.lower() == "b":
						user_color = "Black"

					self.bet()

					if self.substract_money() == True:
						print(f"You placed ${self.bet_amount} on {user_color}")
						try:
							bets[user_color]+=int(self.bet_amount)
						except KeyError:
							bets[user_color]=int(self.bet_amount)
					else:
						pass


				elif int(user_choice) == 0:
					print("\nCommon, how hard it is to type in a proper number?\n")
				else:
					break
			else:
				print("\nYou don't have any more money to bet. Let's play!\n")
				break


		self.counter("Let's spin the wheel!")
		print(f"And the winning number is {ai_pick} {table[ai_pick]}\n")
		self.timing(2)
		for user_bet in bets.items():
			if str(user_bet[0]) in "Red" or str(user_bet[0]) in "Black":
				if user_bet[0] == table[ai_pick]:
					self.money+= int(user_bet[1])*2
					print(f"\nColor {table[ai_pick]} is a lucky one today! You got double the reward for it!\
						\n${int(user_bet[1])*2} were sent to your account!\n")
			elif user_bet[0] == ai_pick:
				print(f"\nJesus Christ! We are going to loose all of our money!\
					\n${int(user_bet[1])*10} were sent to your account")
				self.money+= int(user_bet[1])*14
			else:
				print(f"{user_bet[0]} wasn't a lucky pick, you lost ${user_bet[1]}\n")
			time.sleep(1.9)

		print("\nLet's get back to lobby\n")
		time.sleep(1)
		
		if self.money < starting_money and self.money_borrowed == True:
			self.break_legs(True)
		else:
			self.money_borrowed = False
			pass

	def draw_a_card(self):
		starting_money = self.money
		cards = {
		"Ace":14,"King":13,"Queen":12,"Jack":11,
		"10": 10,"9": 9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2
		}
		to_pick = list(cards.keys())
		print("\nRules are simple, whoever pick the highest card wins!\
			\nDraw isn't possible!\
			\nWe have this cards:\n")
		for i in to_pick:
			print(i,end=" ")
		print("\n")

		self.bet()
		prize = int(self.prize())

		self.counter("Shuffling the deck")
		
		ai_pick=random.choice(to_pick)
		to_pick.remove(ai_pick)
		user_choice=random.choice(to_pick)

		if self.cheat == True:
			print("\nCheats are on ;)\n")

			while cards[user_choice]<cards[ai_pick]:
				if ai_pick == "Ace":
					ai_pick = random.choice(to_pick)
				ai_pick=random.choice(to_pick)
				user_choice=random.choice(to_pick)
		else:
			pass


		if int(self.bet_amount)!=0:	
			print(f"Opponent drew the {ai_pick} with value of {cards[ai_pick]}.\
				\nYou drew the {user_choice} with value of {cards[user_choice]}\n")
			if cards[ai_pick] < cards[user_choice]:	
				print(f"Wow! You won ${prize}... I'll send you the money right away\n")
				self.money += prize
				self.bet_amount = 0
				print(f"You current balance is ${self.money}")
			else:
				print(f"Well buddy, next time fortune will smile on you ;)")
				self.money-= int(self.bet_amount)
				self.bet_amount = 0
				print(f"You have left ${self.money}")
		self.timing(3)

		if self.money < starting_money and self.money_borrowed == True:
			self.break_legs(True)
		else:
			self.money_borrowed = False

	def cho_han(self):
		starting_money = self.money
		dice_01 = self.roll_a_dice()
		dice_02 = self.roll_a_dice()
		choices=["Odd","Even"]
		
		sum_of_two = dice_01+dice_02
		if self.cheat == True:
			print(f"\nCHEAT!\nThe sum is {sum_of_two}!")
		print(f"\nLet's roll two dices! Guess if the sum gonna be odd or even!\nYour choices are:\n\n1){choices[0]}\n2){choices[1]}")
		user_choice = self.input_checker(len(choices))
		if int(user_choice) == 0:
			print("\nHere's an easter egg for ya. You picked zero as an answer but it's out range. I won't punish you though :D\n")
			user_choice = int(user_choice)+1
			print("\nSo your choice is: ",choices[int(user_choice)-1])
		else:
			print("\nYou chose: ",choices[int(user_choice)-1])

		user_choice = choices[int(user_choice)-1]
		

		self.bet()
		prize = int(self.prize())
		self.counter("Dices are rolling")

		if sum_of_two%2 == 0:
			ai_pick = choices[1]
		else:
			ai_pick = choices[0]

		print(f"First dice has value of {dice_01} and second one is {dice_02}.")
		if int(self.bet_amount)!=0:	
			if ai_pick == user_choice:	
				print(f"Wow! You won ${prize}... I'll send you the money right away\n")
				self.money += prize
				self.bet_amount = 0
				print(f"You current balance is ${self.money}")
			else:
				print(f"Well buddy, next time fortune will smile on you ;)")
				self.money-= int(self.bet_amount)
				self.bet_amount = 0
				print(f"You have left ${self.money}")

		self.timing(3)

		if self.money < starting_money and self.money_borrowed == True:
			self.break_legs(True)
		else:
			self.money_borrowed = False

	def flip_coin(self):
		starting_money = self.money
		choices=["Heads","Tails"]
		ai_pick = random.choice(choices)
		if self.cheat == True:
			print(f"\nCHEAT!\nAnswer is {ai_pick}")
		else:
			pass
		print(f"\nLet's flip a coin! Your choices are:\n1){choices[0]}\n2){choices[1]}")
		user_choice = self.input_checker(len(choices))
		if int(user_choice) == 0:
			print("\nHere's an easter egg for ya. You picked zero as an answer but it's out range. I won't punish you though :D\n")
			user_choice = int(user_choice)+1
			print("So your choice is: ",choices[int(user_choice)-1])
		else:
			print("\nYou chose: ",choices[int(user_choice)-1])
		
		self.bet()
		
		prize = int(self.prize())
		if int(self.bet_amount)!=0:	
			self.counter("coin is flipping")
			if ai_pick == choices[int(user_choice)-1]:	
				print(f"Wow! You won ${prize}... I'll send you the money right away\n")
				self.money += prize
				self.bet_amount = 0
				print(f"You current balance is ${self.money}")
			else:
				print(f"Well buddy, next time fortune will smile on you ;)\n")
				self.money-= int(self.bet_amount)
				self.bet_amount = 0
				print(f"You have left ${self.money}")
		self.timing(3)
		if self.money < starting_money and self.money_borrowed == True:
			self.break_legs(True)
		else:
			self.money_borrowed = False

#Call your game of chance functions here
money = 100
game = Game(money)
turn = 1
print("""

████████╗██╗░░██╗███████╗  ░██╗░░░░░░░██╗░█████╗░██████╗░░██████╗████████╗
╚══██╔══╝██║░░██║██╔════╝  ░██║░░██╗░░██║██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
░░░██║░░░███████║█████╗░░  ░╚██╗████╗██╔╝██║░░██║██████╔╝╚█████╗░░░░██║░░░
░░░██║░░░██╔══██║██╔══╝░░  ░░████╔═████║░██║░░██║██╔══██╗░╚═══██╗░░░██║░░░
░░░██║░░░██║░░██║███████╗  ░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝░░░██║░░░
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░

░█████╗░░█████╗░░██████╗██╗███╗░░██╗░█████╗░
██╔══██╗██╔══██╗██╔════╝██║████╗░██║██╔══██╗
██║░░╚═╝███████║╚█████╗░██║██╔██╗██║██║░░██║
██║░░██╗██╔══██║░╚═══██╗██║██║╚████║██║░░██║
╚█████╔╝██║░░██║██████╔╝██║██║░╚███║╚█████╔╝
░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚══╝░╚════╝░
""")
print("Welcome to the worst casino ever.\
\nWe don't care if you win or loose just don't borrow money from that shady dude.")
while True and not game.legs_broken:
	print("\n\
		\nPick the game to play!\n\
		\n1) Play 'Flip a coin'\
		\n2) Play 'Cho Han' dice rolling game\
		\n3) Play 'Draw the highest card'\
		\n4) Play 'Roulette'\
		\n5) Borrow money from a shady dude in the corner\
		\n6) Use cheats :) ")
	if game.cheat == False:
		print(f"\nYou have ${game.money}")
	elif game.cheat == True:
		print(f"Cheats === ON")
		print(f"\nYou have ${game.money}")
	answer = int(game.input_checker(6))
	if answer == 1:
		game.flip_coin()
	elif answer == 2:
		game.cho_han()
	elif answer == 3:
		game.draw_a_card()
	elif answer == 4:
		game.roulette()
	elif answer == 5:
		game.borrow_money()
	elif answer == 6:
		game.use_cheat()
	else:
		print("\nWrong input!\n")
while True:
	if self.money()>10000:
		print("You won the game!")
	else:
		print("Se ya next time... when you can walk again")

	if input():
		break