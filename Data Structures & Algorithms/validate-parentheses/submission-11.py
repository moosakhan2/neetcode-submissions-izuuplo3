class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for b in s:
            if b in brackets:
                if not stack:
                    return False
                top = stack.pop()
                if top != brackets[b]:
                    return False
            else:
                stack.append(b)
        
        return not stack