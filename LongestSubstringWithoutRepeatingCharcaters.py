s = "abcabcbb"

def ls(s):
    char_set = set()
    left = 0

    count = 0

    for right in range(len(s)):
        if s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        count = max(count, right - left + 1)

    return count

ans = ls(s)
print(ans)

