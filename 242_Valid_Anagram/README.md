# Valid Anagram — All Approaches

## Problem

Given two strings `s` and `t`, determine whether `t` is an anagram of `s`.

Two strings are anagrams when they contain the **same characters with the same frequencies**, regardless of order.

### Example

```text
s = "anagram"
t = "nagaram"

Result → True
```

```text
s = "rat"
t = "car"

Result → False
```

---

# Big Picture

There are three common approaches:

```text
                    VALID ANAGRAM
                          ↓
              Do both strings have
                 the same letters?
                          ↓
        ┌─────────────────┼─────────────────┐
        ↓                 ↓                 ↓
     Counter           Sorting          Frequency Array
        ↓                 ↓                 ↓
   Count chars       Sort chars       Count using 26
        ↓                 ↓                 ↓
    Compare           Compare          Add / subtract
    counts             lists              counts
        ↓                 ↓                 ↓
      O(n)            O(n log n)           O(n)
```

---

# Approach 1 — Counter

## Code

```python
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = Counter(s)
        t_dict = Counter(t)

        return s_dict == t_dict
```

## Flow

```text
s, t
 ↓
Check lengths
 ↓
Different?
 ├── YES → False
 └── NO
      ↓
Count characters in s
      ↓
Count characters in t
      ↓
Compare both counts
      ↓
Same?
 ├── YES → True
 └── NO  → False
```

## Example

```text
s = "aabbc"
t = "bcbaa"
```

Counter for `s`:

```text
a → 2
b → 2
c → 1
```

Counter for `t`:

```text
a → 2
b → 2
c → 1
```

```text
Same counts
    ↓
True
```

## Why Counter works

An anagram does not care about position.

It only cares about:

```text
character → how many times it appears
```

---

# Approach 2 — Sorting

## Code

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
```

## Flow

```text
s = "cab"
t = "abc"

     ↓

sorted(s)
     ↓
['a', 'b', 'c']

sorted(t)
     ↓
['a', 'b', 'c']

     ↓

Compare
     ↓
True
```

## Another example

```text
s = "rat"
t = "car"

sorted(s)
 ↓
['a', 'r', 't']

sorted(t)
 ↓
['a', 'c', 'r']

 ↓

Different
 ↓
False
```

---

# Question — How can a string be sorted if strings are immutable?

This is an important distinction.

Python strings are immutable:

```python
s = "cab"
```

You cannot change the characters inside `s`.

For example, you cannot do:

```python
s[0] = "a"
```

That would give an error.

But:

```python
sorted(s)
```

does **not** modify `s`.

Instead, Python creates a new sorted list.

```text
Original string

s = "cab"
     ↓
   unchanged
     ↓
   "cab"


sorted(s)
     ↓
creates a NEW object
     ↓
['a', 'b', 'c']
```

So:

```python
sorted(s)
```

means:

```text
Take the characters from s
        ↓
Sort them
        ↓
Return a NEW list
```

It does NOT mean:

```text
Change s itself
```

## Important difference

```python
s = "cab"

sorted(s)
```

Result:

```text
['a', 'b', 'c']
```

But:

```python
print(s)
```

still gives:

```text
cab
```

The original string was never changed.

---

# Why `sorted()` returns a list

A Python string is immutable, so Python does not sort the string in place.

`sorted()` is a general-purpose function that returns a new sorted list.

```text
"cab"
 ↓
characters
 ↓
['c', 'a', 'b']
 ↓
sort
 ↓
['a', 'b', 'c']
```

If you really wanted a sorted string, you could do:

```python
''.join(sorted(s))
```

Flow:

```text
"cab"
 ↓
sorted()
 ↓
['a', 'b', 'c']
 ↓
''.join()
 ↓
"abc"
```

But for the anagram problem, we don't need to convert it back to a string.

We only need to compare:

```python
sorted(s) == sorted(t)
```

---

# Approach 3 — Frequency Array

## Code

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = [0] * 26

        for char in s:
            freq[ord(char) - ord('a')] += 1

        for char in t:
            freq[ord(char) - ord('a')] -= 1

        for count in freq:
            if count != 0:
                return False

        return True
```

## Important Assumption

This version assumes the strings contain lowercase English letters:

```text
a → z
```

There are 26 possible characters.

---

# What is `freq`?

This is the most important concept in this approach.

```python
freq = [0] * 26
```

creates:

```text
index:  0  1  2  3  4  5  ... 25
        ↓  ↓  ↓  ↓  ↓  ↓       ↓
letter: a  b  c  d  e  f  ...  z
count:  0  0  0  0  0  0  ...  0
```

Think of `freq` as a **shared scoreboard**.

It is NOT part of either string.

```text
s ──────────────┐
                ↓
             freq[]
                ↑
t ──────────────┘
```

Both strings use the **same `freq` array**.

---

# Your Question

> But if order is `abc` and `cab`, its `0, +1, +2` and `-2, 0, -1` for the third approach?

This is the key misunderstanding.

The numbers in `freq` are **NOT positions in the string**.

They are counts for specific letters.

You are thinking:

```text
abc

a → 0
b → +1
c → +2
```

But that is NOT what happens.

Instead:

```text
a → index 0
b → index 1
c → index 2
```

These numbers are **array indexes**, not counts.

The array itself starts as:

```text
freq = [0, 0, 0, 0, ...]
         ↑  ↑  ↑
         a  b  c
```

---

# Let's Walk Through `abc`

Suppose:

```text
s = "abc"
```

Start:

```text
freq

index:   0  1  2
letter:  a  b  c
count:   0  0  0
```

## First character: `a`

```python
freq[ord('a') - ord('a')] += 1
```

