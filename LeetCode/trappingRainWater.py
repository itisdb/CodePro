class Solution:
    def trap(self, height: List[int]) -> int:
        if height is None:
            return 0
        if len(height) == 0:
            return 0
        if len(height) == 1 or height == 2:
            return 0
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        res = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    res += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    res += right_max - height[right]
                right -= 1
        return res