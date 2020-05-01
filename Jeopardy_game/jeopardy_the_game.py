import pandas as pd
import random
import time
import re
import j_symbols
import sys,os

df = pd.read_csv("jeopardy_f.csv")

df.rename(columns = {
	"Show Number":"show_number",
	" Air Date":"air_date",
	" Round":"round",
	" Category":"category",
	" Value":"value",
	" Question":"question",
	" Answer":"answer"
	},
	inplace=True)

df.value = df.value.apply(lambda value: int(value.strip("$").replace(",","")) if value != "None" else 0)
df = df[df["value"] != 0]
df.category = df.category.apply(lambda x: x.lower())
df.answer = df.answer.apply(lambda x: str(x).lower())
df.question = df.question.apply(lambda x: re.sub(re.compile('<.*?>'), '', x))

class Player:
	"""docstring for Player """
	def __init__(self,name,money=0,questions_answered=1,questions=None,skips=1,answers=None):
		self.name = name 
		self.money = money
		self.questions = questions
		self.skips = skips
		self.questions_answered = questions_answered
		self.answers = answers
	def __repr__(self):
		return self.name

	def recorded_question(self):
		iteration = 1
		for i,x in self.questions.items():
			print(f"{iteration}){i}\nCorrect answer was {x}. Your answer was {self.answers[iteration-1]}\n")
			iteration +=1
		
	def user_input(self):
		if self.answers == None:
			self.answers = list()


		x = input("Type in:\n")

		if str(x).lower() == "skip":
			self.skips = 0
			self.answers.append("Skipped")
			return "skip"
		else:
			self.answers.append(str(x))
			return x.lower()

	def add_money(self,value):
		self.money += value

		return self.money
		
	def generate_question(self):

		easy_questions = df[df.value < 400].reset_index()
		medium_questions = df[(df.value > 400) & (df.value < 1400)].reset_index()
		hard_questions = df[df.value > 2000].reset_index()

		if self.questions_answered <= 2:
			choice = random.randrange(0,int(easy_questions.question.count()))
			current_row = easy_questions.loc[choice]
		elif self.questions_answered > 2 and  self.questions_answered < 4:
			choice = random.randrange(0,int(medium_questions.question.count()))
			current_row = medium_questions.loc[choice]
		else:
			choice = random.randrange(0,int(hard_questions.question.count()))
			current_row = hard_questions.loc[choice]
		
		if self.questions == None:
			self.questions = dict()
			self.questions[current_row.question] = current_row.answer
		else:
			self.questions[current_row.question] = current_row.answer
		
		return current_row.question,current_row.answer,current_row.value
		
	def ask_question(self):
		if self.questions_answered <=5:
			print(f"You have {5-self.questions_answered+1} questions left!\nYour next question is:\n",j_symbols.c_print("line"))
			generated_question = Player.generate_question(self)
			
			question = generated_question[0]
			answer = generated_question[1]
			value = generated_question[2]
			
			print(f"{question}\nValues of this question is {value}$")
			print(j_symbols.c_print("line"))
			user_answer = Player.user_input(self)

			if str(user_answer) == "skip":
				print(f"\nSure, the answer is\n{answer}\n")
				Player.add_money(self,value)
				print(f"{value}$ were added to your account\n")
			elif user_answer == "":
				print("\nWell, you actually need to type in something. No money for ya!\n")
			elif str(user_answer).strip() in answer.strip():
				print(j_symbols.c_print("wow"))
				Player.add_money(self,value)
				print(f"{value}$ were added to your account\n")
			else:
				print("\nWell,try googling harder next time ;) No money for ya!\n")

			self.questions_answered +=1
		
player = Player("Player")

print(j_symbols.c_print("intro_text"))
print("\nYou have one skip,to use it simply type in skip")
while True:

	if player.questions_answered < 6:
		player.ask_question()		
	else:
		break
	time.sleep(2)

while True:

	print("Wanna see the correct answers vs yours?")
	x = input("\n")
	if str(x).lower() in "yes":
		player.recorded_question()
	
	if player.money < 2000:
		print(f"You won just {player.money}$ ¯\\_( ͡° ͜ʖ ͡°)_/¯\n",j_symbols.c_print("final_text"))
	else:
		print(f"WOW you won {player.money}$!!! Such a knowledge... That's a real impressive... use of google! ( ͡❛ ͜ʖ ͡❛) \n",j_symbols.c_print("final_text"))

	exiter = input("Hit enter to exit")
	if len(exiter)>= 0:
		break