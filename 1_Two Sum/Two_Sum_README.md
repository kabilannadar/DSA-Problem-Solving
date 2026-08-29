# Two Sum — Brute Force

## Flow

`i` picks the first number.

`j` picks the second/next number.

```text
        i      j
        ↓      ↓
[2,  6,  5,  8,  11]
```

The nested loops check every possible pair:

```text
2 + 6
2 + 5
2 + 8
2 + 11

6 + 5
6 + 8  ← 14 ✅
```

When the pair adds up to the target, return their indexes.

```text
6 → index 1
8 → index 3

→ [1, 3]
```

## The Two Possibilities

### Possibility 1: A valid pair is found

```python
if nums[i] + nums[j] == target:
    return [i, j]
```

The two numbers add up to the target, so the function immediately returns their indexes.

### Possibility 2: No valid pair is found

The loops finish checking every possible pair.

```python
return [-1, -1]
```

This means no pair was found.

## Why does `j` start at `i + 1`?

We never use the same element at the same index twice.

We never check the same pair of indexes twice.

Every unique pair of indexes is checked once.

For example:

```text
i = 0 → j = 1, 2, 3, 4
i = 1 → j = 2, 3, 4
i = 2 → j = 3, 4
i = 3 → j = 4
i = 4 → nothing
```

This avoids checking pairs like:

```text
(0, 1)
(1, 0)
```

because they are the same two indexes.

## Code

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return [-1, -1]
```

## Complexity

- **Time:** `O(n²)` — in the worst case, we check every unique pair.
- **Space:** `O(1)` — we only use the two loop variables.
