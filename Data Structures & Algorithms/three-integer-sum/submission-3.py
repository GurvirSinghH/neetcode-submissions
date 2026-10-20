class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        l=set()
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            hs = set()
            for j in range(i+1, n):
                second = 0 - nums[i] - nums[j]
                if second in hs:
                    l.add((nums[i], second, nums[j]))
                hs.add(nums[j])
        return [list(t) for t in l]