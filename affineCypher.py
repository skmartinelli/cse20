


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

		#print(outputCharposition)


