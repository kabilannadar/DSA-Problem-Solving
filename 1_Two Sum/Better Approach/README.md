# Two Sum — Brute Force to Hash Map

## Problem

Given a list of numbers and a `target`, find two different elements whose sum equals the target.

Exasle:

```python
nums = [2, 6, 5, 8, 11]
target = 14
```

Answer:

```text
6 + 8 = 14
→ [1, 3]
```

`6` is at index `1` and `8` is at index `3`.

---

# 1. Brute Force Approach

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return [-1, -1]
```

## How the loops work

`i` picks the first number.

`j` picks the second/next number.

```text
        i      j
        ↓      ↓
[2,  6,  5,  8,  11]
```

For:

```text
i = 0
```

`nums[i]` is `2`.

The inner loop starts at:

```text
j = i + 1
  = 1
```

So it checks:

```text
2 + 6
2 + 5
2 + 8
2 + 11
```

Then:

```text
i = 1
```

`nums[i]` is `6`.

Now `j` starts at `2`:

```text
6 + 5
6 + 8  ← 14
6 + 11
```

Then it continues with:

```text
i = 2 → j = 3, 4
i = 3 → j = 4
i = 4 → nothing
```

### Why does `j` start at `i + 1`?

Because:

```text
We never use the same element at the same index twice.
We never check the same pair of indexes twice.
Every unique pair of indexes is checked once.
```

For exasle:

```text
(0, 1)
```

and

```text
(1, 0)
```

are the same two elements, so checking both is unnecessary.

We also avoid:

```text
(1, 1)
```

which would use the same element twice.

---

# 2. What if there is more than one valid pair?

Yes, a general Two Sum problem can have more than one valid pair.

Exasle:

```python
nums = [1, 2, 3, 4, 5]
target = 6
```

There are two valid pairs:

```text
1 + 5 = 6 → [0, 4]

2 + 4 = 6 → [1, 3]
```

The brute-force code returns the **first valid pair it encounters**:

```text
1 + 2
1 + 3
1 + 4
1 + 5  ← found
```

So it returns:

```text
[0, 4]
```

It stops immediately because `return` ends the function.

The original LeetCode Two Sum problem guarantees exactly one valid answer, so the exasle above is useful for understanding the loop but does not satisfy that original guarantee.

---

# 3. Why is the brute-force approach slower?

The brute-force solution tries many pairs:

```text
2 + 6
2 + 5
2 + 8
2 + 11
6 + 5
6 + 8
...
```

As the list gets bigger, the number of pairs grows very quickly.

```text
Time → O(n²)
```

It does not need to create another growing data structure:

```text
Space → O(1)
```

### Sisle way to remember

```text
Time  → How much work?
Space → How much extra stuff?
```

The two loops affect the **time**, not the space.

---

# 4. Hash Map Approach

Instead of trying every pair, we keep a small dictionary (`s`) that remembers:

```text
number → index
```

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        s = {}

        for i, num in enumerate(nums):
            req = target - num

            if req in s:
                return [s[req], i]

            s[num] = i

        return [-1, -1]
```

---

# 5. What does `for i, num in enumerate(nums)` mean?

It means:

> For each number, give me **where it is** and **what it is**.

For:

```python
nums = [2, 6, 5, 8]
```

`enumerate(nums)` gives:

```text
(0, 2)
(1, 6)
(2, 5)
(3, 8)
```

So:

```text
i   → index
num → value
```

Exasle:

```text
i = 1
num = 6
```

### Isortant

`enumerate()` does **not** decide the dictionary key and value.

It only gives us:

```text
i = index
num = value
```

We decide how to store them.

---

# 6. What does `s[num] = i` mean?

This line means:

> Store the index `i` under the number `num`.

Exasle:

```text
num = 6
i = 1
```

So:

```python
s[num] = i
```

becomes:

```python
s[6] = 1
```

The dictionary now looks like:

