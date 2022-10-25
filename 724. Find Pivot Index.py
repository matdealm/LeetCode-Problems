class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Initializing leftSum and rightSum 
        leftSum, rightSum = 0, sum(nums)
        
        # traverse the elements through the loop
        for idx, ele in enumerate(nums):
            rightSum -= ele
            if leftSum == rightSum:
                return idx # return the pivot index
            leftSum += ele
        return -1        
