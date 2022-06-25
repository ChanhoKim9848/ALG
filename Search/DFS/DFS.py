# referenced from: https://www.youtube.com/watch?v=7C9RgOcvkvo
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

def dfs(graph, current_node, visited):
    # 현재 노드를 방문처리
    # current node is visited
    visited[current_node] = True
    # 현재 방문처리된 노드를 출력
    # print the current node
    print(current_node, end=" ")

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    # current node visit to next node recursively
    for next_node in graph[current_node]:
        if not visited[next_node]:
            dfs(graph, next_node,visited)

# Testing
# 각 노드가 방문된 정보를 표현
# initialize visited list that shows if each node is visited, 
visited=[False]*len(graph)
dfs(graph,1,visited)
            


