class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = []
        duplicate = False
        for i in range(len(nums)):
            sorted_nums.append(nums[i])
        sorted_nums.sort()  
        print(sorted_nums)

        for i in range(0, len(sorted_nums)-1):
            if sorted_nums[i] == sorted_nums[i+1]:
                duplicate = True
        return duplicate