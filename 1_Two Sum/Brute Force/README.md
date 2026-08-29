# Two Sum - Brute Force Approach

## Understand the Flow

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

## The Three Possibilities

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

### Possibility 3: Multiple valid pairs exist

The algorithm returns the first valid pair it encounters.

For the example `nums = [1, 2, 3, 4, 5], target = 6`, it checks:

1 + 2
1 + 3
1 + 4
1 + 5 ← 6 ✅

So it immediately returns:

[0, 4]

It does not continue looking for 2 + 4.

Note: The original LeetCode Two Sum problem guarantees that there is exactly one valid answer. The third possibility is useful for understanding how the loop behaves when multiple valid pairs exist, but it does not satisfy LeetCode's original guarantee.

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

## Complexity

- **Time:** `O(n²)` - The bigger the list gets, the more pairs we have to try.
- **Space:** `O(1)` - We don't make any new list to store more things. We only use `i` and `j` the two loop variables.
