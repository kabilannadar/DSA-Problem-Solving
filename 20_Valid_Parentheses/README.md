# Valid Parentheses

## Question

Given a string `s` containing `(`, `)`, `{`, `}`, `[` and `]`, determine whether the brackets are valid.

A string is valid when:

1. Every opening bracket has a matching closing bracket.
2. Brackets are closed in the correct order.
3. Every closing bracket has a matching opening bracket.

### Examples

| Input | Output |
|---|---|
| `"()"` | `True` |
| `"()[]{}"` | `True` |
| `"(]"` | `False` |
| `"([)]"` | `False` |
| `"{[]}"` | `True` |

---

## Approach

### Type of Approach

**Stack-based approach**

### Pattern

**Matching / Nested Brackets using Stack**

The main pattern is:

```text
Opening bracket -> PUSH
Closing bracket -> POP + COMPARE
End -> Stack must be empty
```

### Why Stack?

The last opening bracket must be the first bracket to close.

For example:

```text
({[]})
```

The brackets open in this order:

```text
(
{
[
```

They must close in reverse order:

```text
]
}
)
```

This follows **LIFO (Last In, First Out)**, which is exactly how a stack works.

---

## Flow

```text
Start
  |
Create closing -> opening bracket map
  |
Create empty stack
  |
Read each character
  |
Is it an opening bracket?
 |- Yes -> Push into stack
 |
 `- No -> Closing bracket
             |
        Is stack empty?
         |- Yes -> False
         |
         `- No
              |
           Pop stack
              |
        Does it match?
         |- No -> False
         |
         `- Yes -> Continue
                      |
                More characters?
                      |
                     Yes
                      |
                   Repeat

After loop
  |
Is stack empty?
 |- Yes -> True
 `- No  -> False
```

---

## Steps

### Step 1: Create the bracket map

```python
h = {')': '(', '}': '{', ']': '['}
```

This tells us which opening bracket is expected for each closing bracket.

```text
')' -> '('
'}' -> '{'
']' -> '['
```

### Step 2: Create the stack

```python
stk = []
```

The stack stores opening brackets.

### Step 3: Read each character

```python
for c in s:
```

Process the string one character at a time.

### Step 4: Push opening brackets

```python
if c not in h:
    stk.append(c)
```

If the character is an opening bracket, add it to the stack.

### Step 5: Check closing brackets

```python
if not stk:
    return False
```

If the stack is empty, there is no opening bracket available to match the closing bracket.

### Step 6: Pop the latest opening bracket

```python
popped = stk.pop()
```

Get the most recently added opening bracket.

### Step 7: Compare the brackets

```python
if popped != h[c]:
    return False
```

If the popped bracket does not match the expected opening bracket, the string is invalid.

### Step 8: Check the stack at the end

```python
return not stk
```

The string is valid only when all opening brackets have been matched.

---

## Code

```python
class Solution:
    def isValid(self, s: str) -> bool:

        # Map each closing bracket to its matching opening bracket
        h = {')': '(', '}': '{', ']': '['}

        # Store opening brackets
        stk = []

        # Check every character in the string
        for c in s:

            # Opening bracket -> add it to the stack
            if c not in h:
                stk.append(c)

            # Closing bracket
            else:

                # No opening bracket available to match it
                if not stk:
                    return False

                # Remove the most recently added opening bracket
                popped = stk.pop()

                # Check whether it matches the closing bracket
                if popped != h[c]:
                    return False

        # Valid only when no opening brackets are left
        return not stk
```

---

## Walkthrough

### Input

```text
"{[]}"
```

### `{`

Opening bracket -> push.

```text
Stack: ['{']
```

### `[` 

Opening bracket -> push.

```text
Stack: ['{', '[']
```

### `]`

Expected opening bracket:

```text
']' -> '['
```

Pop:

```text
Popped: '['
```

Match -> continue.

```text
Stack: ['{']
```

### `}`

Expected:

```text
'}' -> '{'
```

Pop:

```text
Popped: '{'
```

Match.

```text
Stack: []
```

The stack is empty.

```text
Result: True
```

---

## Edge Cases

### Empty string

```text
Input: ""
Output: True
```

There are no brackets to make invalid.

### Only opening brackets

```text
Input: "((("
Output: False
```

The stack still contains unmatched brackets.

### Closing bracket first

```text
Input: ")"
Output: False
```

There is nothing in the stack to match it.

### Wrong order

```text
Input: "([)]"
Output: False
```

`)` expects `(`, but the most recent opening bracket is `[`.

### Correct nesting

```text
Input: "({[]})"
Output: True
```

Every bracket closes in the correct order.

---

## Complexity

Let `n` be the length of the string.

### Time Complexity

**O(n)**

Each character is processed once.

### Space Complexity

**O(n)**

In the worst case, all characters can be opening brackets and stored in the stack.

---

## Key Takeaway

Remember this pattern:

```text
Opening bracket -> PUSH

Closing bracket
      |
    Check stack
      |
     POP
      |
   Compare
    /    \
 Wrong   Match
   |       |
 False   Continue

End
 |
Stack empty -> True
Stack not empty -> False
```

The important idea is:

> **The last opening bracket must be the first one to close.**

---

# Interview Questions & Answers

### 1. Why did you use a stack?

Because brackets must close in reverse order of how they were opened. A stack follows LIFO, so it fits this problem.

### 2. What does LIFO mean?

**Last In, First Out.**

The last item added to the stack is the first item removed.

### 3. Why do you use a dictionary?

It maps each closing bracket to the opening bracket it should match, making comparison simple.

### 4. Why do you push opening brackets?

We need to remember them so that when a closing bracket appears, we can compare it with the most recently opened bracket.

### 5. Why do you use `pop()`?

`pop()` removes the most recently added opening bracket, which is the bracket that should close first.

### 6. What happens if the stack is empty when a closing bracket appears?

There is no opening bracket available to match it, so we immediately return `False`.

### 7. Why is `"([)]"` invalid?

The stack contains:

```text
['(', '[']
```

When `)` appears, it expects `(`, but `pop()` gives `[`. They do not match, so the string is invalid.

### 8. Why is `"{[]}"` valid?

Each closing bracket matches the most recently opened bracket, and the stack is empty at the end.

### 9. What does `return not stk` do?

It checks whether the stack is empty.

```python
not []          # True
not ['(']       # False
```

So it returns `True` only when no unmatched opening brackets remain.

### 10. What is the time complexity?

**O(n)** because every character is processed once.

### 11. What is the space complexity?

**O(n)** because the stack can contain up to `n` opening brackets.

### 12. What is the main pattern in this problem?

**Stack + matching pairs.**

```text
Push opening brackets
Pop when closing brackets appear
Compare the pair
Check that the stack is empty at the end
```

### 13. Can a Python list be used as a stack?

Yes. `append()` adds to the top and `pop()` removes the top item.

### 14. What happens with `"((()))"`?

Opening brackets are pushed and then popped in reverse order. The stack becomes empty, so the result is `True`.

### 15. What happens with `"((("`?

All three opening brackets remain in the stack. Since the stack is not empty at the end, the result is `False`.

---

## Interview One-Liner

> **I use a stack because the last opening bracket must be the first one to close; I push opening brackets and pop and compare them when I encounter closing brackets.**