Calculate the index:

```text
ord('a') - ord('a')
       ↓
      97 - 97
       ↓
       0
```

So:

```python
freq[0] += 1
```

Now:

```text
index:   0  1  2
letter:  a  b  c
count:   1  0  0
```

---

## Second character: `b`

```text
ord('b') - ord('a')
       ↓
      98 - 97
       ↓
       1
```

So:

```python
freq[1] += 1
```

Now:

```text
index:   0  1  2
letter:  a  b  c
count:   1  1  0
```

---

## Third character: `c`

```text
ord('c') - ord('a')
       ↓
      99 - 97
       ↓
       2
```

So:

```python
freq[2] += 1
```

Now:

```text
index:   0  1  2
letter:  a  b  c
count:   1  1  1
```

So `abc` gives:

```text
[1, 1, 1]
```

NOT:

```text
[0, 1, 2]
```

---

# Now String 2: `cab`

Here is the important part:

**String 2 does not "know" what was in string 1.**

It doesn't need to.

Both strings use the SAME `freq` array.

Before processing `t`:

```text
freq

letter:  a  b  c
count:   1  1  1
```

Now:

```text
t = "cab"
```

---

## `c`

`c` maps to index `2`.

```python
freq[2] -= 1
```

```text
before:
[1, 1, 1]

after:
[1, 1, 0]
```

---

## `a`

`a` maps to index `0`.

```python
freq[0] -= 1
```

```text
before:
[1, 1, 0]

after:
[0, 1, 0]
```

---

## `b`

`b` maps to index `1`.

```python
freq[1] -= 1
```

```text
before:
[0, 1, 0]

after:
[0, 0, 0]
```

---

# This Answers Your Main Question

> How does string 2 know what was in string 1 to make it 0?

It doesn't know.

**`freq` remembers it.**

That's the entire trick.

```text
             STRING 1
                abc
                 ↓
          ADD each character
                 ↓
        ┌─────────────────┐
        │ freq = [1,1,1]  │
        └─────────────────┘
                 ↑
                 │
          STRING 2
                cab
                 ↓
        SUBTRACT each character
                 ↓
        ┌─────────────────┐
        │ freq = [0,0,0]  │
        └─────────────────┘
```

So:

```text
String 1 → +1 for every character
String 2 → -1 for every character
                       ↓
                everything cancels
                       ↓
                    [0,0,0]
                       ↓
                     True
```

---

# Why Does Order Not Matter?

Take:

```text
s = "abc"
t = "cab"
```

First string:

```text
a → +1
b → +1
c → +1

freq = [1,1,1]
```

Second string:

```text
c → -1
a → -1
b → -1

freq = [0,0,0]
```

It doesn't matter that `c` came first in `t`.

`c` always goes to:

```text
freq[2]
```

`a` always goes to:

```text
freq[0]
```

`b` always goes to:

```text
freq[1]
```

So the same letters always affect the same positions.

---

# Example Where It Fails

```text
s = "aab"
t = "abb"
```

First:

```text
a → +1
a → +1
b → +1

freq = [2,1,0]
```

Second:

```text
a → -1
b → -1
b → -1
```

Result:

```text
freq = [1,-1,0]
```

Now check:

```python
for count in freq:
    if count != 0:
        return False
```

We have:

```text
[1,-1,0]
 ↑
not zero
 ↓
False
```

Therefore:

```text
"aab" and "abb"
       ↓
Not anagrams
       ↓
False
```

---

# Breaking Down `ord()`

This line looks scary:

```python
freq[ord(char) - ord('a')] += 1
```

Mentally expand it:

```python
index = ord(char) - ord('a')
freq[index] += 1
```

For `c`:

```text
char = 'c'

ord('c')
   ↓
99

ord('a')
   ↓
97

99 - 97
   ↓
2

freq[2]
   ↓
the counter for c
```

So:

```text
character
    ↓
ord()
    ↓
number
    ↓
subtract ord('a')
    ↓
array index
    ↓
update that character's counter
```

---

# All Three Approaches Compared

| Approach        | Main Idea                     |       Time | Extra Space |
| --------------- | ----------------------------- | ---------: | ----------: |
| Counter         | Count characters and compare  |       O(n) |        O(k) |
| Sorting         | Sort both and compare         | O(n log n) |        O(n) |
| Frequency Array | Add/subtract character counts |       O(n) |      O(1)\* |

`k` = number of distinct characters.

`*` The frequency-array approach is O(1) when the alphabet is fixed at 26 lowercase letters.

---

# Which One Should You Learn?

### Counter

Best for:

```text
Easy to understand
↓
Short code
↓
Python-specific solution
```

```python
Counter(s) == Counter(t)
```

Very practical.

---

### Sorting

Best for understanding the basic idea:

```text
Different order
      ↓
Sort
      ↓
Same order
      ↓
Compare
```

It's simple, but slower than the linear approaches.

---

### Frequency Array

Best for understanding:

```text
Arrays
↓
Indexes
↓
Character mapping
↓
Counting
↓
Time/space optimization
```

This is the most educational approach if you want to understand what is happening **under the hood** rather than relying on `Counter`.

---

# Final Mental Model

## Counter

```text
s → count
t → count
    ↓
 compare
```

## Sorting

```text
s → sort
t → sort
    ↓
 compare
```

## Frequency Array

```text
s → ADD → freq
              ↓
t → SUBTRACT → freq
              ↓
        all zero?
          ↓
      YES → True
      NO  → False
```

The most important thing to remember from the third approach:

> **`freq` is the memory. String 1 writes its character counts into it. String 2 removes those counts. String 2 does not know string 1 — the shared `freq` array remembers.**
