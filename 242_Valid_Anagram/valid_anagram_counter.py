from collections import Counter 
class Solution:  
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):  # Check whether the two strings have different lengths.
            return False  # Different lengths mean they cannot be anagrams.

        s_dict = Counter(s)  # Count the frequency of every character in the s string.
        t_dict = Counter(t)  # Count the frequency of every character in the t string.

        return s_dict == t_dict  # Compare both frequency dictionaries; equal counts mean they are anagrams.