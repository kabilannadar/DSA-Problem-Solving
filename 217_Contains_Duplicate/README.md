# Contains Duplicate

## Problem

Given an integer array `nums`, return `True` if any value appears at least twice in the array. Otherwise, return `False`.

## Solution

```python
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
```

## How It Works

We use a **set** to store numbers that we have already encountered.

For every number:

1. Check if the number is already in the set.
2. If it is already there → a duplicate exists → return `True`.
3. If it is not there → add it to the set.
4. If we finish the entire list without finding a duplicate → return `False`.

## Example

For:

```text
nums = [1, 2, 3, 2]
```

Step by step:

```text
h = {}

1 → not in h → add 1 → {1}
2 → not in h → add 2 → {1, 2}
3 → not in h → add 3 → {1, 2, 3}
2 → already in h → True
```

So the answer is:

```text
True
```

## Why Use a Set?

A Python `set` is useful because checking whether a value exists in it is **O(1)** on average.

This lets us check every number efficiently without comparing every number with every other number.

## Complexity

- **Time:** `O(n)` — we go through the array once.
- **Space:** `O(n)` — in the worst case, we store every number in the set.

## Core Idea

> Keep every number you've seen in a set. If you see the same number again, a duplicate exists.
