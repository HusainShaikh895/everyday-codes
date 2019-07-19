# comparison of running time for 
# memoization, iterative and non-memoized recursive approach
# to find n'th fibbonaci number
import time

def fibbo(n, memo):
	if(n==0):
		return 0
	elif(n==1):
		return 1
	elif(memo[n]==None):
		memo[n] = fibbo(n-1, memo) + fibbo(n-2, memo)
	return memo[n]

def fibboRec(n):
	if(n==0):
		return 0
	elif(n==1):
		return 1
	else:
		return fibboRec(n-1) + fibboRec(n-2)

def iterative(n):
	if(n<=1):
		return n
	first = 1
	second = 1
	while(n>2):
		current = first + second
		first, second = second, current
		n-=1
	return current

size = 200
memo = [None]*size
n = int(input("Enter the number: "))

startTime = time.time()
print("\nMemoized : ",fibbo(n, memo))
print("Memoization time : ",(time.time() - startTime))

startTime = time.time()
print("\nIterative : ",iterative(n))
print("Iterative time : ",(time.time() - startTime))

startTime = time.time()
print("\nNon - Memoized : ",fibboRec(n))
print("Non - Memoization time : ",(time.time() - startTime))
# conclusion : 
# as maximum recursive depth exceeds at around n = 800
# i didn't see any difference between memoized and iterative running time
# although they both beat normal recursive (non-memoized) approach to death
