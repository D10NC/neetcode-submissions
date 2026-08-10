class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        pairs = { ")" : "(" ,"]" : "[" , "}" : "{" }

        for character in s:
            if character in pairs:
                if not stack:
                    return False
                if stack.pop() != pairs[character]:
                    return False
                
            else:
                    stack.append(character)
        
        return not stack