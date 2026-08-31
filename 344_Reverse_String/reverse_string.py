class Solution:
    def reverseString(self, s: List[str]) -> None:
        # Start l at the first character (index 0)
        # Start r at the last character (last index)
        l, r = 0, len(s) - 1

        # Keep swapping while l is before r
        while l < r:

            # Swap the characters at the left and right positions
            s[l], s[r] = s[r], s[l]

            # Move l one position toward the middle from left (+1)
            l += 1

            # Move r one position toward the middle from right (-1)
            r -= 1