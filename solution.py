import heapq
from typing import List

def find_kth_largest(nums: List[int], k: int) -> int:
    min_heap: List[int] = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]

if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(f"{k}nd largest element in {nums} is: {find_kth_largest(nums, k)}")
