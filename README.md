**I will explain everything simply, sweetly, and clearly, just like you are five years old!**

# DSA Roadmap

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

### Two things to learn

**1. The solution progression**

> "How did we improve the brute-force solution?"

**2. The pattern**

> "How can I recognize that another problem needs the same technique?"

Do not memorize solutions. Learn the reason behind them.

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

- **Two Sum**
- **Best Time to Buy and Sell Stock**
- **Contains Duplicate**
- **Maximum Subarray**
- **Product of Array Except Self**
- **Remove Duplicates from Sorted Array**
- **Move Zeroes**
- **Missing Number**
- **Majority Element**
- **Intersection of Two Arrays**

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

- **Valid Palindrome**
- **Valid Anagram**
- **First Unique Character in a String**
- **Longest Substring Without Repeating Characters**
- **Reverse String**
- **Reverse Words in a String**
- **Group Anagrams**
- **Find All Anagrams in a String**
- **Minimum Window Substring** (later)

---

# 3. Hash Maps & Sets

### Core idea

> Use extra memory to make lookup fast.

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

- **Two Sum**
- **Contains Duplicate**
- **Valid Anagram**
- **First Unique Character in a String**
- **Group Anagrams**
- **Top K Frequent Elements** (later; usually combines hashing with heap/bucket sort)

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

- **Reverse String**
- **Valid Palindrome**
- **Remove Duplicates from Sorted Array**
- **Two Sum II — Input Array Is Sorted**
- **Merge Sorted Array**
- **3Sum**
- **Container With Most Water** (later)

---

# 5. Sliding Window

### Core idea

> Keep a moving section of a string/array instead of repeatedly checking every possible section.

Use it for **contiguous subarrays / substrings**.

Learn:

- Fixed-size window
- Variable-size window
- Expand right
- Shrink left
- Maintain sum/count/state

### Most important / commonly asked

- **Maximum Average Subarray I**
- **Best Time to Buy and Sell Stock**
- **Longest Substring Without Repeating Characters**
- **Longest Repeating Character Replacement**
- **Minimum Size Subarray Sum**
- **Find All Anagrams in a String**
- **Permutation in String**
- **Minimum Window Substring** (advanced)

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

- **Range Sum Query**
- **Product of Array Except Self**
- **Subarray Sum Equals K**
- **Minimum Size Subarray Sum**

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

> Nested structures / next greater or smaller → think Stack.

### Most important / commonly asked

- **Valid Parentheses**
- **Min Stack**
- **Next Greater Element**
- **Daily Temperatures**
- **Evaluate Reverse Polish Notation**
- **Largest Rectangle in Histogram** (later)

---

# 8. Queue

### Core idea

> **FIFO — First In, First Out.**

Learn:

- Enqueue/dequeue
- Queue implementation
- BFS
- Level-by-level processing

### Most important / commonly asked

- **Rotting Oranges**
- **Binary Tree Level Order Traversal**
- **Number of Islands** (BFS version)
- **Implement Queue using Stacks**

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

- **Reverse Linked List**
- **Middle of the Linked List**
- **Linked List Cycle**
- **Merge Two Sorted Lists**
- **Remove Nth Node From End of List**
- **Intersection of Two Linked Lists**
- **Palindrome Linked List**

---

# 10. Sorting

### Core idea

> Sometimes sorting makes the rest of the problem much easier.

Learn:

- When sorting helps
- Sorting + two pointers
- Sorting + intervals
- Sorting + greedy
- `O(n log n)` sorting

Do not spend excessive time implementing every sorting algorithm for interview preparation.

### Most important / commonly asked

- **Sort an Array**
- **Merge Sorted Array**
- **Contains Duplicate**
- **Merge Intervals**
- **Meeting Rooms**
- **Kth Largest Element in an Array** (later)

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

- **Binary Search**
- **Search Insert Position**
- **First Bad Version**
- **Find First and Last Position of Element in Sorted Array**
- **Search in Rotated Sorted Array**
- **Find Minimum in Rotated Sorted Array**
- **Koko Eating Bananas**
- **Capacity to Ship Packages Within D Days** (later)

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

