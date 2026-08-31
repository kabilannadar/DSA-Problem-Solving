# Reverse String

## Problem

Given an array of characters `s`, reverse the array **in-place**.

## How It Works

We use **two pointers**:

- `l` → starts from the left
- `r` → starts from the right

We swap the characters at both pointers, then move them toward the center.

### Example

```text
s = ["h", "e", "l", "l", "o"]

l → h    e    l    l    o ← r
```

**Step 1:** Swap `h` and `o`

```text
o    e    l    l    h
```

Move `l` right and `r` left:

```text
o    e    l    l    h
     l         r
```

**Step 2:** Swap `e` and `l`

```text
o    l    l    e    h
```

Move the pointers again. They meet in the middle, so we stop.

Final result:

```text
["o", "l", "l", "e", "h"]
```

## Why `l < r`?

We only need to swap pairs until the two pointers meet.

The middle character does not need to be swapped with itself.

## Key Idea

> Swap the first and last characters, then move both pointers toward the center.

## Complexity

- **Time:** `O(n)` — we go through half of the array, which is still linear.
- **Space:** `O(1)` — no extra array is created.

## Important Concept: In-Place

The original array is modified directly instead of creating a new array.

Python allows us to swap two values in one line:

```python
s[l], s[r] = s[r], s[l]
```

is same as:

```python
s[l] = s[r]
s[r] = s[l]
```
