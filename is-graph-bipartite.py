class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        nodeColors = {}

        def _colorNodes(node, currentColor):
            if node in nodeColors:
                return nodeColors[node] == currentColor
                
            nodeColors[node] = currentColor
            for neighbor in graph[node]:
                if not _colorNodes(neighbor, not currentColor):
                    return False
            return True

        for node in range(len(graph)):
            if node not in nodeColors and not _colorNodes(node, True):
                return False

        return True
