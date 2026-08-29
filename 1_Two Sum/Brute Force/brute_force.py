class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # eg. list = [1, 2, 4], target = 6
        # i represents the index of the first number in the pair.
        for i in range(len(nums)):

            # j represents the index of the second number.
            # It starts at i + 1 because:
            # nums[i] + nums[i] would use the same element twice,
            # and pairs like (0,1) and (1,0) are the same pair.
            for j in range(i + 1, len(nums)):

                # nums[i] and nums[j] are the two values we're testing.
                # If their sum equals target, we found the required pair.
                if nums[i] + nums[j] == target:

                    # The problem asks for indexes, not the values themselves.
                    return [i, j]

        # Reaching here means every possible pair was checked
        # and none of them produced the target.
        return [-1, -1]