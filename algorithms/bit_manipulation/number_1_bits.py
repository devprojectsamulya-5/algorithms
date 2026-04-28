"""
You are given an unsigned integer n. Return the number of 1 bits in its binary representation.

You may assume n is a non-negative integer which fits within 32-bits.

Example 1:

Input: n = 00000000000000000000000000010111

Output: 4
Example 2:

Input: n = 01111111111111111111111111111101

Output: 30
"""

"""
What to remember from this problem:

To inspect individual bits, use modulo 2 (or bitwise AND with 1) to check the last bit, then right shift to move to the next one.
This is the fundamental "bit counting" pattern — iterate through bits one at a time.

Push further(see v2 solution):
There's actually a clever trick using n & (n - 1) that skips over the 0 bits entirely, so it only loops as many times as there are 1-bits. Think about what n & (n - 1) does to the binary representation — try a few examples by hand and see if you can rewrite your solution using it.
Related problems:

LeetCode 338 — Counting Bits: Return the count of 1-bits for every number from 0 to n. Builds directly on this problem with a dynamic programming twist.
LeetCode 190 — Reverse Bits: Reverse the bits of a 32-bit integer. Uses the same shift-and-inspect pattern but in a different way
"""

class Solution:
    def numberOfBits_v1(self, n: int)-> int:
        counter = 0
        while (n > 0):
            counter += n % 2
            n = n >> 1
        return counter
    def numberOfBits_v2(self, n: int)-> int:
        counter = 0
        while (n > 0):
            counter += 1
            # everytime we do a n & n -1 the last 1 or righmost 1 becomes 0 and eveything after that flips.
            # so when we n & n-1, we make everything from the last 1 into a 0. We continue to do that until n becomes 0
            #The trick: n & (n - 1) always removes the rightmost 1-bit. So you just loop and count until n hits 0. The loop runs exactly as many times as there are 1-bits.
            #Starting with n = 12 (binary 1100), which has 2 one-bits:
            # Iteration 1: n = 1100 & 1011 = 1000, counter = 1
            # Iteration 2: n = 1000 & 0111 = 0000, counter = 2
            #Loop ends because n = 0. Counter is 2 — correct answer.
            n = n & (n-1)
        return counter
sol = Solution()
print(sol.numberOfBits_v1(0))
print(sol.numberOfBits_v1(0b01111111111111111111111111111101))
print(sol.numberOfBits_v1(0b00000000000000000000000000010111))
print(sol.numberOfBits_v1(1))

print(sol.numberOfBits_v2(0))
print(sol.numberOfBits_v2(0b01111111111111111111111111111101))
print(sol.numberOfBits_v2(0b00000000000000000000000000010111))
print(sol.numberOfBits_v2(1))