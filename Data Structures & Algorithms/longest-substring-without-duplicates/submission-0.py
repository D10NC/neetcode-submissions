class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longestLength = 0
        leftPointer = 0

        seen = {}

        for rightPointer in range(len(s)):
            if s[rightPointer] in seen and seen[s[rightPointer]] >= leftPointer:
                leftPointer = seen[s[rightPointer]] + 1
            
            seen[s[rightPointer]] = rightPointer

            currentLength = rightPointer - leftPointer + 1 
            if currentLength > longestLength:
                longestLength = currentLength
            
        return longestLength


        