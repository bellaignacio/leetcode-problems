from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        def _build_graph(edges):
            graph = defaultdict(list)

            for edge in edges:
                src, dst = edge
                graph[src].append(dst)

            return graph

        red = _build_graph(redEdges)
        blue = _build_graph(blueEdges)

        answer = [-1 for _ in range(n)]
        visited = set([(0, None)]) # (node, previous edge color)
        queue = deque([(0, 0, None)]) # (node, length, previous edge color)

        while queue:
            node, length, previous = queue.popleft()
            if answer[node] == -1:
                answer[node] = length
            if previous != 'red':
                for neighbor in red[node]:
                    if (neighbor, 'red') not in visited:
                        visited.add((neighbor, 'red'))
                        queue.append((neighbor, length + 1, 'red'))
            if previous != 'blue':
                for neighbor in blue[node]:
                    if (neighbor, 'blue') not in visited:
                        visited.add((neighbor, 'blue'))
                        queue.append((neighbor, length + 1, 'blue'))

        return answer
