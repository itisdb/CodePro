class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        lines = [line.strip() for line in f.readlines()]
        n, m = map(int, lines[0].split())
        total = 0
        for i in range(1, m + 1):
            a, b, k = map(int, lines[i].split())
            total += (b - a + 1) * k

        return total / n

    