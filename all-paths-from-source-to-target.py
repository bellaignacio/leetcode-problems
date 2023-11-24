class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        results = []

        def _backtrack(current, path):
            if current == target:
                results.append(path.copy())
                return

            for neighbor in graph[current]:
                path.append(neighbor)
                _backtrack(neighbor, path)
                path.pop()

        _backtrack(0, [0])
        return results
