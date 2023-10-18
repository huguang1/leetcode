def threeSum(nums):
    nums.sort()
    n, ans = len(nums), []
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i+1, n-1
        while l < r:
            if l > i + 1 and nums[l] == nums[l - 1]:
                l += 1
                continue
            if r < n - 1 and nums[r] == nums[r + 1]:
                r -= 1
                continue
            sums = nums[i]+nums[l]+nums[r]
            if sums == 0:
                ans.append([nums[i], nums[l], nums[r]])
                l += 1
            elif sums > 0:
                r -= 1
            else:
                l += 1
    return ans


