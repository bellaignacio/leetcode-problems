class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points:
            distances.append([(x ** 2) + (y ** 2), x, y]) # don't need to square root - can still compare distances accurately
        heapq.heapify(distances)

        results = []
        for i in range(k):
            dist, x, y = heapq.heappop(distances)
            results.append([x, y])

        return results
