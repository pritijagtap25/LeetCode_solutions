from typing import List
# 26. Remove Duplicates from Sorted Array
def removeDuplicates(nums: list[int]) -> int:
    j = 1 
    for i in range(1, len(nums)):
        if nums[i] != nums [i-1]:
            nums[j] = nums[i]
            j += 1
    return j

# Test the function
test_nums = [1, 1, 2,2,3,3,4,4,5,5]
length = removeDuplicates(test_nums)
print(length)  # Output: 5
print(test_nums[:length])  # Output: [1,2,3,4,5]