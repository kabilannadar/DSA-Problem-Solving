# **DSA Realmap**

A structured interview-focused DSA roadmap built from:

- **Striver A2Z DSA Sheet** → structured learning order and progression.
- **Tech Interview Handbook** → interview priority, techniques, complexity, corner cases, and essential questions.
- **Sean Prashad LeetCode Patterns** → pattern recognition and representative LeetCode practice.

## How to use this roadmap

For **every problem**:

```text
Understand the problem
        ↓
Brute force
        ↓
Find the repeated/unnecessary work
        ↓
Better approach
        ↓
Optimal approach
        ↓
Code it yourself
        ↓
Test it
        ↓
Explain time + space complexity
```

The goal is not to memorize solutions.

The goal is to recognize:

```text
Problem → Pattern → Approach → Complexity
```

---

### Two things to learn

**1. The solution progression**

> "How did we improve the brute-force solution?"

**2. The pattern**

> "How can I recognize that another problem needs the same technique?"

Do not memorize solutions. Learn the reason behind them.

---

## Table of Contents

### Core Topics

1. [Arrays](#1-arrays)
2. [Strings](#2-strings)
3. [Hash Maps & Sets](#3-hash-maps--sets)
4. [Two Pointers](#4-two-pointers)
5. [Sliding Window](#5-sliding-window)
6. [Prefix Sum / Precomputation](#6-prefix-sum--precomputation)
7. [Stack](#7-stack)
8. [Queue](#8-queue)
9. [Linked List](#9-linked-list)
10. [Sorting](#10-sorting)
11. [Binary Search](#11-binary-search)
12. [Recursion](#12-recursion)
13. [Backtracking](#13-backtracking)
14. [Trees](#14-trees)
15. [Heaps / Priority Queue](#15-heaps--priority-queue)
16. [Graphs](#16-graphs)
17. [Matrix / 2D Arrays](#17-matrix--2d-arrays)
18. [Intervals](#18-intervals)
19. [Greedy](#19-greedy)
20. [Bit Manipulation](#20-bit-manipulation)
21. [Dynamic Programming](#21-dynamic-programming)
22. [Trie](#22-trie)
23. [Advanced Patterns](#23-advanced-patterns)

### Reference Sections

- [Final Learning Order](#final-learning-order)
- [Interview Priority](#interview-priority)
- [Resource Workflow](#resource-workflow)
- [The Rule for Your Problem List](#the-rule-for-your-problem-list)
- [Core Interview Set](#core-interview-set)

---

# 1. Arrays

### Learn

- Indexing and traversal
- In-place modification
- Counting/frequency
- Sorting
- Prefix/suffix precomputation
- Multiple passes
- Using the array index as information

### Patterns

- Two pointers
- Hash map/set
- Sliding window
- Prefix sum
- Sorting
- Binary search

### Most important / commonly asked

1. **Two Sum**
2. **Best Time to Buy and Sell Stock**
3. **Maximum Subarray**
4. **Contains Duplicate**
5. **Product of Array Except Self**
6. **Remove Duplicates from Sorted Array**
7. **Move Zeroes**
8. **Missing Number**

## Next Questions

- Majority Element
- Merge Sorted Array
- 3Sum
- Container With Most Water
- Maximum Product Subarray

---

# 2. Strings

### Learn

- Character traversal
- Frequency counting
- Palindromes
- Substrings vs subsequences
- String + hash map
- String + two pointers
- String + sliding window

### Patterns

- Two pointers
- Hash map/set
- Sliding window
- Sorting
- Stack

### Most important / commonly asked

1. **Reverse String**
2. **Valid Palindrome**
3. **Valid Anagram**
4. **First Unique Character in a String**
5. **Longest Substring Without Repeating Characters**
6. **Reverse Words in a String**

## Next Questions

- Group Anagrams
- Find All Anagrams in a String
- Longest Repeating Character Replacement
- Minimum Window Substring

---

# 3. Hash Maps & Sets

### Core idea

> Use extra memory when fast lookup or counting can remove repeated searching.

Learn:

- Dictionary
- Set
- Frequency counting
- Value → index
- Value → count
- Seen-before pattern
- Time/space trade-off

### Recognition

> **Need fast lookup? Think Hash Map / Set.**

### Most important / commonly asked

1. **Two Sum**
2. **Contains Duplicate**
3. **Valid Anagram**
4. **First Unique Character in a String**
5. **Group Anagrams**
6. **Majority Element**

## Next Questions

- Subarray Sum Equals K
- Longest Consecutive Sequence
- Top K Frequent Elements

---

# 4. Two Pointers

### Core idea

> Use two positions that move through the data in a controlled way.

Learn:

- Left/right pointers
- Same-direction pointers
- One pointer reads, another writes
- Two pointers on sorted arrays
- Two pointers on strings
- Fast/slow pointers in linked lists

### Recognition

> Can two moving positions replace repeated scanning?

### Most important / commonly asked

1. **Reverse String**
2. **Valid Palindrome**
3. **Remove Duplicates from Sorted Array**
4. **Two Sum II — Input Array Is Sorted**
5. **Merge Sorted Array**

## Next Questions

- 3Sum
- Container With Most Water
- Trapping Rain Water

---

# 5. Sliding Window

### Core idea

> Keep a moving section of a string/array instead of repeatedly checking every possible section.

### Recognition

Look for:

> contiguous subarray / substring + longest / shortest / maximum / minimum

Learn:

- Fixed-size window
- Variable-size window
- Expand right
- Shrink left
- Maintain sum/count/state

### Most important / commonly asked

1. **Longest Substring Without Repeating Characters**
2. **Best Time to Buy and Sell Stock**
3. **Minimum Size Subarray Sum**

## Next Questions

- Longest Repeating Character Replacement
- Find All Anagrams in a String
- Minimum Window Substring
- Sliding Window Maximum

---

# 6. Prefix Sum / Precomputation

### Core idea

> Calculate useful information once so later work becomes cheaper.

Learn:

- Prefix sum
- Prefix/suffix values
- Running totals
- Range queries
- Prefix + hash map

### Most important / commonly asked

1. **Range Sum Query**
2. **Product of Array Except Self**
3. **Subarray Sum Equals K**

## Next Questions

- Contiguous Array
- Range Sum Query 2D

---

# 7. Stack

### Core idea

> **LIFO — Last In, First Out.**

Learn:

- Push
- Pop
- Top/peek
- Matching brackets
- Monotonic stack

### Recognition

> Nested structures / Undo-like behavior / Next Greater or Smaller → think Stack.

### Most important / commonly asked

1. **Valid Parentheses**
2. **Min Stack**
3. **Next Greater Element**
4. **Daily Temperatures**

## Next Questions

- Evaluate Reverse Polish Notation
- Largest Rectangle in Histogram
- Asteroid Collision

---

# 8. Queue and BFS

### Core idea

> **FIFO — First In, First Out.**

> Queues are commonly used for BFS and level-by-level processing.

Learn:

- Enqueue/dequeue
- Queue implementation
- BFS
- Level-by-level processing

### Most important / commonly asked

1. **Rotting Oranges**
2. **Binary Tree Level Order Traversal**
3. **Number of Islands**
4. **Implement Queue using Stacks**

## Next Questions

- Open the Lock
- 01 Matrix

---

# 9. Linked List

### Core idea

> Nodes point to the next node instead of being accessed by array index.

Learn:

- Traversal
- Insert/delete
- Reverse links
- Singly/doubly linked list
- Fast/slow pointers

### Recognition

> Linked list + two moving pointers → often fast/slow pointer technique.

### Most important / commonly asked

1. **Reverse Linked List**
2. **Linked List Cycle**
3. **Middle of the Linked List**
4. **Merge Two Sorted Lists**
5. **Remove Nth Node From End of List**

## Next Questions

- Intersection of Two Linked Lists
- Palindrome Linked List
- Add Two Numbers
- Reorder List

---

# 10. Sorting

### Core idea

> Sometimes sorting makes the rest of the problem much easier.

Learn:

- Why sorting can simplify a problem
- Sorting + two pointers
- Sorting + intervals
- Sorting + greedy
- Basic sorting complexities
- `O(n log n)` sorting

Do not spend excessive time implementing every sorting algorithm for interview preparation.

### Most important / commonly asked

1. **Sort an Array**
2. **Merge Sorted Array**
3. **Sort Colors**
4. **Merge Intervals**

## Next Questions

- Non-overlapping Intervals
- Meeting Rooms
- Kth Largest Element in an Array

---

# 11. Binary Search

### Core idea

> If the data/answer has a property that lets you remove half the possibilities, use binary search.

Learn:

- Basic binary search
- Search space
- First/last occurrence
- Rotated sorted arrays
- Binary search on the answer

### Recognition

> Sorted data or a monotonic answer space.

### Most important / commonly asked

1. **Binary Search**
2. **Search Insert Position**
3. **Find First and Last Position of Element in Sorted Array**
4. **Search in Rotated Sorted Array**
5. **Find Minimum in Rotated Sorted Array**

## Next Questions

- Search a 2D Matrix
- Koko Eating Bananas
- Capacity to Ship Packages Within D Days

---

# 12. Recursion

### Core idea

> A function solves a smaller version of the same problem.

Every recursive solution has:

```text
Base case
+
Recursive case
```

### Learn

- Base case
- Recursive call
- Return flow
- Call stack

### Most important / commonly asked

1. **Factorial**
2. **Fibonacci Number**
3. **Reverse String**
4. **Power of a Number**
5. **Subsets**

## Next Questions

- Permutations
- Tree Traversal
- Pow(x, n)

---

# 13. Backtracking

### Core idea

```text
Choose
  ↓
Explore
  ↓
Undo
```

Use it when you must explore different possible choices.

### Most important / commonly asked

1. **Subsets**
2. **Permutations**
3. **Combination Sum**

## Next Questions

- Letter Combinations of a Phone Number
- Word Search
- Palindrome Partitioning
- N-Queens

---

# 14. Trees

### Core idea

> One node can branch into other nodes.

Learn in this order:

```text
Binary Tree
   ↓
DFS
   ├── Preorder
   ├── Inorder
   └── Postorder
   ↓
BFS / Level Order
   ↓
Height / Depth
   ↓
Diameter
   ↓
Lowest Common Ancestor
   ↓
BST
```

### BST

Learn:

- Search
- Insert
- Delete
- Validate

### Most important / commonly asked

1. **Maximum Depth of Binary Tree**
   2 **Binary Tree Preorder Traversal**
2. **Binary Tree Inorder Traversal**
3. **Binary Tree Level Order Traversal**
4. **Invert Binary Tree**
5. **Validate Binary Search Tree**

## Next Questions

- Diameter of Binary Tree
- Lowest Common Ancestor
- Search in a Binary Search Tree
- Insert into a Binary Search Tree
- Delete Node in a BST
- Balanced Binary Tree

---

# 15. Heaps / Priority Queue

### Core idea

> Quickly access the smallest or largest item while keeping the rest available.

Learn:

- Min heap
- Max heap
- Push
- Pop
- Peek
- Python `heapq`
- Top-K pattern

### Recognition

> Top/least K, repeated smallest/largest choice, Repeated priority-based processing.

### Most important / commonly asked

1. **Kth Largest Element in an Array**
2. **Top K Frequent Elements**
3. **K Closest Points to Origin**
4. **Last Stone Weight**

## Next Questions

- Task Scheduler
- Merge K Sorted Lists
- Find Median from Data Stream

---

# 16. Graphs

### Core idea

> Things connected to other things.

Learn:

1. Graph representation
2. BFS
3. DFS
4. Connected components
5. Cycle detection
6. Shortest path basics
7. Topological sort
8. Union-Find

### Recognition

```text
Reach / traverse → BFS or DFS
Connectivity → DFS / BFS / Union-Find
Dependencies → Topological Sort
Shortest path → BFS / Dijkstra
```

### Most important / commonly asked

1. **Number of Islands**
2. **Flood Fill**
3. **Rotting Oranges**
4. **Clone Graph**
5. **Course Schedule**

## Next Questions

- Number of Connected Components
- Graph Valid Tree
- Redundant Connection
- Course Schedule II
- Network Delay Time

---

# 17. Matrix / 2D Arrays

### Core idea

> An array where each position can have rows, columns and neighboring cells.

Learn:

- Row/column traversal
- Boundary checks
- Directions
- Visited cells
- BFS/DFS on grids

### Most important / commonly asked

1. **Spiral Matrix**
2. **Set Matrix Zeroes**
3. **Rotate Image**
4. **Number of Islands**
5. **Flood Fill**

## Next Questions

- Search a 2D Matrix
- Word Search
- Pacific Atlantic Water Flow

---

# 18. Intervals

### Core idea

Work with ranges such as:

```text
[start, end]
```

Learn:

- Sort by start/end
- Detect overlap
- Merge intervals
- Sweep-line idea

### Recognition

For overlapping intervals:

> Sort first, then reason about the overlap.

### Most important / commonly asked

1. **Merge Intervals**
2. **Insert Interval**
3. **Non-overlapping Intervals**
4. **Meeting Rooms**
5. **Meeting Rooms II**

## Next Questions

- Minimum Number of Arrows to Burst Balloons
- Interval List Intersections

---

# 19. Greedy

### Core idea

> Make the best choice now when that choice can be shown to lead to the best overall result.

Do not assume "greedy" means simply choosing what looks best.

Learn:

- Local choice
- Why the choice is safe
- Sorting + greedy
- Interval greedy problems

### Most important / commonly asked

1. **Jump Game**
2. **Best Time to Buy and Sell Stock**
3. **Assign Cookies**
4. **Non-overlapping Intervals**

## Next Questions

- Jump Game II
- Gas Station
- Partition Labels

---

# 20. Bit Manipulation

### Core idea

> Work directly with the binary bits of numbers.

Learn:

- AND
- OR
- XOR
- Left/right shift
- Set/unset/toggle bits
- Counting bits

### Recognition

> XOR / binary representation / bit counting → think Bit Manipulation.

### Most important / commonly asked

1. **Single Number**
2. **Number of 1 Bits**
3. **Counting Bits**
4. **Power of Two**
5. **Missing Number** (also works as a bit-manipulation problem)

---

# 21. Dynamic Programming

### Core idea

> Solve smaller problems once, remember the answers, and reuse them.

Think:

```text
Recursion
   ↓
Repeated work
   ↓
Memoization
   ↓
Bottom-up DP
```

### Recognition

> The same smaller problems keep appearing.

### Most important / commonly asked

1. **Climbing Stairs**
2. **House Robber**
3. **Coin Change**
4. **Unique Paths**

## Next Questions

- House Robber II
- Target Sum
- Longest Common Subsequence
- Word Break
- Longest Increasing Subsequence

**Do DP late.** It is one of the least useful topics to attack first when your fundamentals are still developing.

---

# 22. Trie

### Core idea

> A tree designed to store words/prefixes.

Learn:

- Insert
- Search
- Prefix search

### Most important / commonly asked

1. **Implement Trie (Prefix Tree)**
2. **Design Add and Search Words Data Structure**

## Next Questions

- Word Search II

---

# 23. Advanced Patterns

Learn these only after the core patterns are comfortable.

### Monotonic Stack

- Next Greater Element
- Daily Temperatures
- Largest Rectangle in Histogram
- Trapping Rain Water

### Monotonic Queue

- Sliding Window Maximum

### Union-Find

- Number of Connected Components
- Graph Valid Tree
- Redundant Connection

### Topological Sort

- Course Schedule
- Course Schedule II
- Alien Dictionary (advanced)

### Shortest Path

- Network Delay Time
- Cheapest Flights Within K Stops

### Advanced Range Queries

- Binary Indexed Tree
- Segment Tree

### Advanced Selection

- Kth Largest
- Quickselect

Sean Prashad's current pattern heuristics specifically map these problem clues to monotonic stacks/queues, prefix sums/BIT/segment trees, Union-Find, topological sort, shortest-path methods, and heap/quickselect/bucket-sort approaches.

---

# Final Learning Order

Use this as the actual sequence:

```text
1. Arrays
2. Strings
3. Hash Maps & Sets
4. Two Pointers
5. Sliding Window
6. Prefix Sum / Precomputation
7. Stack
8. Queue
9. Linked List
10. Sorting
11. Binary Search
12. Recursion
13. Backtracking
14. Trees
15. Heaps / Priority Queue
16. Graphs
17. Matrix / 2D Arrays
18. Intervals
19. Greedy
20. Bit Manipulation
21. Dynamic Programming
22. Trie
23. Advanced Patterns
```

# Pattern Recognition Cheat Sheet

| When the problem says / shows... | Think...                     |
| -------------------------------- | ---------------------------- |
| Need fast lookup                 | Hash Map / Set               |
| Sorted array                     | Binary Search / Two Pointers |
| Compare from both ends           | Two Pointers                 |
| Modify in place                  | Two Pointers / Swapping      |
| Contiguous subarray / substring  | Sliding Window               |
| Repeated range sums              | Prefix Sum                   |
| Matching brackets                | Stack                        |
| Next greater / smaller           | Monotonic Stack              |
| First-in-first-out processing    | Queue                        |
| Linked list + middle/cycle       | Fast & Slow Pointers         |
| Top K / Kth largest              | Heap / Quickselect           |
| Tree                             | DFS / BFS                    |
| Grid traversal                   | BFS / DFS                    |
| Graph connectivity               | DFS / BFS / Union-Find       |
| Dependencies                     | Topological Sort             |
| Shortest weighted path           | Dijkstra                     |
| Overlapping ranges               | Sort + Intervals             |
| Generate all combinations        | Backtracking                 |
| Same smaller problems repeat     | Dynamic Programming          |
| Prefix matching                  | Trie                         |
| XOR / bit counting               | Bit Manipulation             |

---

# Interview Priority

If time is limited, prioritize:

## 🔴 Highest priority

```text
Arrays
Strings
Hash Maps / Sets
Two Pointers
Sliding Window
Stack
Linked List
Binary Search
Trees
```

## 🟠 High priority

```text
Queue / BFS
Heap / Priority Queue
Graphs
Matrix
Intervals
Recursion
Backtracking
Greedy
```

## 🟡 Later

```text
Bit Manipulation
Dynamic Programming
Trie
Advanced Graphs
Advanced Range Queries
```

Tech Interview Handbook currently places Array, String, Sorting/Search, Matrix, Tree and Graph among its high-priority areas, with Hash Table, Recursion, Linked List, Queue, Stack, Heap, Trie and Interval in a middle tier, and DP lower.

---

# Resource Workflow

### Striver A2Z

Use Striver as the **main learning sequence**.

```text
Learn concept
→ brute force
→ better
→ optimal
```

## Tech Interview Handbook

Use it to understand:

- What is high priority?
- What technique is being used?
- What complexity should I know?
- What corner cases matter?
- Which questions are essential vs recommended?

## Sean Prashad — LeetCode Patterns

Use it after learning a topic to practice **pattern recognition** and find related problems. It currently contains 179 questions grouped by pattern and includes heuristics such as sorted array → binary search/two pointers, fast lookup → hash table/set, next greater/smaller → monotonic stack, top-K → heap/quickselect/bucket sort, and permutations/subsets → backtracking.

### LeetCode

Use it to actually:

```text
Write
→ Run
→ Fail
→ Debug
→ Submit
→ Repeat
```

---

# The Rule for Your Problem List

Do not try to finish every problem listed here.

For a new pattern:

```text
Learn pattern
   ↓
1 brute-force problem
   ↓
1 easy representative problem
   ↓
1–2 variations
   ↓
Move on
```

Then revisit old patterns.

The goal is to reach:

> **"I have seen this before. I know what approach to try."**

rather than:

> **"I remember the exact code for this one problem."**

---

# Core Interview Set

If you eventually need one compact set to revise before interviews:

### Arrays / Strings

- Two Sum
- Maximum/Largest Element
- Second Largest
- Contains Duplicate
- Reverse String
- Palindrome
- Character Frequency
- First Non-Repeating Character
- Anagram
- Remove Duplicates
- Missing Number
- Move Zeroes
- Maximum Subarray
- Best Time to Buy and Sell Stock

### Basic DSA

- Valid Parentheses
- Reverse Linked List
- Linked List Cycle
- Merge Two Sorted Lists
- Binary Search
- Basic BFS/DFS problem

### Basic numbers

- Prime Number
- Fibonacci
- Factorial
- Palindrome Number
- Reverse Number
- Armstrong Number
- Sum of Digits
- GCD / HCF
- LCM

# Advanced Interview Set

### Two Pointers / Sliding Window

- Reverse String
- Remove Duplicates from Sorted Array
- Two Sum II
- Minimum Size Subarray Sum
- Longest Repeating Character Replacement

### Stack

- Valid Parentheses
- Min Stack
- Next Greater Element
- Daily Temperatures

### Linked List

- Reverse Linked List
- Middle of Linked List
- Linked List Cycle
- Merge Two Sorted Lists

### Binary Search

- Binary Search
- Search Insert Position
- Search in Rotated Sorted Array
- Find Minimum in Rotated Sorted Array

### Trees

- Maximum Depth of Binary Tree
- Invert Binary Tree
- Binary Tree Level Order Traversal
- Diameter of Binary Tree
- Validate Binary Search Tree

### Heap

- Kth Largest Element in an Array
- Top K Frequent Elements

### Graphs

- Number of Islands
- Flood Fill
- Rotting Oranges
- Course Schedule

### Backtracking

- Subsets
- Permutations
- Combination Sum

### Dynamic Programming

- Climbing Stairs
- House Robber
- Coin Change

## The standard for moving to the next topic

You do not need to solve every problem.

Move on when you can:

- Explain the basic pattern.
- Recognize when to use it.
- Solve a few representative problems without copying.
- Explain the brute-force approach.
- Explain why the optimized approach is better.
- Explain time and space complexity in simple words.

> **Learn fewer problems deeply instead of collecting hundreds of solutions.**
