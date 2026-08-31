class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Store each number together with its original index.
        # Example: [2, 6, 5] → [(2, 0), (6, 1), (5, 2)]
        nums_with_index = [(num, i) for i, num in enumerate(nums)]

        # Sort the tuples using the number (the first item in each tuple).
        # The original indexes stay attached to their numbers.
        # Example: [(2, 0), (6, 1), (5, 2)]
        #       → [(2, 0), (5, 2), (6, 1)]
        nums_with_index.sort(key=lambda x: x[0])

        # Put one pointer at the beginning and one at the end.
        L, R = 0, len(nums) - 1

        # Keep checking while the two pointers have not met.
        while L < R:

            # [0] gives the value from each tuple.
            # Add the values at the left and right pointers.
            current_sum = nums_with_index[L][0] + nums_with_index[R][0]

            # If their sum is the target, we found the pair.
            if current_sum == target:

                # [1] gives the original index from each tuple.
                # Return the original indexes, not indexes of the sorted positions.
                return [nums_with_index[L][1], nums_with_index[R][1]]

            # If the sum is too small, move L right.
            # Because the list is sorted, this gives us a bigger number.
            elif current_sum < target:
                L += 1

            # If the sum is too large, move R left.
            # Because the list is sorted, this gives us a smaller number.
            else:
                R -= 1

        # We checked every possible pair and found no answer.
        return [-1, -1]