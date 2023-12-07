from collections import deque, defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj_list = defaultdict(list)

        for i in range(n):
            if manager[i] != -1:
                adj_list[manager[i]].append(i)

        queue = deque()
        queue.append((headID, 0))
        max_time = 0

        while queue:
            mgr, running_time = queue.popleft()
            max_time = max(max_time, running_time)

            for emp in adj_list[mgr]:
                queue.append((emp, running_time + informTime[mgr]))

        return max_time
