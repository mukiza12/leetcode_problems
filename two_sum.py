class Solution:
    def twoSum(self, nums: list[int], target:int) -> list[int]:

        num_dict = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_dict:
                return[num_dict[complement], i]

            num_dict[num] = i

        return[]

sol = Solution()

l_nums = [2,7,11,15]
target = 9

output = sol.twoSum(l_nums, target)

print(output)