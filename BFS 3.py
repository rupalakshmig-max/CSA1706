from collections import deque
graph={'1':['2','7'],
       '2':['3','6'],
       '3':['4','5'],
       '4':[],
       '5':[],
       '6':[],
       '7':['8','10'],
       '8':['9'],
       '9':[],
       '10':[]}
def bfs(start):
    visited=[]
    queue=deque([start])
    while queue:
        node=queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited
print("BFS:","->".join(bfs('1')))
