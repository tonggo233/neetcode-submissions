class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front = [1] * len(nums)

        for i in range(1, len(nums)):
            front[i] = front[i-1] * nums[i-1]

        back = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            back[i] = back[i+1] * nums[i+1]

        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = front[i] * back[i]

        return result