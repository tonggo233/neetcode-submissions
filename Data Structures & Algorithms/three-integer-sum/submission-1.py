
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(0, len(nums)-2):
            if nums[i] > 0:              # ✨ 优化1: 最小的数>0，不可能凑出0，直接结束
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            target = -nums[i]            # ✨ 优化2: 缓存target，避免每次都算3个数的和

            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif two_sum > target:
                    right -= 1
                else:
                    left += 1
        return result

