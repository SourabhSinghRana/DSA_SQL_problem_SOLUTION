
''' 
Convert 1D Array Into 2D Array

You are given a **0-indexed** 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with creating a 2-dimensional (2D) array with  m rows and n columns using **all** the elements from original.

The elements from indices 0 to n - 1 (**inclusive**) of original should form the first row of the constructed 2D array, the elements from indices n to 2 * n - 1 (**inclusive**) should form the second row of the constructed 2D array, and so on.
'''



    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        if len(original) == m * n:
            for r in range(m):
                ans.append([])
                for c in range(n):
                    ans[-1].append(original[r * n + c])
        return ans
    
    
    
    
    
'''  <aside>
💡 **Question 2**

You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase **may be** incomplete.

</aside>'''



class Solution:
    def arrangeCoins(self, n: int) -> int:
        coin_counter = 0
        rows = 0
        
        if n == 1:
            return 1

        while coin_counter+(rows+1) <= n:
            rows += 1
            coin_counter = coin_counter + rows
        
        return rows
    
    
    
    
'''
<aside>
💡 **Question 3**

Given an integer array nums sorted in **non-decreasing** order, return *an array of **the squares of each number** sorted in non-decreasing order*.

**Example 1:**

**Input:** nums = [-4,-1,0,3,10]

**Output:** [0,1,9,16,100]

</aside>
'''


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if(nums[0]<0):
            beg = 0
            end = n-1
            i = n-1
            
            newLst = [None]*n
            while(i>=0):
                if(nums[beg]*nums[beg] > nums[end]*nums[end]):
                    newLst[i] = nums[beg]*nums[beg]
                    beg += 1
                else:
                    newLst[i] = nums[end]*nums[end]
                    end -= 1
                i -= 1  
                
            return newLst 
        
        else:
            for i in range(n):
                nums[i] *= nums[i]
            return nums
        
        
        
'''
<aside>
💡 **Question 4**

Given two **0-indexed** integer arrays nums1 and nums2, return *a list* answer *of size* 2 *where:*

- answer[0] *is a list of all **distinct** integers in* nums1 *which are **not** present in* nums2*.*
- answer[1] *is a list of all **distinct** integers in* nums2 *which are **not** present in* nums1.

**Note** that the integers in the lists may be returned in **any** order.

</aside>
'''


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        # define set to store elements
        s1 = set(nums1)
        s2 = set(nums2)

        # define output
        out = [[],[]]

        # adding the elements to output if not contains in the set
        for i in s1:
            if i not in s2:  
                out[0].append(i)
        for i in s2:
            if i not in s1:
                out[1].append(i)
        
        return out
    
    
    
    
'''
Given two integer arrays arr1 and arr2, and the integer d, *return the distance value between the two arrays*.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.
'''

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        distance = len(arr1)
        for num in arr1:
            start = 0
            end = len(arr2) - 1
            while start <= end:
                mid = (start+end)//2
                if abs(num- arr2[mid]) <= d:
                    distance -= 1
                    break
                elif arr2[mid] > num :
                    end = mid-1
                elif arr2[mid] < num :
                    start = mid+1
        return distance
    
    
    

''
An integer array original is transformed into a **doubled** array changed by appending **twice the value** of every element in original, and then randomly **shuffling** the resulting array.

Given an array changed, return original *if* changed *is a **doubled** array. If* changed *is not a **doubled** array, return an empty array. The elements in* original *may be returned in **any** order*.
''

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
