class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = []
        tar = target
        for i in range(0, len(nums)):
            numbers.insert(i, nums[i])
        for x in range(len(numbers)):
            for y in range(x+1, len(numbers)):
                if numbers[x]+ numbers[y] == tar:
                    return [x, y]