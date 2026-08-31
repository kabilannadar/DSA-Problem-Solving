class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # L starts at the beginning and R starts at the end
        L, R = 0, len(s) - 1

        # Keep moving both pointers toward each other until they meet
        while L < R:

            # If the left character is not a letter or number,
            # skip it by moving L to the right and contnue to check again
            if not s[L].isalnum():
                L += 1
                continue
            
            # If the right character is not a letter or number,
            # skip it by moving R to the left and continue to check again
            if not s[R].isalnum():
                R -= 1
                continue
            
            # Compare both characters after converting them to lowercase
            # If they are different, the string is not a palindrome
            if s[L].lower() != s[R].lower():
                return False
            
            # Move L and R, one position toward the center if all the above conditions are satisfied
            L += 1
            R -= 1
        
        # All valid characters matched, so it is a palindrome
        return True