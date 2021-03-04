class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        result = []
        for m in range(len(nums)):
            a = nums[m]
            for n in range(m+1,len(nums)):
                b = nums[n]
                if a + b == target:
                    result.append(m)
                    result.append(n)
        return result

nums = [1,2,3,4,5,6]
target = 9
object = Solution()

result = object.twoSum(nums,target)
print(result)






