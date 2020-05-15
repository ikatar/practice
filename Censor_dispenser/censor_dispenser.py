import re

def censor(text,words_to_censor,double_occurrences):
	#removes words and negative words after 2 occurrences
	text = text.lower()
	for word in words_to_censor:
		#text = text.lower().replace(word," === ")
		text = re.sub(r"\b{w}\b".format(w=word),"X"*len(word),text)

	count = {}
	count_sorted = {}
	for word in double_occurrences:
		if word in text:
			try:
				count[word]= re.search(r"\b{word}\b".format(word=word),text).start()
			except Exception:
				pass
	for k in sorted(count,key=count.get):
		count_sorted[k] = count[k]
	
	to_remvoe=list(count_sorted.keys())
	
	for i in to_remvoe[2:]:
		text = text.replace(i,"X"*len(i))
	return text

def censor_plus_next_words(text,list1,list2):
	big_list = list1+list2
	text = text.lower()
	for word in big_list:
		text = re.sub(r"\w*'?\w? {w} \w*'?\w?".format(w=word),"X"*len(word)+"",text)
	return text

email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithms ", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

print(censor(email_three,proprietary_terms,negative_words ))
print(censor_plus_next_words(email_four,proprietary_terms,negative_words))
