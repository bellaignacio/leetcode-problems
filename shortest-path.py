from collections import defaultdict, deque

def shortest_path(edges, nodeA, nodeB):
    graph = build_graph(edges)
    visited = set()
    visited.add(nodeA) # same as visited = set([nodeA])
    queue = deque()
    queue.append((nodeA, 0)) # same as queue = deque([(nodeA, 0)])

    while queue:
        node, distance = queue.popleft()
        if node == nodeB:
            return distance
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return -1


def build_graph(edges):
    graph = defaultdict(list)

    for edge in edges:
        node1, node2 = edge
        graph[node1].append(node2)
        graph[node2].append(node1)

    return graph
