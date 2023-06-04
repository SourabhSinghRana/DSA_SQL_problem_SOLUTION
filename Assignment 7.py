'''
Given two strings s and t, *determine if they are isomorphic*.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
'''

# Time Complexity : O(n)
class Solution(object):
    def isIsomorphic(self, s, t):
        map1 = []
        map2 = []
        for idx in s:
            map1.append(s.index(idx))
        for idx in t:
            map2.append(t.index(idx))
        if map1 == map2:
            return True
        return False
    
    
'''
Given a string num which represents an integer, return true *if* num *is a **strobogrammatic number***.

A **strobogrammatic number** is a number that looks the same when rotated 180 degrees (looked at upside down).
'''


def strobogrammatic_num(n):
	
	result = numdef(n, n)
	return result
	
def numdef(n, length):
	
	if n == 0: return [""]
	if n == 1: return ["1", "0", "8"]
	
	middles = numdef(n - 2, length)
	result = []
	
	for middle in middles:
		if n != length:		
			result.append("0" + middle + "0")

		result.append("8" + middle + "8")
		result.append("1" + middle + "1")
		result.append("9" + middle + "6")
		result.append("6" + middle + "9")
	return result

if __name__ == '__main__':
	
	print(strobogrammatic_num(3))
 
 
 
'''
Given two non-negative integers, num1 and num2 represented as string, return *the sum of* num1 *and* num2 *as a string*.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
'''


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)
        n=int(num1)
        n1=int(num2)
        n2=n+n1
        return str(n2)


'''
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.
'''

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        temp = []
        first = 0
        last = k-1                 
        while (first <= len(s)-1):     
            if last > len(s)-1:
                last = len(s) - 1
            while(last >= first): 
                temp.append(s[last])  
                last = last - 1
            first = first + k                 
            last = first + (k-1)
            while(last >= first):
                if first > len(s)-1:
                    break
                temp.append(s[first])  
                first = first + 1                
            last = first + (k-1)       
        return ''.join(temp)
            
            
            
'''
Given two strings s and t, return true *if they are equal when both are typed into empty text editors*. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        
        def finalSTR(str1: str) -> str:
            countHash = 0
            endStr = ''
            for i in range(len(str1)-1, -1, -1):
                if(str1[i] == '#'):
                    countHash += 1
                elif(countHash > 0):
                    countHash -= 1
                else:
                    endStr = str1[i] + endStr
                    
            return endStr
        
        if(finalSTR(s) == finalSTR(t)):
            return True
        
        return False
        
        
        
'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
'''


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1,y1=coordinates[0][0],coordinates[0][1]
        x2,y2=coordinates[1][0],coordinates[1][1]
        for x3,y3 in coordinates[2:]:
            if (y3-y1)*(x2-x1)!=(x3-x1)*(y2-y1):
                return False
        else:
            return True