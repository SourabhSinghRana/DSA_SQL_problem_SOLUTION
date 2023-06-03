'''
<aside>
💡 **Question 1**
Given three integer arrays arr1, arr2 and arr3 **sorted** in **strictly increasing** order, return a sorted array of **only** the integers that appeared in **all** three arrays.

**Example 1:**

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]

Output: [1,5]

**Explanation:** Only 1 and 5 appeared in the three arrays.

</aside>
'''

class Solution:
    def arraysIntersection(
        self, arr1: List[int], arr2: List[int], arr3: List[int]
    ) -> List[int]:
        def find(arr, val):
            left, right = 0, len(arr) - 1
            while left < right:
                mid = (left + right) >> 1
                if arr[mid] >= val:
                    right = mid
                else:
                    left = mid + 1
            return arr[left] == val

        res = []
        for num in arr1:
            if find(arr2, num) and find(arr3, num):
                res.append(num)
        return res
    
    
    
    
'''
<aside>
💡 **Question 2**

Given two **0-indexed** integer arrays nums1 and nums2, return *a list* answer *of size* 2 *where:*

- answer[0] *is a list of all **distinct** integers in* nums1 *which are **not** present in* nums2*.*
- answer[1] *is a list of all **distinct** integers in* nums2 *which are **not** present in* nums1.

**Note** that the integers in the lists may be returned in **any** order.

**Example 1:**

**Input:** nums1 = [1,2,3], nums2 = [2,4,6]

**Output:** [[1,3],[4,6]]

</aside>
'''

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1=set(nums1)
        n2=set(nums2)
        r1=list(set(x for x in nums1 if x not in n2))
        r2=list(set(x for x in nums2 if x not in n1))
        return [r1,r2]
    


    
'''
<aside>
💡 **Question 3**
Given a 2D integer array matrix, return *the **transpose** of* matrix.

The **transpose** of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

**Example 1:**

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]

Output: [[1,4,7],[2,5,8],[3,6,9]]

</aside>
'''


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n=len(matrix),len(matrix[0])
        ans = [[None] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                ans[j][i]=matrix[i][j]
        
        return ans
    
    
    
    
    
'''
<aside>
💡 **Question 4**
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is **maximized**. Return *the maximized sum*.

**Example 1:**

Input: nums = [1,4,3,2]

Output: 4

</aside>
'''


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0
        numsLen = len(nums)
        for i in range(0, numsLen - 1, 2):
            result += nums[i]
        return result
    
    
    
    
    
'''
<aside>
💡 **Question 5**
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase **may be** incomplete.

Given the integer n, return *the number of **complete rows** of the staircase you will build*.

</aside>
'''


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
💡 **Question 6**
Given an integer array nums sorted in **non-decreasing** order, return *an array of **the squares of each number** sorted in non-decreasing order*.

**Example 1:**

Input: nums = [-4,-1,0,3,10]

Output: [0,1,9,16,100]

**Explanation:** After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100]

</aside>
'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        # Two Pointer Approach
        n = len(nums)
        l, r = 0, n - 1
        k = n - 1
        ans = [0] * n
        while k >= 0:
            if abs(nums[l]) > nums[r]:
                ans[k] = nums[l] * nums[l]
                l += 1
            else:
                ans[k] = nums[r] * nums[r]
                r -= 1
            k -= 1
        return ans
    
    
'''
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

*Return the array in the form* [x1,y1,x2,y2,...,xn,yn].
'''


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr1=[]
        arr2=[]
        arr3=[]
        for i in range(n):
            arr1.append(nums[i])
        for i in range(n,2*n):
            arr2.append(nums[i])
        for i in range(n):
            arr3.append(arr1[i])
            arr3.append(arr2[i])
        return arr3