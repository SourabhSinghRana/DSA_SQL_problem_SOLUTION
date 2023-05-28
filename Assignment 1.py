'''
<aside>
💡 **Q1.** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Example:**
Input: nums = [2,7,11,15], target = 9
Output0 [0,1]

</aside>
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        arrayDict = dict()
        
        for i in range(0, len(nums)):
            diff = target - nums[i]
            
            if(diff in arrayDict):
                return [arrayDict[diff], i]
            else:
                arrayDict[nums[i]] = i;
                
                
                
                
                
'''
<aside>
💡 **Q2.** Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
- Return k.

**Example :**
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_*,_*]

</aside>
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=0
        for v in nums:
            if v!=val:
                nums[j] = v
                j+=1
        return j
    


''' 
<aside>
💡 **Q3.** Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

**Example 1:**
Input: nums = [1,3,5,6], target = 5

</aside>
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums)-1
        mid = 0
        
        while(start <= end):
            mid = int((start+end)/2)
            if(target == nums[mid]):
                return mid
            elif(target > nums[mid]):
                start = mid + 1
            else:
                end = mid - 1
        
        if(target > nums[mid]):
            
            while(target < nums[mid] and mid<len(nums)):
                mid = mid+1
            
            return mid+1
        else:
            while(target > nums[mid] and mid>0):
                mid = mid-1
            
            return mid
        


        
'''
<aside>
💡 **Q3.** Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

**Example 1:**
Input: nums = [1,3,5,6], target = 5

</aside>
'''


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        n = len(digits)
        for i in reversed(range(n)):
            val = digits[i] + carry + 1 if i == n-1 else digits[i] + carry
            if val <= 9:
                digits[i] = val
                carry = 0
            else:
                carry = val // 10
                val -= 10
                digits[i] = val
        if carry:
            digits.insert(0, carry)
        return digits
    
    
    
    '''
    <aside>
💡 **Q5.** You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

**Example 1:**
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

</aside>
    '''
    
    
    class Solution:
        
        def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

            newLst = []
            i=j=0

            if(n != 0):
                for _ in range(len(nums1)):
                    if(j<n):
                        if(nums1[i] < nums2[j] and i<m):
                            newLst.append(nums1[i])
                            i+=1
                        else:
                            newLst.append(nums2[j])
                            j+=1
                    else:
                        newLst.append(nums1[i])
                        i+=1
                        
                print(newLst)
                for i in range(len(nums1)):
                    nums1[i] = newLst[i]     
                    
                    
'''
<aside>
💡 **Q7.** Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.

Note that you must do this in-place without making a copy of the array.

**Example 1:**
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

</aside>
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        l, r = 0, 0
        while r < len(nums):
            if nums[r] != 0:
                nums[l] = nums[r]
                r += 1
                l += 1
            else:
                r += 1
        
        while l < len(nums):
            nums[l] = 0
            l += 1



'''
<aside>
💡 **Q8.** You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

**Example 1:**
Input: nums = [1,2,2,4]
Output: [2,3]

</aside>
'''

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        toRemove = sum(nums) - sum(set(nums))
        actualMissing = sum(range(1, len(nums)+1)) - sum(set(nums))
        return [toRemove, actualMissing]