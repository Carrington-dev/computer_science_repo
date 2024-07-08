from collections import defaultdict, deque


def bfs(n, m, edges, s):
    # Create graph representation as adjacency list
    graph = defaultdict(set)
    for start, end in edges:
        graph[start].add(end)
        graph[end].add(start)

    print(graph)
    
    # Use hash table to store distances
    distances = {}
    
    # Use deque as a queue
    q = deque([(s, 0)])
    while q:
        curr, dist = q.popleft()
        if curr in distances:
            continue
        distances[curr] = dist
        # push all neighbors to queue along with the distance
        q.extend([(n, dist+6) for n in graph[curr]])
    
    result = []
    for i in range(1, n+1):
        if i == s:
            continue
        result.append(distances.get(i, -1))
    return result


print(bfs(4, 2, [[1, 2], [1, 3]], 1))