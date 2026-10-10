from collections import deque
graph1= {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}
graph2={'1':['2','3'],
       '2':['4','5'],
       '3':[],
       '4':['5'],
       '5':[]}
graph3={'1':['2','7'],
       '2':['3','6'],
       '3':['4','5'],
       '4':[],
       '5':[],
       '6':[],
       '7':['8','10'],
       '8':['9'],
       '9':[],
       '10':[]}
graph4= {
    '0': ['1'],
    '1': ['0', '2', '3'],
    '2': ['1'],
    '3': ['1',' 4'],
    '4': ['3', '6', '5'],
    '5': ['4', '7'],
    '6': ['4', '7'],
    '7': ['5', '6']
}
def bfs(graph,start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return visited
b="y"
while b=="Y" or b=="y":
   a=int(input("for which graph u want the bfs path?"))
   if a==1:
    graph=graph1
   elif a==2:
    graph=graph2
   elif a==3:
    graph=graph3
   elif a==4:
    graph=graph4
   else:
    print("choose from 1-4 option")
    continue
   start=next(iter(graph))
   if start not in graph:
       print("invalid starting node:")
   else:
       print("BFS PATH:","->".join(bfs(graph,start)))
   b=input("do you want to continue?(y/n):")
