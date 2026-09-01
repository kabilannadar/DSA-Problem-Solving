class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create an empty set to remember numbers we have already seen
        h = set()

        # Go through each number in the list one by one
        for i in nums:

            # If this number is already in the set,
            # we have seen it before → duplicate found
            if i in h:
                return True

            # If we haven't seen this number,
            # add it to the set so we can check it later
            else:
                h.add(i)

        # Finished checking all numbers and found no duplicate
        return False