a = int(input ("input a: "))
b = int(input ("input b: "))
r = 0
print("a             b               r")
while (b !=0):
	r=a%b
	a=b
	b=r
	print(a, "         ", b, "          ", r)

print("final gcd is: ", a)
	
