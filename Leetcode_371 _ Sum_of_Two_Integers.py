class Solution:
    def getSum(self, a: int, b: int) -> int:
        MOD     = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b != 0:
            a, b = (a ^ b) & MOD, ((a & b) << 1) & MOD
        return a if a <= MAX_INT else ~(a & MAX_INT) ^ MAX_INT

        print (getSum4(-4,2))
