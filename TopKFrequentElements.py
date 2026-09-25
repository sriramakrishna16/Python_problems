def freqElements(nums, k):
    group = {}
    for num in nums:
        group[num] = group.get(num,0)+1
    sorted_list = sorted(group, key = group.get, reverse = True)
    print(sorted_list)
    return sorted_list[:k]

nums = [1, 1, 1, 2, 2, 3, 3, 3, 3]
k = 2
print(freqElements(nums,k))