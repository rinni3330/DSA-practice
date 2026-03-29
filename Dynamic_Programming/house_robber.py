def rob(nums):

    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    dp = [0]*len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2,len(nums)):
        dp[i] = max(dp[i-1], nums[i] + dp[i-2])

    return dp[-1]

nums = list(map(int, input("Enter numbers: ").split()))
print("max robber:",rob(nums))

#optimized version
def rob(nums1):
    prev2, prev1 = 0, 0

    for num in nums1:
        curr = max(prev1, num + prev2)
        prev2 = prev1
        prev1 = curr

    return prev1

nums1 = list(map(int, input("Enter numbers: ").split()))
print("max robber:",rob(nums1))