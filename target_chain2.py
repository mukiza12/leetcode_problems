class TargetChain:
    
    # We only write the Two-Sum logic ONCE. 
    # We can reuse this function as many times as we want!
    def find_pairs(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_dict:
                return [num_dict[complement], i]
                
            num_dict[num] = i
            
        return []

    # Cleaned up unused parameters and fixed the return type hint
    def combine_targets(self, target1: int, target2: int) -> int:
        return target1 + target2


# --- The Game Execution ---
sol = TargetChain()

nums1 = [2, 7, 11, 13]
target1 = 9

nums2 = [3, 8, 12, 5]
target2 = 17

nums3 = [2, 7, 11, 13, 3, 8, 12, 5, 15]

# Play Stage 1
result1 = sol.find_pairs(nums1, target1)
result2 = sol.find_pairs(nums2, target2)

# Play Stage 2 (Combine and final search)
target3 = sol.combine_targets(target1, target2) 
final_output = sol.find_pairs(nums3, target3)

print(f"Stage 1 Result: {result1}")
print(f"Stage 2 Result: {result2}")
print(f"Final Boss Target ({target3}) Found At: {final_output}")