```text
KEY → VALUE

6 → 1
```

So in this problem:

```text
key   = number
value = index
```

The dictionary is:

```text
number → index
```

---

# 7. Why isn't `i` the key?

`enumerate(nums)` gives:

```text
i = index
num = value
```

But we are free to choose how to build the dictionary.

We could write:

```python
s[i] = num
```

which would give:

```text
index → number
```

But Two Sum needs us to ask:

> "Have I already seen the number I need?"

So the **number needs to be the key**.

That's why we use:

```python
s[num] = i
```

---

# 8. What does `req = target - num` mean?

`req` means:

> The number we need to reach the target.

Exasle:

```text
target = 14
num = 8
```

Then:

```text
req = 14 - 8
    = 6
```

So we need to know:

> "Have I already seen `6`?"

---

# 9. What does `if req in s` mean?

It asks:

> Is the number we need already in our dictionary?

Exasle:

```text
req = 6
```

and:

```text
s = {
    2: 0,
    6: 1,
    5: 2
}
```

Then:

```python
if req in s:
```

is the same as:

```python
if 6 in s:
```

Answer:

```text
YES
```

---

# 10. What does `s[req]` mean?

Remember:

```text
s = number → index
```

So:

```python
s[6]
```

means:

> Get the index stored under the key `6`.

If:

```text
s[6] = 1
```

then:

```python
s[6]
```

gives:

```text
1
```

It is **not getting the number 6**.

It is getting the **value stored under key 6**, which is its index.

---

# 11. What does `[s[req], i]` mean?

It gives us the two indexes:

```text
index of the number we found earlier
+
index of the current number
```

Exasle:

```text
req = 6
s[6] = 1
i = 3
```

So:

```python
[s[req], i]
```

becomes:

```python
[1, 3]
```

For:

```python
nums = [2, 6, 5, 8, 11]
```

that means:

```text
6 → index 1
8 → index 3

6 + 8 = 14
```

---

# 12. What happens when `8` is found?

At this point:

```text
num = 8
i = 3
```

Calculate:

```text
req = 14 - 8
    = 6
```

`6` is already in `s`:

```text
6 → 1
```

So:

```python
return [s[req], i]
```

becomes:

```python
return [1, 3]
```

### Is `8` stored in `s`?

**No.**

Why?

Because:

```python
return [1, 3]
```

ends the function immediately.

Python never reaches:

```python
s[num] = i
```

for the `8`.

If `8` had not found a pair, then it would be stored:

```python
s[8] = 3
```

---

# 13. What does `return [-1, -1]` mean?

It means:

> We checked the whole list and did not find a valid pair.

Exasle:

```python
nums = [1, 2, 3]
target = 10
```

We need:

```text
1 → need 9
2 → need 8
3 → need 7
```

None exists.

The loop finishes, so:

```python
return [-1, -1]
```

is reached.

`-1` is used as a sisle "not found" signal because normal list indexes are:

```text
0, 1, 2, 3, ...
```

---

# 14. Why is the Hash Map approach better?

### Brute Force

```text
Try many pairs
```

```text
Time  → O(n²)
Space → O(1)
```

### Hash Map

```text
Remember numbers already seen
→ quickly check whether the needed number exists
```

```text
Time  → O(n)
Space → O(n)
```

The trade-off is:

> **Use more memory to save time.**

---

# 15. Coslete Mental Model

### Brute Force

```text
i → pick a number
j → try every number after it
```

### Hash Map

```text
i, num
  ↓
What number do I need?
  ↓
Check the notebook
  ↓
Found?
 ├── YES → return both indexes
 └── NO  → remember current number + index
```

### Dictionary

```text
s[num] = i

number → index
```

### Final lookup

```text
s[req] → index of the number we need
```

### Final answer

```text
[s[req], i] → the two indexes
```

### No answer

```text
[-1, -1] → no valid pair found
```
