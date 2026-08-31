# Two Sum — Sorting + Two Pointers

## Question

Given an array of numbers and a target, find two numbers whose sum equals the target and return their **original indexes**.

Example:

```python
nums = [2, 6, 5, 8, 11]
target = 14
```

Result:

```text
6 + 8 = 14
→ [1, 3]
```

---

# Flow

```text
Create (value, original_index) pairs
              ↓
        Sort by value
              ↓
       L → beginning
       R → end
              ↓
        Add L + R
              ↓
     ┌────────┼────────┐
     ↓        ↓        ↓
  Equal    Smaller   Larger
     ↓        ↓        ↓
  Answer     L++       R--
```

Repeat until the pair is found or `L` and `R` meet.

---

# Steps

## 1. Create the tuple list

We need to sort the numbers, but the answer must contain the **original indexes**.

So keep each number together with its original index:

```python
nums_with_index = [(num, i) for i, num in enumerate(nums)]
```

For:

```text
[2, 6, 5, 8, 11]
```

we get:

```text
[(2,0), (6,1), (5,2), (8,3), (11,4)]
```

Each tuple is:

```text
(value, original_index)
```

---

## 2. Sort the tuple list

```python
nums_with_index.sort(key=lambda x: x[0])
```

`x[0]` means the **value** in the tuple.

So:

```text
[(2,0), (6,1), (5,2), (8,3), (11,4)]
```

becomes:

```text
[(2,0), (5,2), (6,1), (8,3), (11,4)]
```

The original indexes stay attached to their numbers.

---

## 3. Set the two pointers

```python
L, R = 0, len(nums) - 1
```

`L` starts at the first item.

`R` starts at the last item.

```text
[(2,0), (5,2), (6,1), (8,3), (11,4)]
  ↑                                  ↑
  L                                  R
```

---

## 4. Add the two values

```python
current_sum = nums_with_index[L][0] + nums_with_index[R][0]
```

`[0]` means:

> Get the value from the tuple.

Example:

```text
L → (2,0)
R → (11,4)

2 + 11 = 13
```

---

## 5. Compare the sum with the target

### If the sum equals the target

```python
if current_sum == target:
```

We found the pair.

Now use `[1]` because `[1]` gives the **original index**:

```python
return [nums_with_index[L][1], nums_with_index[R][1]]
```

For:

```text
(6,1)
(8,3)
```

we return:

```text
[1,3]
```

---

### If the sum is smaller than the target

```python
elif current_sum < target:
    L += 1
```

Move `L` to the right.

Because the list is sorted, we get a bigger value.

Example:

```text
2 + 11 = 13
13 < 14
```

Move `L`:

```text
5 + 11 = 16
```

---

### If the sum is larger than the target

```python
else:
    R -= 1
```

Move `R` to the left.

Because the list is sorted, we get a smaller value.

---

# Full Example

```text
Original:
[2, 6, 5, 8, 11]

Target:
14
```

### Create tuples

```text
[(2,0), (6,1), (5,2), (8,3), (11,4)]
```

### Sort

```text
[(2,0), (5,2), (6,1), (8,3), (11,4)]
```

### Move the pointers

```text
2 + 11 = 13
→ smaller than 14
→ L moves right

5 + 11 = 16
→ larger than 14
→ R moves left

5 + 8 = 13
→ smaller than 14
→ L moves right

6 + 8 = 14
→ found
```

Original indexes:

```text
6 → 1
8 → 3
```

Answer:

```text
[1, 3]
```

---

# Tuple `[0]` and `[1]`

Every item has this structure:

```text
(value, original_index)
```

Example:

```text
(6, 1)
 ↑  ↑
[0] [1]
```

Therefore:

```python
nums_with_index[L][0]
```

means:

```text
Get the value → 6
```

and:

```python
nums_with_index[L][1]
```

means:

```text
Get the original index → 1
```

---

# Why do we keep the original index?

Sorting changes the positions.

Before sorting:

```text
index:  0  1  2  3  4
value:  2  6  5  8 11
```

After sorting:

```text
value:  2  5  6  8 11
```

The position of `6` changed.

But the answer still needs its **original index**, which was `1`.

That's why we keep:

```text
(6, 1)
```

instead of just:

```text
6
```

---

# Why is this better than Brute Force?

## Brute Force

Try every possible pair.

```text
Time  → O(n²)
Space → O(1)
```

## Sorting + Two Pointers

Sort first, then use `L` and `R`.

```text
Time  → O(n log n)
Space → O(n)
```

We use extra space to keep each value together with its original index.

---

# Is This Better Than Hash Maps Too?

It actually **isn't better than the Hash Map approach** for the normal Two Sum problem.

It is better than the **brute-force** approach, but Hash Map is faster.

## Compare Them

| Approach               |           Time |  Space |
| ---------------------- | -------------: | -----: |
| Brute Force            |        `O(n²)` | `O(1)` |
| Sorting + Two Pointers |   `O(n log n)` | `O(n)` |
| Hash Map               | `O(n)` average | `O(n)` |

## Why Hash Map Is Faster

Hash Map:

```text
Go through the array once
↓
Remember each number
↓
Quickly check whether the required number exists
```

So roughly:

```text
n items → n checks
```

## Sorting + Two Pointers

You first have to:

```text
Create tuples
↓
Sort them
↓
Move L and R
```

The **sorting alone** costs:

```text
O(n log n)
```

So it cannot beat the Hash Map's average `O(n)` time for standard Two Sum.

## Then Why Learn Sorting + Two Pointers?

Because it teaches a **very important pattern**:

```text
Sort
↓
Left + Right
↓
Too small → L++
Too large → R--
```

That pattern is extremely useful for problems like:

- **Two Sum II**
- **3Sum**
- **Container With Most Water**
- **Trapping Rain Water**

Also, sometimes the problem's constraints make sorting preferable, or you want to avoid hash-table lookup.

## The Main Idea

```text
Brute Force
    ↓
Sorting + Two Pointers
    ↓
Hash Map
```

For the standard Two Sum problem:

```text
Brute Force            → O(n²)
Sorting + Two Pointers → O(n log n)
Hash Map               → O(n) average
```

So **Sorting + Two Pointers is an improvement over brute force, but Hash Map is the better approach for standard Two Sum.**

# Quick Revision

```text
1. Create (value, original_index)
2. Sort by value
3. L = first item
4. R = last item
5. Add the two values
6. Equal   → return original indexes
7. Smaller → L++
8. Larger  → R--
```

### Remember

```text
tuple = (value, original_index)

[0] → value
[1] → original index

L moves right  → bigger value
R moves left   → smaller value
```

> **Sort the values so two pointers can work, but keep the original indexes attached to the values.**
