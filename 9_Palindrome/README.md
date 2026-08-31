# Palindrome Number

## Question

Given an integer `x`, return `True` if it reads the same forward and backward.

Examples:

```text
121 → True
121 → True
-121 → False
```

---

## Flow

```text
Original number
      ↓
Save the original number
      ↓
Take the last digit
      ↓
Add it to the reversed number
      ↓
Remove the last digit
      ↓
Repeat until x becomes 0
      ↓
Compare original and reversed
```

---

## Steps

### 1. Check for a negative number

```python
if x < 0:
    return False
```

A negative number cannot be a palindrome.

---

### 2. Save the original number

```python
org = x
```

We save `x` because `x` will change inside the loop.

---

### 3. Start the reversed number

```python
rev_num = 0
```

We start with `0` and build the reversed number one digit at a time.

---

### 4. Take the last digit

```python
digit = x % 10
```

`% 10` gives the last digit.

For example:

```text
121 % 10 = 1
```

---

### 5. Add the digit to the reversed number

```python
rev_num = rev_num * 10 + digit
```

For `121`:

```text
First:
0 * 10 + 1 = 1

Second:
1 * 10 + 2 = 12

Third:
12 * 10 + 1 = 121
```

So:

```text
rev_num: 0 → 1 → 12 → 121
```

---

### 6. Remove the last digit from `x`

```python
x //= 10
```

`// 10` removes the last digit.

```text
121 // 10 = 12
12  // 10 = 1
1   // 10 = 0
```

So each loop does:

```text
Take → Add → Remove → Repeat
```

---

### 7. Compare the original and reversed numbers

```python
return org == rev_num
```

If they are the same:

```text
121 == 121
→ True
```

If they are different:

```text
121 == 121
→ True
```

`==` simply compares the two values.

---

## Complete Code

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Negative numbers are not palindromes.
        if x < 0:
            return False

        # Save the original number because x changes in the loop.
        org = x

        # Start the reversed number at 0.
        rev_num = 0

        # Keep processing digits until x becomes 0.
        while x > 0:

            # Take the last digit from x.
            # Example: 121 % 10 = 1
            digit = x % 10

            # Add the digit to the end of rev_num.
            # Example:
            # 0 * 10 + 3 = 3
            # 3 * 10 + 2 = 32
            # 32 * 10 + 1 = 321
            rev_num = rev_num * 10 + digit

            # Remove the last digit from x.
            # Example: 121 // 10 = 12
            x //= 10

        # Compare the original number with the reversed number.
        return org == rev_num
```

---

## Quick Revision

```text
x % 10
→ take the last digit

rev_num * 10 + digit
→ add the digit to the reversed number

x // 10
→ remove the last digit

org == rev_num
→ check if the number is a palindrome
```

### Remember

> **Take → Add → Remove → Repeat → Compare**

---

## Complexity

```text
Time  → O(log x)
Space → O(1)
```

The loop processes the digits of the number, and only a fixed number of variables are used.
