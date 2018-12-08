#Beals Conjecture:
#If A**x + B**y = C**z, where A, B, C, x, y and z are positive integers and x, y 
# and z are all greater than 2, then A, B and C must have a common prime factor.

#We attempt to provide a counterexample that satifies the following:
#Ax + By must equal Cz
#A, B, C, x, y, z must all be positive integers
#x, y, z must all be greater than 2
#A, B, C must have no common factor (other than 1).

#I am going to try all possible combinations of A,B,C,x,y,z up to 23,
#which I calculate to be 97,336,000 combinations. 
#Hopefully my Raspberry Pi doesn't melt. 
#Also, I don't actually expect to find anything interesting
#I just thought this would be a fun experiment. 

#Maybe in the future I will try to clean this up and optimize it a bit. 

import math
import random

solved = False
solution = []
equationsoln = []


def primeFactors(n): 
	factorization = set()

	while n % 2 == 0: 
		factorization.add(int(2))
		n = n / 2
          
	for i in range(3,int(math.sqrt(n))+1,2): 
		while n % i== 0: 
			factorization.add(int(i))
			n = n / i 
	
	if n > 2: 
		factorization.add(int(n))

	return factorization

def nocommonpf(A,B,C):
	X = primeFactors(A)
	Y = primeFactors(B)
	Z = primeFactors(C)
	if X & Y & Z:
		return False	
	else:
		print("You either ran out of numbers, screwed something up, broke something, or you're really rich.")
		return True


for A in range(1,23):
	for B in range(1,23):
		for C in range(1,23):
			for x in range(3,23):
				for y in range(3,23):
					for z in range(3,23):

						if (A**x) + (B**y) == (C**z):
							equationsoln.append((A,B,C,x,y,z)) #Just for fun
							if nocommonpf(A,B,C):
								solution.append([A,B,C,x,y,z])
print(solution)
print(equationsoln)
								




