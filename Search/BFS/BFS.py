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

from collections import deque 
def bfs(graph, start_node, visited):
    # 큐를 사용하기위해 데크 라이브러리를 사용
    # to implement Queue, we import deque library
    # initialize queue with the start node
    queue = deque([start_node])

    # 현재 노드 방문처리
    # current node is visited (True)
    visited[start_node] = True

    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        # get the new node from the queue and print it
        new_node = queue.popleft()
        print(new_node, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입하고 방문처리
        # the nodes that haven't been are inserted in the queue and make them visited
        for node in graph[new_node]:
            if not visited[node]:
                queue.append(node)
                visited[node]=True

# Testing

# 각 노드가 방문된 정보를 표현
# initialize visited list that shows if each node is visited, 
visited=[False]*len(graph)

bfs(graph, 1, visited)


