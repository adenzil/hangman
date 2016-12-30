from random import randint
print("")

name = raw_input("enter your name : ")

print("")

print("hi "+name)

print("")

words = ["friction","timepass","monaco","exchange","target","floral","guitar","yapsurvey","cappuccino","apple"]
word = words[randint(0,9)]
temp = word
turns = 10
count = 0

print("We have randomly selected a word for you. Go ahead and guess that word, you have " + str(turns) + " turns.")

print("")

while turns>0:
	
	guess = raw_input("guess char : ")
	print("")
	state = False

	for char in temp:

		if guess == word:
			print("Genius !!")
			state = True
			count = len(word)
			break

		elif guess == char:

			print(guess+" exists")
			state = True
			count += 1
			temp = temp.replace(guess,"")
			break

	if state==False:
		turns -= 1
		print("wrong guess " + str(turns) + " turn left")

	print("")

	if len(word) == count:
		print("you won")
		break

if len(word) < count:
	print("game over")

print("")
print("the word was "+word)
print("")


