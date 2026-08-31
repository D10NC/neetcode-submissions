class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        leftPointer = 0
        longestLength = 0

        seen = {}

        for rightPointer in range(len(s)):
            seen[s[rightPointer]] = seen.get(s[rightPointer], 0) + 1

            while (rightPointer - leftPointer + 1) - max(seen.values()) > k:
                seen[s[leftPointer]] -= 1
                leftPointer += 1

            currentLength = rightPointer - leftPointer + 1
            
            if currentLength > longestLength:
                longestLength = currentLength

        return longestLength