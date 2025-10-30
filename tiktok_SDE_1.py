

def merge_intervals(intervals):
    if not intervals or len(intervals) == 0:
        return []
    output = []
    intervals.sort(key=lambda x:x[0])
    for s, e in intervals:
        if not output or output[-1][1] < s:
            output.append([s,e])
        else:
            output[-1][1] = max(e, output[-1][1])
    
    return output 

test1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(f"输入: {test1}")
print(f"输出: {merge_intervals(test1)}")

test2 = [[1, 4], [2, 3]]
print(f"\n输入: {test2}")
print(f"输出: {merge_intervals(test2)}")


# passed