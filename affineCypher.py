


def alphabet_position(text):
	nums = [str(ord(x)-96) for x in text.lower() if x>= 'a' and x<='z']
	return " ".join(nums)







encordec= input("(e)ncrypt or (d)ecrypt? ")
a = int(input("value of a? "))
b = int(input("value of b? "))
string = input("whats the string to encrypt / decrypt? ")


if (encordec=="e"):
	for element in range(0, len(string)):
		letter = string[element]
		position = ord(letter)-97
		outputCharposition=int(((a*position)+b)%26)
		
		print(chr(outputCharposition+97))

if (encordec=="d"):
	for element in range(0, len(string)):
		letter = string[element]
		position = ord(letter)-97
		
		if (a==19):
			mult=11

		elif (a==9):
			mult=3
		elif (a==21):
			mult=5
		elif (a==15):
			mult=7
		elif (a==23):
			mult=17
		elif (a==3):
			mult=9
		elif (a==5):
			mult=27
		elif (a==7):
			mult=15
		elif (a==11):
			mult=19
		elif (a==17):
			mult=23
		elif (a==25):
			mult=25
		else:
			print("nice job, a doesn't have an inverse")

		outputCharposition= int((mult*(position-b))%26)
		print(chr(outputCharposition+97))

		

