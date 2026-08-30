class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # This is an empty dictionary
        # Think of it as a notebook
        # eg. "I saw this number at this index"
        s = {}

        # Go through nums one item at a time, and give me both the item's index and its value.
        for i, num in enumerate(nums):
            # What number do I need to add (req) to my current number (num) to reach the target
            req = target - num

            if req in s:
                #If number is found in our notebook
                #Return the index of the number we found earlier, and the index of the current number.
                return [s[req], i]

            #Remember that I found a number at an index, we need to write it in our notebook
            s[num] = i

        # I checked everything, but I couldn't find a pair.
        return [-1, -1]
