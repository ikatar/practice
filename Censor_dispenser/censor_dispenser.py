import re

def censor(text,words_to_censor,double_occurrences):
	#removes words and negative words after 2 occurrences
	original_text = text
	text = text.lower()
	to_remove=[]

	for word in words_to_censor:
		word = re.compile(r"\b{word}\b".format(word=word))
		for m in word.finditer(text):
			to_remove.append([[m.group()],[m.start(),m.end()]])
	for word in to_remove:
		original_text = original_text[:word[1][0]] + "X"*len(word[0][0]) + original_text[word[1][1]:]

	to_remove =[]

	for word in double_occurrences:
		word = re.compile(r"\b{word}\b".format(word=word))
		for m in word.finditer(text):
			to_remove.append([[m.group()],[m.start(),m.end()]])
	
	to_remove.sort(key=lambda x: x[1][1])
	
	for word in to_remove[2:]:
		original_text = original_text[:word[1][0]] + "X"*len(word[0][0]) + original_text[word[1][1]:]

	return original_text

def censor_plus_next_words(text,list1,list2):
	big_list = list1+list2
	original_text = text
	text = text.lower()

	to_remove =[]

	for word in big_list:
		word = re.compile(r"\b\w*['-]?\w*\b ?\b{word}\b ?\b\w*['-]?\w*\b".format(word=word))
		for m in word.finditer(text):
			to_remove.append([[m.group()],[m.start(),m.end()]])
	to_remove.sort(key=lambda x: x[1][1])

	for word in to_remove:
		original_text = original_text[:word[1][0]] +"X"*len(word[0][0])+ original_text[word[1][1]:]
	return original_text

email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithms ", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressing", "distressed", "concerning", "horrible", "horribly", "questionable"]

print(censor(email_three,proprietary_terms,negative_words))
print(censor_plus_next_words(email_four,proprietary_terms,negative_words))

