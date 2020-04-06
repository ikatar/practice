from sys import argv
import csv 

#get the small or large list 
fileName = argv[1]

#get the DNA sequence file 
dnaFile = open(argv[2],"r")
dna = dnaFile.readline()

def main(str,dna):
	#Final match name defined in case no match was found
	Name = "none"
	#make a dict with proper values depending on the amount of them
	values = {}
	
	with open(fileName,"r") as file:
		reader = csv.DictReader(file)
		for row in reader:
			for x in row:
				values[x] = "0"
			values.pop("name")
	
	#let's find some mathces 				
	for key in values:
		kl = len(key)
		finalValue = 0
		counter = 0
		
		# go through each letter 
		for x in range(len(dna)):
			
			#reset the counter to avoid addint previous count 
			if counter>0:
				counter = 0
				continue
				
			# example x: x + kl == AGATC, where x is "A" and x+kl is "A" + 5 letters A+G+A+T+C
			if dna[x: x + kl] == key:
				while dna[x - kl: x] == dna[x: x +kl]:
					counter += 1
					#skip over "kl" letters forward to find the next match if present 
					x += kl
				
				#storing the new value 
				if counter > finalValue:
					finalValue = counter+1
		
		# final and the highest value to add to our dict
		values[key] = finalValue
	
	#finally we need to find a match among people in database 
	with open(fileName,"r") as file:
		reader = csv.DictReader(file)
		
		for row in reader:
			copyRow = row.copy()
			copyRow.pop("name")
			
			for value in copyRow:
				#we need to convert value to int since by defaullt it's a string 
				if values[value] == int(copyRow[value]):
					Name = row["name"]
	print ("Provided sequence has matches with\n" + Name)

main(fileName,dna)