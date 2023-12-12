from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        # my solution
        nums.sort()
        for i in range(nums[0], len(nums)+1):
            if i not in nums:
                return i
        """

        # optimized version

        # sum of nums
        sum_of_nums = sum(nums)
        sum_of_range = (len(nums)*(len(nums)+1))/2

        return sum_of_range - sum_of_nums

def main():
    nums = [9,6,4,2,3,5,7,0,1]
    s = Solution()
    missing_number = s.missingNumber(nums)
    print(f"the missing number from {nums} is: {missing_number}")
    # print(s.missingNumber(nums))

if __name__ == "__main__":
    main()