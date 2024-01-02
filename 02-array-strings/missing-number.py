# LEETCODE problem 268

class Solution(object):
    
    # bruteforce

    def MissingNumber(self, nums):
        nums_sum = sum(nums)
        n = len(nums)
        actual_sum = 0
        for i in range(n+1):
            actual_sum += i
            i += 1
        return actual_sum - nums_sum
    
    # optimized

    def missing_number(self, nums):
        n = len(nums)
        return (n * (n+1) // 2) - (sum(nums))
    


    

missing = Solution()
print(missing.missing_number([3,0,1,2]))



