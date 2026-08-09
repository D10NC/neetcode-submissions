class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numberSet = set(nums)

        longest = 0

        for i in numberSet:
            
            if i-1 not in numberSet:
                count = 1
                next = i+1
                while next in numberSet:
                    count += 1
                    next += 1
                longest = max(longest, count)

        return longest

        