# Valid Palindrome

## Problem

Given a string `s`, determine whether it is a palindrome after:

- Converting uppercase letters to lowercase.
- Ignoring non-alphanumeric characters such as spaces and punctuation.

Return `True` if it is a palindrome, otherwise return `False`.

---

## Core Idea

Use **two pointers**:

```text
L →                         ← R
```

- `L` starts at the beginning.
- `R` starts at the end.
- Skip characters that are not letters or numbers.
- Compare the characters at `L` and `R`.
- If they match, move both pointers toward each other.
- If they do not match, return `False`.
- If the pointers meet without finding a mismatch, return `True`.

---

## Code

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:

        # L starts at the beginning and R starts at the end
        L, R = 0, len(s) - 1

        # Keep moving both pointers toward each other until they meet
        while L < R:

            # If the left character is not a letter or number,
            # skip it by moving L to the right
            if not s[L].isalnum():
                L += 1
                continue

            # If the right character is not a letter or number,
            # skip it by moving R to the left
            if not s[R].isalnum():
                R -= 1
                continue

            # Compare both characters after converting them to lowercase
            # If they are different, the string is not a palindrome
            if s[L].lower() != s[R].lower():
                return False

            # Move L one position towards R
            L += 1

            # Move R one position towards L
            R -= 1

        # All valid characters matched, so it is a palindrome
        return True
```

---

# Flow

```text
Start
  ↓
Set L = 0 and R = last index
  ↓
Is L < R?
  ↓
 YES
  ↓
Is s[L] alphanumeric?
  ├── NO → L += 1 → go back to while loop
  └── YES
          ↓
     Is s[R] alphanumeric?
          ├── NO → R -= 1 → go back to while loop
          └── YES
                  ↓
          Compare s[L] and s[R]
                  ↓
          Are they different?
          ├── YES → return False
          └── NO
                ↓
        L += 1 and R -= 1
                ↓
          Go back to while loop
                ↓
        L >= R → return True
```

---

# Step-by-Step

## Step 1 — Set the pointers

```python
L, R = 0, len(s) - 1
```

For:

```text
s = "A man, a plan, a canal: Panama"
```

The pointers start here:

```text
L → A man, a plan, a canal: Panama ← R
```

---

## Step 2 — Check the left character

```python
if not s[L].isalnum():
    L += 1
    continue
```

`isalnum()` checks whether the character is a letter or number.

Examples:

```text
"A".isalnum() → True
"5".isalnum() → True
",".isalnum() → False
" ".isalnum() → False
```

If the character is invalid, move `L` to the right.

---

## Step 3 — Check the right character

```python
if not s[R].isalnum():
    R -= 1
    continue
```

If the right character is a space or punctuation, move `R` to the left.

---

## Step 4 — Compare valid characters

```python
if s[L].lower() != s[R].lower():
    return False
```

`lower()` makes the comparison case-insensitive.

For example:

```text
"A".lower() == "a".lower()

"a" == "a"
```

If the characters are different, the string cannot be a palindrome.

---

## Step 5 — Move the pointers

If the characters match:

```python
L += 1
R -= 1
```

Meaning:

```text
# Move L one position towards R
L += 1

# Move R one position towards L
R -= 1
```

Then we repeat the process.

---

# Example 1 — Palindrome

```text
s = "A man, a plan, a canal: Panama"
```

Ignore spaces and punctuation:

```text
AmanaplanacanalPanama
```

Compare from both sides:

```text
A ↔ a  ✓
m ↔ m  ✓
a ↔ a  ✓
n ↔ n  ✓
a ↔ a  ✓
p ↔ P  ✓
...
```

Every valid character matches.

```text
Answer = True
```

---

# Example 2 — Not a Palindrome

```text
s = "race a car"
```

Compare:

```text
r ↔ r  ✓
a ↔ a  ✓
c ↔ c  ✓
e ↔ a  ✗
```

`e` and `a` are different.

Immediately:

```python
return False
```

```text
Answer = False
```

---

# Example 3 — Ignoring Symbols

```text
s = ".,"
```

Both characters are non-alphanumeric.

```text
. → skip
, → skip
```

There are no valid characters left to compare.

Therefore:

```text
Answer = True
```

---

# Example 4 — Numbers

```text
s = "12321"
```

Compare:

```text
1 ↔ 1  ✓
2 ↔ 2  ✓
3
```

The pointers meet at `3`.

```text
Answer = True
```

---

# Why Use Two Pointers?

A simple alternative would be:

1. Remove all spaces and symbols.
2. Convert everything to lowercase.
3. Reverse the string.
4. Compare both strings.

But that requires creating another string.

The two-pointer approach checks the original string directly.

```text
Left →                 ← Right
       \             /
        \           /
         \         /
          \       /
           \     /
            Meet
```

This makes the solution **in-place with constant extra space**.

---

# Important Python Methods

## `isalnum()`

Checks whether a character is a letter or number.

```python
"a".isalnum()   # True
"7".isalnum()   # True
"#".isalnum()   # False
" ".isalnum()   # False
```

## `lower()`

Converts a character/string to lowercase.

```python
"A".lower()     # "a"
"Hello".lower() # "hello"
```

---

# Why `continue`?

Consider:

```python
if not s[L].isalnum():
    L += 1
    continue
```

`continue` means:

> Stop this iteration and immediately start the next iteration of the same loop.

We don't want to compare an invalid character.

Example:

```text
s = "a,b"
```

When `L` reaches `,`:

```text
, → invalid
L += 1
continue
```

The loop starts again with the next valid character.

---

# Questions to Ask Yourself

### 1. Why do we use `L < R`?

Because we only need to compare characters until the two pointers meet.

---

### 2. Why don't we compare the entire string?

Because a palindrome can be verified by comparing matching characters from the two ends.

---

### 3. Why use `isalnum()`?

Because spaces and punctuation should be ignored.

---

### 4. Why use `lower()`?

Because uppercase and lowercase letters should be treated as the same character.

---

### 5. Why return `False` immediately?

The moment one pair doesn't match, we know the entire string cannot be a palindrome.

---

### 6. Why use `continue`?

To skip the current invalid character and restart the loop with the updated pointer.

---

### 7. Why move both pointers after a successful comparison?

Because that pair has already been checked. We now need to compare the next pair.

---

### 8. What happens if the string is empty?

```text
s = ""
```

There are no characters that can contradict a palindrome.

```text
Answer = True
```

---

### 9. What happens with one character?

```text
s = "a"
```

`L` and `R` point to the same character, so:

```python
L < R
```

is `False`.

The loop doesn't run and the function returns:

```text
True
```

---

# Complexity

### Time: `O(n)`

Each pointer moves only from the outside toward the center.

We never move a pointer backward.

### Space: `O(1)`

We do not create another string or array.

Only two pointer variables are used:

```python
L
R
```

---

# Pattern to Remember

This problem teaches the **Two Pointers** pattern.

When you see a problem involving:

- Comparing both ends of a string/array
- Reversing something
- Checking a palindrome
- Finding pairs
- Moving inward from both sides

Think:

```text
L →                  ← R
```

Then ask:

> **Can I solve this by moving two pointers toward each other?**

---

## One-Line Summary

> Start from both ends, skip invalid characters, compare lowercase values, and move the pointers toward each other.
