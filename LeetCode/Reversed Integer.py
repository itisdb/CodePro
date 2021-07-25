class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        if x < 0:
            x = -x
            x = str(x)[::-1]
            x = int(x)
            x = -x
        else:
            x = str(x)[::-1]
            x = int(x)

        if x <= -pow(2,31) or x >= pow(2,31) - 1:
            return 0
        return x