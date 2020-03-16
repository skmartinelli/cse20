
print("Make A > B")
a = int(input ("input a: "))
b = int(input ("input b: "))
r = 0

# K is an index
k = -1
R = []
A = []
P = []
Q = []


R.insert(-1,b)
R.insert(-2,a)

P.insert(-1,1)
P.insert(-2,0)

Q.insert(-1,0)
Q.insert(-2,1)

print("k                 r(k)             a(k)        p(k)               q(k)")
print("-2              ",R[-2],"            (none)            0              1")
print("-1               ",R[-1],"           (none)           1                 0")

while (R[k] != 0):
	k+=1
	A.insert(k, R[k-2]//R[k-1])
	R.insert(k, R[k-2] % R[k-1])
	P.insert(k, (A[k]*P[k-1]) + P[k-2])
	Q.insert(k, (A[k]*Q[k-1]) + Q[k-2])

	# I mixed up the order of inserting P and Q at the start so P and Q switched but it works lol
	print(k,"               ",R[k],"            ",A[k],"               ",Q[k],"             ", P[k])
	

	

print("Output is: ", k, "  ", R[k-1],"   ", P[k-1],"       ", Q[k-1])


# all the ps here are really Qs
if (k%2==0):
	negonepower = 1
	answer = (negonepower * P[k-1])
else:
	negonepower = -1
	answer = (negonepower * P[k-1]) + a

if (R[k-1] != 1):
	print("DNE THERE IS NO SOLUTION")

else: 
	print("the answer is ", answer)

	
	




