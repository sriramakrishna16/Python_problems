def threeSum(nums):
    nums.sort()
    ans = []
    for x in range(len(nums)):
        if x > 0 and nums[x] == nums[x-1]:
            continue
        left = x + 1
        right = len(nums)-1
        if nums[x] > 0:
            break
        while left < right:
            sum = nums[x] + nums[left] + nums[right]
            if sum == 0:
                ans.append([nums[x], nums[left], nums[right]])
                while nums[left] == nums[left + 1]:
                    left += 1
                while nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif sum > 0:
                right -= 1
            else:
                left += 1
    return ans


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))

s = "raama"
parts = s.split()
print(parts)