nums = [4, 3, 2, 7, 8, 2, 3, 1]


# using dictionary

# def findDup(nums):
#     seen = {}
#     for num in nums:
#         seen[num] = seen.get(num,0)+1
#     ans = []
#     for i, j in seen.items():
#         if j > 1:
#             ans.append(i)
#             z += 1
#     return ans

# using set

def findDup(nums):
    seen = set()
    ans = []

    for num in nums:
        if num in seen:
            ans.append(num)
        else:
            seen.add(num)
    return ans

ans = findDup(nums)
print(ans)