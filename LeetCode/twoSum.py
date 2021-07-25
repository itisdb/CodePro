from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            # List to store results
        result = []
        # Dictionary to store the difference and its index
        index_map = {}
        # Loop for each element
        for i, n in enumerate(nums):
            # Difference which needs to be checked
            difference = target - n
            if difference in index_map:
                result.append(i)
                result.append(index_map[difference])
                break
            else:
                index_map[n] = i
        return result
        '''Here in the else section we are storing the present value in the dictionary
        so that it can be used later when checking for the presence of the difference 
        in the dictionary'''