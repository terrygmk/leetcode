# Python 3.10.4

class Solution:    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 蛮力
        # 空间复杂度：o(n^2)
        # 时间复杂度：o(1)
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                if nums[i] == target - nums[j] :
                    return [i,j]

    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        # 2次 Hash Table
        # 空间复杂度：o(n)
        # 时间复杂度：o(n)
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]] 

    def twoSum3(self, nums: list[int], target: int) -> list[int]:
        # 1次 Hash Table
        # 空间复杂度：o(n)
        # 时间复杂度：o(n)
        hashMap = {}
        for i in range(0,len(nums)):
            complement = target - nums[i]
            if complement in hashMap:
                return [hashMap[complement], i]
            hashMap[nums[i]] = i

if __name__ == '__main__':
    print('01-two-sum.py : 涉及查找速度,优先考虑hashMap. 以空间换时间。')
    nums = [2,7,11,15]
    target = 9
    print(Solution().twoSum(nums,target))
    print(Solution().twoSum2(nums,target))
    print(Solution().twoSum3(nums,target))