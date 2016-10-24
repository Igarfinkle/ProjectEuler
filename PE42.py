import HelperFunctions
listOfTriangleNumbers = list(HelperFunctions.polygonal(i,3) for i in range(40) )


infile = open("p042_words.txt", "r")
wordlist = list(word[1:-1] for word in infile.readline().split(','))

count = 0
for word in wordlist:

	sum=0
	for char in word:
		sum+=HelperFunctions.uppercase_letter_to_number(char)
	if sum in listOfTriangleNumbers:
		count+=1
		print word

print count