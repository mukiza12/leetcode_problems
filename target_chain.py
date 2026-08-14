class TargetChain:
    def targetchain_1(self, nums: list[int], target:int) -> list[int]:

        num_dict_1 = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_dict_1:
                return[num_dict_1[complement], i]

            num_dict_1[num] = i

        return[]

    def targetchain_2(self, nums: list[int], target:int) -> list[int]:
    
            num_dict_2 = {}
    
            for i, num in enumerate(nums):
                complement = target - num
    
                if complement in num_dict_2:
                    return[num_dict_2[complement], i]
    
                num_dict_2[num] = i
    
            return[]
    

    def combine (self, nums1: list[int], target1:int,  nums2: list[int], target2:int) -> list[int]:


         final_target = target1 + target2

         return final_target

    def last_chain (self, nums3: list[int], target3:int) -> list[int]:

         num_dict_3 = {}
             
         for i, num in enumerate(nums3):
                         complement = target3 - num
             
                         if complement in num_dict_3:
                             return[num_dict_3[complement], i]
             
                         num_dict_3[num] = i
             
         return[]
    
         

sol = TargetChain()


nums1 = [2, 7, 11, 13]
target1 = 9

nums2 = [3, 8, 12, 5]
target2 = 17

nums3 = [2, 7, 11, 13,3, 8, 12, 5, 15]
target3 = sol.combine(nums1,target1, nums2,target2)   

output = sol.last_chain(nums3, target3)
print(output)
    

    