- **Factorial**
- **Fibonacci**
- **Reverse String**
- **Subsets**
- **Tree Traversal**
- **Pow(x, n)**

---

# 13. Backtracking

### Core idea

> **Choose → Explore → Undo**

Use it when you must explore different possible choices.

### Most important / commonly asked

- **Subsets**
- **Permutations**
- **Combination Sum**
- **Letter Combinations of a Phone Number**
- **Word Search**
- **N-Queens** (advanced)

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

- **Maximum Depth of Binary Tree**
- **Binary Tree Preorder Traversal**
- **Binary Tree Inorder Traversal**
- **Binary Tree Level Order Traversal**
- **Invert Binary Tree**
- **Diameter of Binary Tree**
- **Lowest Common Ancestor**
- **Validate Binary Search Tree**
- **Search in a Binary Search Tree**

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

> Top/least K, repeated smallest/largest choice, priority processing.

### Most important / commonly asked

- **Kth Largest Element in an Array**
- **Top K Frequent Elements**
- **K Closest Points to Origin**
- **Last Stone Weight**
- **Task Scheduler**
- **Find Median from Data Stream** (advanced)

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

### Most important / commonly asked

- **Number of Islands**
- **Flood Fill**
- **Rotting Oranges**
- **Clone Graph**
- **Course Schedule**
- **Number of Connected Components**
- **Graph Valid Tree**
- **Network Delay Time** (later)

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

- **Set Matrix Zeroes**
- **Spiral Matrix**
- **Rotate Image**
- **Number of Islands**
- **Flood Fill**
- **Rotting Oranges**

---

# 18. Intervals

### Core idea

> Problems involving ranges such as `[start, end]`.

Learn:

- Sort by start/end
- Detect overlap
- Merge intervals
- Sweep-line idea

### Most important / commonly asked

- **Merge Intervals**
- **Insert Interval**
- **Non-overlapping Intervals**
- **Meeting Rooms**
- **Meeting Rooms II**
- **Minimum Number of Arrows to Burst Balloons**

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

- **Assign Cookies**
- **Jump Game**
- **Gas Station**
- **Non-overlapping Intervals**
- **Minimum Number of Arrows to Burst Balloons**
- **Task Scheduler** (also uses other patterns)

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

> Counting bits / XOR / binary-level operations.

### Most important / commonly asked

- **Single Number**
- **Number of 1 Bits**
- **Counting Bits**
- **Power of Two**
- **Missing Number** (also works as a bit-manipulation problem)

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

- **Climbing Stairs**
- **House Robber**
- **House Robber II**
- **Coin Change**
- **Unique Paths**
- **Longest Common Subsequence** (later)
- **Target Sum** (later)

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

- **Implement Trie (Prefix Tree)**
- **Design Add and Search Words Data Structure**
- **Word Search II** (advanced)

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

This is deliberately **not identical to Striver's page order**. It is a learning order designed to build one technique on top of another while keeping the high-value interview topics early. Striver's A2Z remains the main course structure; the Handbook and Sean Prashad resources help decide what to prioritize and how to recognize patterns.

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

Use it to **learn the topic progressively**.

### Tech Interview Handbook

Use it to **understand the technique, complexity, corner cases and interview priority**.

### Sean Prashad LeetCode Patterns

Use it to **recognize patterns and choose what to practice next**. It currently contains 179 questions grouped by pattern and includes heuristics such as sorted array → binary search/two pointers, fast lookup → hash table/set, next greater/smaller → monotonic stack, top-K → heap/quickselect/bucket sort, and permutations/subsets → backtracking.

### LeetCode

Use it to **write, submit, fail, fix, and repeat**.

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

### Arrays / Hashing

- Two Sum
- Contains Duplicate
- Best Time to Buy and Sell Stock
- Maximum Subarray
- Product of Array Except Self

### Strings

- Valid Palindrome
- Valid Anagram
- First Unique Character
- Longest Substring Without Repeating Characters

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
