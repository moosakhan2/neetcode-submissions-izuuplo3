class Solution:
    def getSum(self, a: int, b: int) -> int:
        max_int = 0x7fffffff
        mask = 0xffffffff

        while b != 0:
            tmp = (a&b)<<1
            a = (a^b) & mask # clip it within 32 bits
            b = tmp & mask

        if a > max_int:
            return ~(a^mask)
        
        return a
            
       

# 2 and 1

# 0 0 1
# 0 1 1
# ^
# a & b << 1