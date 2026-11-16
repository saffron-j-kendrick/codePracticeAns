class Solution:
    def removeStars(self, s: str) -> str:
        self.stack = []

        for char in s:
            if char == "*":
                self.stack.pop()
            else:
                self.stack.append(char)
        
        
        result = ''.join(self.stack)
        return result