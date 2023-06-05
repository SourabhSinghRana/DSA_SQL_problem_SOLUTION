'''
Given an integer `n`, return *`true` if it is a power of two. Otherwise, return `false`*.

An integer `n` is a power of two, if there exists an integer `x` such that `n == 2x`.
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return bin(n)[2:].rstrip('0') == '1'
    
    
    
'''
Given a number n, find the sum of the first natural numbers.
'''


def findSum(n):
	sum = 0
	x = 1
	while x <= n:
		sum = sum + x
		x = x + 1
	return sum


n = 5
print findSum(n)



'''
Given a positive integer, N. Find the factorial of N. 
'''

def factorial(n):
	
	if n == 0:
		return 1
	
	return n * factorial(n-1)

num = 5;
print("Factorial of", num, "is",
factorial(num))




''
Given a number N and a power P, the task is to find the exponent of this number raised to the given power, i.e. N^P.
''

def power(N, P):

	if P == 0:
		return 1

	return (N*power(N, P-1))


if __name__ == '__main__':
	N = 5
	P = 2

	print(power(N, P))



'''
Given an array of integers arr, the task is to find maximum element of that array using recursion.
'''


def findMinRec(A, n):

	if (n == 1):
		return A[0]
	return min(A[n - 1], findMinRec(A, n - 1))


if __name__ == '__main__':
	A = [1, 4, 45, 6, -50, 10, 2]
	n = len(A)
	print(findMinRec(A, n))
 
 
 
 
 
'''
Given first term (a), common difference (d) and a integer N of the Arithmetic Progression series, the task is to find Nth term of the series.
'''



def Nth_of_AP(a, d, N) :
	return (a + (N - 1) * d)
	

a = 2 
d = 1 
N = 5 


print( "The ", N ,"th term of the series is : ",
	Nth_of_AP(a, d, N))


'''
Given a string S, the task is to write a program to print all permutations of a given string.
'''


def toString(List):
	return ''.join(List)


def permute(a, l, r):
	if l == r:
		print(toString(a))
	else:
		for i in range(l, r):
			a[l], a[i] = a[i], a[l]
			permute(a, l+1, r)
			a[l], a[i] = a[i], a[l]



string = "ABC"
n = len(string)
a = list(string)


permute(a, 0, n)





'''
Given an array, find a product of all array elements.
'''

arr=[1,2,3,4,5]
product=1


i=0
j=len(arr)-1


while(i<j):
	product*=arr[i]*arr[j]
	i+=1
	j-=1
	

if(i==j):
	product*=arr[i]

print(product)


