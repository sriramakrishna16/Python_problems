nums = [100, 4, 200, 1, 3, 2]


# order of n log n
# def lcs(nums):
#     if not nums:
#         return 0
#     nums = sorted(nums)
#     final = 1
#     count = 1
#     for i in range(1,len(nums)):
#         if nums[i] - nums[i-1] == 1:
#             count += 1
#         else:
#             count = 1

#         if count > final:
#             final = count

#     return final

# order of n
def lcs(nums):
    nums_set = set(nums)
    longest = 0

    for num in nums_set:
        if num - 1 not in nums_set:
            current = num
            count = 1
            while current + 1 in nums_set:
                current += 1
                count += 1
            longest = max(longest, count)

        return longest

ans = lcs(nums)
print(ans)