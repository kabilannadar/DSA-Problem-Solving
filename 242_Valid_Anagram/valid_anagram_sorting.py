class Solution:  
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # Check whether the both strings have different lengths.
            return False # Different lengths mean they cannot be anagrams.

        if sorted(s) == sorted(t): # Sort both strings and compare them.
            return True # If sorted strings are equal mean they are anagrams.

        return False # Strings are not anagrams.