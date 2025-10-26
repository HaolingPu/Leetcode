class Sidewalk:
    def __init__(self):
        # 已打湿区间列表，保持合并状态
        self.intervals = []

    def drop(self, x: float) -> bool:
        """落下一滴雨在 x 处，返回是否已经完全覆盖 [0,100]"""
        new = [max(0, x - 0.5), min(100, x + 0.5)]
        merged = []
        placed = False

        for l, r in self.intervals:
            # 若当前区间在 new 右侧且不重叠
            if r < new[0]:
                merged.append([l, r])
            # 若当前区间在 new 左侧且不重叠
            elif l > new[1]:
                if not placed:
                    merged.append(new)
                    placed = True
                merged.append([l, r])
            else:
                # 与 new 有重叠 → 合并
                new[0] = min(new[0], l)
                new[1] = max(new[1], r)

        if not placed:
            merged.append(new)
        self.intervals = merged

        print(self.intervals)
        # 检查是否全覆盖
        if len(self.intervals) == 1 and self.intervals[0][0] <= 0 and self.intervals[0][1] >= 100:
            return True
        return False


sidewalk = Sidewalk()
print(sidewalk.drop(0.3))   # False, 只打湿 [0,0.8]
print(sidewalk.drop(0.8))   # False, 合并成 [0,1.3]
print(sidewalk.drop(50.0))  # False, 分成两段 [0,1.3],[49.5,50.5]
print(sidewalk.drop(99.7))  # False, [99.2,100]