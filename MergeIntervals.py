intervals =[
    [1,3],
    [2,6],
    [8,10],
    [9,12]
]

def mergeIntervals(intervals):
    intervals.sort(key = lambda x : x[0])

    ans = []

    for interval in intervals:
        start = interval[0]
        end = interval[1]

        if not ans or start > ans[-1][1]:
            ans.append([start, end])
        else:
            ans[-1][1] = max(ans[-1][1], end)

    return ans 

print(mergeIntervals(intervals))
        