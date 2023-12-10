from typing import List

class Solution:
    def __init__(self):
        pass

    """
    my solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for i in range(len(nums)-1):
            print(i)
            if nums[i] == nums[i+1]:
                return True
        return False
    """

    """
    optimized solution: uses set which keeps the unique elements of the list

    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_is_present = set()
        for num in nums:
            if num in num_is_present:
                return True
            num_is_present.add(num)
        return False

def main():
    s = Solution()
    print(s.containsDuplicate([1]))

if __name__ == "__main__":
    main()