"""
You are given a non-empty array of integers nums. Every integer appears twice except for one.

Return the integer that appears only once.

You must implement a solution with
O(n)
O(n) runtime complexity and use only
O(1)
O(1) extra space.

Example 1:

Input: nums = [3,2,3]

Output: 2
Example 2:

Input: nums = [7,6,6,7,8]

Output: 8
Constraints:

1 <= nums.length <= 10000
-10000 <= nums[i] <= 10000
"""

"""
What to remember from this problem:

My initial approach was correct in spirit — use XOR to find duplicates.
But I was thinking of it as a search problem (for each element, scan the rest of the array to find its pair), when it's actually an accumulation problem (XOR everything together in one pass and let the math do the work).
Same mistake showed up in code: I reached for map (applies a function to each element independently) when I needed reduce (carries a result forward across the whole list).


XOR properties: a ^ a = 0, 0 ^ a = a, and it's commutative/associative — order doesn't matter.
This is a classic "find the unique element" pattern using bit manipulation.
reduce is your tool when you need to accumulate a result across a list; map is for independent transformations.
"""


from functools import reduce

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return reduce(lambda a, b: a ^ b, nums)

Solution = Solution()
print(Solution.singleNumber(nums=[3,2,3]))
print(Solution.singleNumber(nums=[7,6,6,7,8]))