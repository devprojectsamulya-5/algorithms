"""
Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].

Return an array output where output[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 4

Output: [0,1,1,2,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100

Constraints:

0 <= n <= 1000
"""

"""
My original mistake: I confused i - 1 (the previous number) with i >> 1 (the number with its last bit dropped). These are very different — i - 1 has no meaningful bit-count relationship to i, but i >> 1 does because it's literally i minus its last bit.
The key insight: Any number's 1-bit count can be broken into two parts: everything except the last bit (i >> 1, already computed) plus the last bit itself (i & 1). This is what makes the DP work — every answer depends on a smaller, already-solved subproblem.
What to remember: When building a DP solution over binary representations, right-shift (>> 1) is your go-to way to connect a number to a smaller subproblem, not - 1.
The problem happens with the powers of 2, lets say we have to calculate 1 is 128, answer is 1, how do you explain this
Great question. Let's trace it.
128 is 10000000. 128 >> 1 is 64, which is 1000000. 128 & 1 is 0.
So count[128] = count[64] + 0 = count[64].
And 64 >> 1 is 32, 64 & 1 is 0. So count[64] = count[32] + 0.
This keeps going: 32 → 16 → 8 → 4 → 2 → 1. All powers of 2, all with last bit 0, so we just keep copying the count from the smaller power of 2.
Until we hit 1: 1 >> 1 is 0, 1 & 1 is 1. So count[1] = count[0] + 1 = 1.
That 1 propagates all the way back up. Every power of 2 has exactly one 1-bit, and the chain of right-shifts eventually reaches 1, which is where that single count comes from.
but what if the number is 130

130 is 10000010.
130 >> 1 is 65 (1000001), and 130 & 1 is 0. So count[130] = count[65] + 0.
65 >> 1 is 32 (100000), and 65 & 1 is 1. So count[65] = count[32] + 1.
And we already know count[32] chains down to 1 through powers of 2.
So count[130] = 1 + 1 = 2. Which is correct — 10000010 has two 1-bits.
Each right-shift peels off the last bit. Every time that last bit is a 1, we add 1 to the count. The chain always terminates at count[0] = 0.

"""

class Solution:
    def numberOfBits(self, n: int) -> list[int]:
        count = []
        count.append(0)
        i = 1
        while i <= n:
            count.append(count[i >> 1] + (i & 1))
            i += 1
        return count

sol = Solution()
print(sol.numberOfBits(0))
print(sol.numberOfBits(2))
print(sol.numberOfBits(5))