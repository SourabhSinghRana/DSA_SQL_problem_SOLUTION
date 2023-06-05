'''
Given an integer `n`, return *`true` if it is a power of three. Otherwise, return `false`*.

An integer `n` is a power of three, if there exists an integer `x` such that `n == 3x`.
'''

import math
b = 81
a = 3

p = math.log(b) / math.log(a)

if (p - int(p) == 0):
	print("YES")

else:
	print("NO")





'''
You have a list `arr` of all integers in the range `[1, n]` sorted in a strictly increasing order. Apply the following algorithm on `arr`:

- Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
- Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
- Keep repeating the steps again, alternating left to right and right to left, until a single number remains.
'''

from math import log2, floor

class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return 1
        c = floor(log2(n))
        m = 0  # 2^i * k + m remains
        p = 1
        for i in range(1, c):
            p <<= 1
            if i % 2 == 0:
                first = m if m > 0 else p
                if first % (2 * p) == m:
                    m += p
            else:
                last = ((n - m) // p) * p + m
                if last % (2 * p) == m:
                    m += p
        return m if m > 0 else 2 * p
    
    
    
    
'''
Given a set represented as a string, write a recursive code to print all subsets of it. The subsets can be printed in any order.

**Example 1:**

Input :  set = “abc”

Output : { “”, “a”, “b”, “c”, “ab”, “ac”, “bc”, “abc”}
'''


def powerSet(str1, index, curr):
	n = len(str1)

	if (index == n):
		return

	print(curr)

	for i in range(index + 1, n):
		curr += str1[i]
		powerSet(str1, i, curr)

		curr = curr.replace(curr[len(curr) - 1], "")

	return



if __name__ == '__main__':
	str = "abc"
	powerSet(str, -1, "")
 
 
 
 
'''
Given a string calculate length of the string using recursion.

**Examples:**
'''

str = "GeeksforGeeks"


def string_length(str) :
	

	if str == '':
		return 0
	else :
		return 1 + string_length(str[1:])
	

print (string_length(str))



'''
We are given a string S, we need to find count of all contiguous substrings starting and ending with same character.

**Examples :**
'''

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a = b = c = 0                       
        ans, i, n = 0, 0, len(s)            
        for j, letter in enumerate(s):       
            if letter == 'a': a += 1        
            elif letter == 'b': b += 1
            else: c += 1
            while a > 0 and b > 0 and c > 0: 
                ans += n-j                  
                if s[i] == 'a': a -= 1       
                elif s[i] == 'b': b -= 1
                else: c -= 1
                i += 1                     
        return ans    
    
    
    
'''
The tower of Hanoi is a famous puzzle where we have three rods and N disks. The objective of the puzzle is to move the entire stack to another rod. You are given the number of discs N. Initially, these discs are in the rod 1. You need to print all the steps of discs movement so that all the discs reach the 3rd rod. Also, you need to find the total moves.Note: The discs are arranged such that the top disc is numbered 1 and the bottom-most disc is numbered N. Also, all the discs have different sizes and a bigger disc cannot be put on the top of a smaller disc. Refer the provided link to get a better clarity about the puzzle.
'''

def move(disks, source=1, auxiliary=2, target=3):
     
    if disks > 0:
 
        # move `n-1` discs from source to auxiliary using the target
        # as an intermediate pole
        move(disks - 1, source, target, auxiliary)
 
        # move one disc from source to target
        print(f'Move disk {disks} from {source} —> {target}')
 
        # move `n-1` discs from auxiliary to target using the source
        # as an intermediate pole
        move(disks - 1, auxiliary, source, target)
 
 
# Tower of Hanoi Problem
if __name__ == '__main__':
 
    n = 3
    move(n)
 
 
 
 
 
'''
Given a string, count total number of consonants in it. A consonant is an English alphabet character that is not vowel (a, e, i, o and u). Examples of constants are b, c, d, f, and g.
'''


def isConsonant(ch):

	ch = ch.upper()
	return not (ch == 'A' or ch == 'E' or
				ch == 'I' or ch == 'O' or
				ch == 'U') and ord(ch) >= 65 and ord(ch) <= 90

def totalConsonants(string):
	count = 0
	for i in range(len(string)):
		if (isConsonant(string[i])):
			count += 1
			
	return count


string = "abc de"
print(totalConsonants(string))

