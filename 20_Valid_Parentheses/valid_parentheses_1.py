class Solution:
    def isValid(self, s: str) -> bool:

        # Map each closing bracket to its matching opening bracket
        h = {')': '(', '}': '{', ']': '['}

        # Store opening brackets
        stk = []

        # Check every character in the string
        for c in s:

            # Opening bracket → add it to the stack
            # eg. '(' : stack -> ['(']
            if c not in h:
                stk.append(c)

            # Closing bracket
            else:

                # No opening bracket available to match it
                if not stk:
                    return False

                # Remove the most recently added opening bracket
                popped = stk.pop()

                # Check whether it matches the closing bracket
                # eg. ')' closing bracket : '(' opening bracket
                if popped != h[c]:
                    return False

        # Valid only when no opening brackets are left
        return not stk