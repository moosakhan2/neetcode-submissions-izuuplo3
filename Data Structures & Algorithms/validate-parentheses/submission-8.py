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
                top = stack.pop() if stack else ''
                if top != brackets[b]:
                    return False
            else:
                stack.append(b)
        
        return stack == []