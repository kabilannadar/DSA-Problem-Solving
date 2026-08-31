class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Negative numbers are not palindromes.
        if x < 0:
            return False

        # Save the original number because x will change in the loop.
        org = x

        # Start with reversed number as 0.
        rev_num = 0

        # Keep taking digits from x until nothing is left.
        while x > 0:

            # Take the last digit from x.
            # Example: 121 % 10 = 1
            digit = x % 10

            # Add the new digit to the end of rev_num.
            # Example:
            # 0 * 10 + 1 = 1
            # 1 * 10 + 2 = 12
            # 12 * 10 + 1 = 121
            rev_num = rev_num * 10 + digit

            # Remove the last digit from x.
            # Example: 121 // 10 = 12
            x //= 10

        # Compare the original number with the reversed number.
        # Reversed → True, different → False
        return org == rev_num