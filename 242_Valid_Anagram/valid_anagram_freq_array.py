class Solution:  # Create a class named Solution
    def isAnagram(self, s: str, t: str) -> bool:  # Create a method that takes two strings and returns True/False
        
        if len(s) != len(t):  # Check if both strings have different lengths
            return False  # Different lengths means they cannot be anagrams

        freq = [0] * 26  # Create an array of 26 zeros, one counter for each letter a-z

        for char in s:  # Go through each character in the first string
            freq[ord(char) - ord('a')] += 1  # Find the character's index and increase its count

        for char in t:  # Go through each character in the second string
            freq[ord(char) - ord('a')] -= 1  # Find the character's index and decrease its count

        for count in freq:  # Check every character count in the frequency array
            if count != 0:  # If any character count is not zero
                return False  # The character frequencies are different, so not an anagram

        return True  # All character counts are zero, so the strings are anagrams