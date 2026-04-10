def two_sum(nums: list[int], target: int) -> list[int]:
    # I have to create a hash map to store {number: index}
    seen = {}

    #this for loop has to iterate through each number with its index
    for i, num in enumerate(nums):

        #calculate what number we need to complete the pair
        complement = target - num

        #now we have to check if the number has already been seen bro
        if complement in seen:
            return[seen[complement], i]
        
        seen[num] = i

    return []

print(two_sum([11, 2, 15, 7 ], 9))
    
