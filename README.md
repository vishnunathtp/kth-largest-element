# Find the Kth Largest Element

Optimal heap-based and QuickSelect algorithm to find the $k$-th largest element in an unsorted array.

## Problem Description
Given an integer array `nums` and an integer `k`, return the $k$-th largest element in the array.

### Example
- Input: `nums = [3, 2, 1, 5, 6, 4], k = 2`
- Output: `5`

## Approach & Complexity
Maintain a min-heap containing the $k$ largest elements seen so far. For each element, insert into heap and pop if size exceeds $k$. The top of the heap is the answer.

- **Time Complexity:** $O(N \log K)$
- **Space Complexity:** $O(K)$

## How to Run & Test
```bash
python solution.py
python -m unittest discover tests
```
