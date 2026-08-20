class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # closing : opening {keys: values}
        pairs = {')': '(', ']': '[', '}': '{'}

        for char in s:
            #check if its a opening bracket
            if char not in pairs:
                #push onto stack
                stack.append(char)
                continue

            #check if its closing
            if char in pairs:
                # check if stack is empty or does it not match the last added item
                if not stack or pairs[char] != stack[-1]:
                    return False

                # pop if it does
                stack.pop()

        return not stack
# (){} valid