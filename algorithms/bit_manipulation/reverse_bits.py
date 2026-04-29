"""
Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result.

Example 1:

Input: n = 00000000000000000000000000010101

Output:    2818572288 (10101000000000000000000000000000)
Explanation: Reversing 00000000000000000000000000010101, which represents the unsigned integer 21, gives us 10101000000000000000000000000000 which represents the unsigned integer 2818572288.
"""

"""
My original thinking: Swap first and last bits in place — correct intuition but unnecessarily complicated for implementation.
The key insight: Don't swap in place. Build the reversed number from scratch by extracting bits from the right side of n and pushing them into the left side of result, one at a time. Left-shift result, add the bit, right-shift n. Repeat 32 times.
What to remember: When you need to rearrange bits, building a new number is usually simpler than modifying in place. The pattern of "extract last bit, shift result, add bit" is a fundamental bit manipulation building block.
Related problems to try:

LeetCode 7 — Reverse Integer: Similar idea but with decimal digits instead of bits, with overflow considerations.
LeetCode 461 — Hamming Distance: XOR two numbers then count 1-bits — combines patterns from your previous problems.
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        count = 0
        while count < 32:
            result = (result << 1) + (n & 1)
            n = n >> 1
            count = count + 1
        return result