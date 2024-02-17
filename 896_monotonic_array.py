from typing import List

def isMonotonic(nums: List[int]) -> bool:

    # Lập trình tại đây
    new_nums = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            new_nums.append(nums[i])
            
    nums = new_nums
    # print(nums)
    if len(nums) == 1:
        return True
    
    if nums[0] < nums[1]:
        for i in range(2, len(nums)):
                if nums[i-1] > nums[i]:
                    return False
        return True
    
    for i in range(2, len(nums)):
        if nums[i-1] < nums[i]:
            return False
    return True

def main():
    print(isMonotonic([1,2,2,3])) # True
    print(isMonotonic([-1, 2000, 33999, 3])) # False
    print(isMonotonic([1,3,2])) # False
    print(isMonotonic([1,5,2])) # False
    print(isMonotonic([6,6,100])) # True
    print(isMonotonic([5,3,2,4,1])) # False
    print(isMonotonic([1,1,1,1,1])) # True
    print(isMonotonic([1,1,1,1,2])) # True
    
if __name__ == "__main__":
    main()
