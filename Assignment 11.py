'''
Given a non-negative integer `x`, return *the square root of* `x` *rounded down to the nearest integer*. The returned integer should be **non-negative** as well.

You **must not use** any built-in exponent function or operator.
'''


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x < 2:
            return x
        
        start = 0
        end = x/2
        
        while (start <= end):
            
            mid = int((start + end) / 2)
            
            square = mid * mid
            
            if square == x:
                return mid
            
            if square > x:
                end = mid - 1
                
            else:
                start = mid + 1
                
        return end
    
    
'''
A peak element is an element that is strictly greater than its neighbors.

Given a **0-indexed** integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any of the peaks**.

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in `O(log n)` time.
'''


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] < nums[mid + 1]:
                l =  mid + 1
            else:
                r = mid 
        return l
    
    
    
'''
Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only **one repeated number** in `nums`, return *this repeated number*.

You must solve the problem **without** modifying the array `nums` and uses only constant extra space.
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            ind = abs(num)
            
            if nums[ind] < 0:
                return ind
            
            nums[ind] *= -1 
            
            
            
'''
Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated `4` times.
- `[0,1,2,4,5,6,7]` if it was rotated `7` times.
'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low,high=0,len(nums)-1
        n=len(nums)
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]<=nums[(mid-1+n)%n] and nums[mid]<=nums[(mid+1)%n]:
                return nums[mid]
            if nums[mid]>=nums[low]:
                if nums[high]>=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                high=mid-1

        return -1
    
    
    
'''
Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if(len(nums) < 1): return [-1,-1]
        
        if(len(nums) == 1):
            if(nums[0]!=target): return [-1,-1]
            return [0,0]
        
        start, end = 0, len(nums)-1
        
        index = [-1,-1]
        
        while(start <= end):
            mid = int((start+end)/2)
            if(target==nums[mid]):
                i = mid
                print(i, nums[i])
                while(i>=0):
                    print(i, nums[i])
                    if(nums[i] != target):
                        index[0] = i+1
                        break
                    else:
                        index[0] = i
                        i-=1
                                   
                i = mid
                while(i<len(nums)):
                    print(i, nums[i])
                    if(nums[i] != target):
                        index[1] = i-1
                        break  
                    else:
                        index[1] = i
                        i+=1 
                break
            elif(target > nums[mid]):
                start = mid + 1
            else:
                end = mid - 1
               
        
        return index