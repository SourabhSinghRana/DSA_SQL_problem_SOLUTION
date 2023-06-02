'''
Question 1
Given an integer array nums of length n and an integer target, find three integers
in nums such that the sum is closest to the target.
Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2

Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''


class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2] # initialize closest sum
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right: # two-pointer approach
                sum = nums[i] + nums[left] + nums[right]
                if sum == target: # sum equals target, return immediately
                    return sum
                elif sum < target:
                    left += 1
                else:
                    right -= 1
                if abs(sum - target) < abs(closest_sum - target): # update closest sum
                    closest_sum = sum
        return closest_sum
    
    
    
    
    

'''
Question 2
Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:
           ● 0 <= a, b, c, d < n
           ● a, b, c, and d are distinct.
           ● nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
'''



class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2] # initialize closest sum
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right: # two-pointer approach
                sum = nums[i] + nums[left] + nums[right]
                if sum == target: # sum equals target, return immediately
                    return sum
                elif sum < target:
                    left += 1
                else:
                    right -= 1
                if abs(sum - target) < abs(closest_sum - target): # update closest sum
                    closest_sum = sum
        return closest_sum
    

'''
<aside>
💡 **Question 3**
A permutation of an array of integers is an arrangement of its members into a
sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr:
[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically greater
permutation of its integer. More formally, if all the permutations of the array are
sorted in one container according to their lexicographical order, then the next
permutation of that array is the permutation that follows it in the sorted container.

If such an arrangement is not possible, the array must be rearranged as the
lowest possible order (i.e., sorted in ascending order).

</aside>
'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def reverse(nums, start):
            end = len(nums) - 1
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        reverse(nums, i + 1)
        
        
        
        
'''
Question 4
Given a sorted array of distinct integers and a target value, return the index if the
target is found. If not, return the index where it would be if it were inserted in
order.

You must write an algorithm with O(log n) runtime complexity.
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
Question 5
You are given a large integer represented as an integer array digits, where each
digits[i] is the ith digit of the integer. The digits are ordered from most significant
to least significant in left-to-right order. The large integer does not contain any
leading 0's.
'''

class Solution:
    def plusOne(self, digits):
        strings = ""
        for number in digits:
            strings += str(number)

        temp = str(int(strings) +1)

        return [int(temp[i]) for i in range(len(temp))]



'''
Question 6
Given a non-empty array of integers nums, every element appears twice except
for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only
constant extra space.
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}  

        
        for i in nums:
            if i not in dict: 
                dict[i] = True 
            else:
                dict[i] = False  

        
        for key, val in dict.items():
            if val == True:
                return key 



'''
Question 7
You are given an inclusive range [lower, upper] and a sorted unique integer array
nums, where all elements are within the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in
nums.
'''

class Solution:
    	def summaryRanges(self, nums: List[int]) -> List[str]:

		start = 0
		end = 0

		result = []

		while start < len(nums) and end<len(nums):

			if end+1 < len(nums) and nums[end]+1 == nums[end+1]:
				end=end+1

			else:
				if start == end:
					result.append(str(nums[start]))
					start = start + 1
					end = end + 1
				else:
					result.append(str(nums[start])+'->'+str(nums[end]))
					start = end + 1
					end = end + 1

		return result


'''
Question 8
Given an array of meeting time intervals where intervals[i] = [starti, endi],
determine if a person could attend all meetings.
'''

def canAttendMeetings(intervals):
        
    intervals.sort(key=lambda a: a.start)
    for i in range(len(intervals)-1):
        if intervals[i].end > intervals[i+1].start:
            return False
    return True