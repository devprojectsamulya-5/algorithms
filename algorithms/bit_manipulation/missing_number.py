"""
Given an array nums containing n integers in the range [0, n] without any duplicates, return the single number in the range that is missing from nums.

Follow-up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

Example 1:

Input: nums = [1,2,3]

Output: 0
Explanation: Since there are 3 numbers, the range is [0,3]. The missing number is 0 since it does not appear in nums.

Example 2:

Input: nums = [0,2]

Output: 1
Constraints:

1 <= nums.length <= 1000

"""

"""
The key insight: This is the same XOR trick from the single number problem, just reframed. Instead of every number appearing twice except one, you create the pairs yourself — XOR the expected range with the actual array, and the unpaired (missing) number survives.
What to remember: Whenever a problem involves finding what's missing or unique in a known range, think about XOR. Create pairs artificially by combining the expected set with the actual set.
Alternative approach worth knowing: There's a math-based solution — sum of [0, n] is n*(n+1)/2. Subtract the actual sum of the array. The difference is the missing number. Same complexity, no XOR needed.
Related problems:

LeetCode 268 → LeetCode 41 — First Missing Positive: Harder version — array is unsorted, can contain negatives, and you need the first missing positive. Requires a different technique.
LeetCode 287 — Find the Duplicate Number: Inverse of this problem — one number appears twice instead of one being missing. Has a clever O(1) space solution using a different pattern entirely.

"""
from functools import reduce

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        orig_xor = 0
        arr_xor = 0
        n = len(nums) + 1
        orig_xor = reduce(lambda a, b: a ^ b, range(0,n))
        arr_xor =  reduce(lambda a, b: a ^b, nums)
        return orig_xor ^ arr_xor