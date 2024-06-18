class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeroCount = 0
        power5 = 5

        while n // power5:
            zeroCount += n // power5
            power5 *= 5
        return zeroCount