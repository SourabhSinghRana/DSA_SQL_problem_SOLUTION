'''
Question 1:- Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2),
..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
'''

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        nums.sort()

        max_sum = 0
        
        for i in range(0, len(nums), 2):
            max_sum += min(nums[i], nums[i+1]) 

        return max_sum
    
    
    
'''
Question 2
Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started
to gain weight, so she visited a doctor.
'''

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        limit = len(candyType)/2

        diff = {}
        for candy in candyType:
            if(candy not in diff.keys()):
                diff[candy] = 1


        return int(min(limit, len(diff.keys())))
    
    
    
'''
Question 4
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.
'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if(n==0): return True

        if(len(flowerbed)==1 and flowerbed[0]==0 and n==1):
            return True
        elif(len(flowerbed)==1 and flowerbed[0]==1 and n==1): 
            return False    

        l = 0
        r = 0
        for i, x in enumerate(flowerbed):
            if x==1:
                l = i-1-1
                r = i+1+1
                break

        while(l>=0):
            if(flowerbed[l]==0 and flowerbed[l+1]==0):
                if(l-1 < 0):
                    flowerbed[l] = 1
                    n -= 1  
                elif(flowerbed[l-1] == 0):
                    flowerbed[l] = 1
                    n -= 1
            l-=1
            if(n<=0): return True

        while(r<=len(flowerbed)-1):
            if(flowerbed[r]==0 and flowerbed[r-1]==0):
                if(r+1 > len(flowerbed)-1):
                    flowerbed[r] = 1
                    n -= 1
                elif(flowerbed[r+1] == 0):
                    flowerbed[r] = 1
                    n -= 1
            r+=1
            if(n<=0): return True    

        return False
    
    
    
    
'''
Question 6
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise,
return -1.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Explanation: 9 exists in nums and its index is 4
'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        length = len(nums)
        
        start = 0
        mid = int(length-1 / 2)
        end = length-1
        
        while(start <= end):
            #print(start, mid, end)
            if(target == nums[mid]):
                return mid
            elif(target > nums[mid]):
                start = mid+1
            else:
                end = mid-1
            mid =  int((start+end)/2)   

        return -1             
    
    
'''
Question 7
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is
monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Example 1:
Input: nums = [1,2,2,3]
Output: true
'''  
    
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
       inc = True
       dec = True
       for i in range(1,len(nums)):
           inc = inc and nums[i-1] >= nums[i]
           dec = dec and nums[i-1] <= nums[i]
       return inc or dec
