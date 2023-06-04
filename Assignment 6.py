'''
<aside>
💡 **Question 1**

A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

- s[i] == 'I' if perm[i] < perm[i + 1], and
- s[i] == 'D' if perm[i] > perm[i + 1].

Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return **any of them**.

</aside>
'''


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        L,ic,dc=[],0,len(s)
        for i in s:
            if i=='I':
                L.append(ic)
                ic+=1
            else:
                L.append(dc)
                dc-=1
        if s[-1]=='I':L.append(ic)
        else:L.append(dc)
        return L
    
    
''
Given an array of integers arr, return *true if and only if it is a valid mountain array*.

Recall that arr is a mountain array if and only if:

- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that:
''

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) >=3 :
            
            peak = arr.index(max(arr))
            
            if peak!=0 and peak!=len(arr)-1:
                
                left = arr[:peak]
                left_s = sorted(left)

                right = arr[peak:]
                right_s = sorted(right,reverse=True)

                R_A = len(right_s)
                R_B = len(set(right))
                L_A = len(left_s)
                L_B = len(set(left))

                if left_s == left and L_A == L_B and right_s == right and R_A == R_B:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

                    
            
            
'''
The **product sum** of two equal-length arrays a and b is equal to the sum of a[i] * b[i] for all 0 <= i < a.length (**0-indexed**).

- For example, if a = [1,2,3,4] and b = [5,2,3,1], the **product sum** would be 1*5 + 2*2 + 3*3 + 4*1 = 22.

Given two arrays nums1 and nums2 of length n, return *the **minimum product sum** if you are allowed to **rearrange** the **order** of the elements in* nums1.
'''


def minValue(A, B, n):

    A.sort()
    B.sort()

    result = 0
    for i in range(n):
        result += (A[i] * B[n - i - 1])
 
    return result
 
 
A = [3, 1, 1]
B = [6, 5, 4]
n = len(A)
print (minValue(A, B, n))



'''
An integer array original is transformed into a **doubled** array changed by appending **twice the value** of every element in original, and then randomly **shuffling** the resulting array.

Given an array changed, return original *if* changed *is a **doubled** array. If* changed *is not a **doubled** array, return an empty array. The elements in* original *may be returned in **any** order*.
'''

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
        data = Counter(changed)
        result = []
        for k in sorted(data):
            if data[k] < 0:
                return []
            elif k == 0:
                x, y = divmod(data[k], 2)
                if y == 1:
                    return []
                result += [0] * x
            elif data[k] > 0:
                value = k * 2
                if data[value] == 0:
                    return []
                min_value = min(value, data[k])
                result += [k] * min_value
                data[k] -= min_value
                data[value] -= min_value
        return result
    


''
Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.
''

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        r1, c1, c2 = len(mat1), len(mat1[0]), len(mat2[0])
        res = [[0] * c2 for _ in range(r1)]
        mp = defaultdict(list)
        for i in range(r1):
            for j in range(c1):
                if mat1[i][j] != 0:
                    mp[i].append(j)
        for i in range(r1):
            for j in range(c2):
                for k in mp[i]:
                    res[i][j] += mat1[i][k] * mat2[k][j]
        return res