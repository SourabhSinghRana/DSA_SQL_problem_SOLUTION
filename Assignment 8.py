'''
Given two strings s1 and s2, return *the lowest **ASCII** sum of deleted characters to make two strings equal*.

**Example 1:**

**Input:** s1 = "sea", s2 = "eat"

**Output:** 231
'''

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
        for i in range(len(s1)-1,-1,-1):
            for j in range(len(s2)-1,-1,-1):
                if s1[i] == s2[j]:
                    dp[i][j] = ord(s1[i]) + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])                    
        total = 0
        for c in s1:
            total += ord(c)
        for c in s2:
            total += ord(c)
        return total - dp[0][0]*2
    
    
    
'''
Given a string s containing only three types of characters: '(', ')' and '*', return true *if* s *is **valid***.

The following rules define a **valid** string:

- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == ")":
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1
            
            if leftMax < 0:
                return False
            elif leftMin < 0:
                leftMin = 0
        
        return leftMin == 0
    
    
    
'''
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.
You always start to construct the **left** child node of the parent first if it exists.
'''


    def tree2str(self, root: Optional[TreeNode]) -> str:
                    
        if(root == None):
            return ""
        
        output: str = str(root.val)
        
        if (root.left != None or root.right != None):
            output += "(" + self.tree2str(root.left) + ")"
            
        if (root.right != None):
            output += "(" + self.tree2str(root.right) + ")"          
        
        return output;    
    
    
    

'''
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of **consecutive repeating characters** in chars:

- If the group's length is 1, append the character to s.
- Otherwise, append the character followed by the group's length.

The compressed string s **should not be returned separately**, but instead, be stored **in the input character array chars**. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
'''



ass Solution:
    def compress(self, chars: List[str]) -> int:
        wrt_pointer, chk_pointer = 0, 0
        current_char = None
        current_len = 0
        
        while chk_pointer < len(chars):
            if chars[chk_pointer] != current_char:
                # a new character
                if current_len > 1:
                    len_str = []
                    while current_len:
                        len_str.append(str(current_len % 10))
                        current_len = current_len // 10
                    for lstr in len_str[::-1]:
                        chars[wrt_pointer] = lstr
                        wrt_pointer += 1
                chars[wrt_pointer] = chars[chk_pointer]
                wrt_pointer += 1
                current_char = chars[chk_pointer]
                current_len = 1
            else:
                # the same character
                current_len += 1
            chk_pointer += 1
        
        if current_len > 1:
            len_str = []
            while current_len:
                len_str.append(str(current_len % 10))
                current_len = current_len // 10
            for lstr in len_str[::-1]:
                chars[wrt_pointer] = lstr
                wrt_pointer += 1
        return wrt_pointer
    
    
    
    
'''
Given two strings s and p, return *an array of all the start indices of* p*'s anagrams in* s. You may return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

    def findAnagrams(self, s: str, p: str) -> List[int]:
        hm, res, pL, sL = defaultdict(int), [], len(p), len(s)
        if pL > sL: return []

        # build hashmap
        for ch in p: hm[ch] += 1

        # initial full pass over the window
        for i in range(pL-1):
            if s[i] in hm: hm[s[i]] -= 1
            
        # slide the window with stride 1
        for i in range(-1, sL-pL+1):
            if i > -1 and s[i] in hm:
                hm[s[i]] += 1
            if i+pL < sL and s[i+pL] in hm: 
                hm[s[i+pL]] -= 1
                
            # check whether we encountered an anagram
            if all(v == 0 for v in hm.values()): 
                res.append(i+1)
                
        return res
    
    
    
    
'''
Given two strings s and goal, return true *if you can swap two letters in* s *so the result is equal to* goal*, otherwise, return* false*.*

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].
'''


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(s)
        diffs = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diffs.append((s[i], goal[i]))
        return len(diffs) == 2 and diffs[0] == diffs[1][::-1]