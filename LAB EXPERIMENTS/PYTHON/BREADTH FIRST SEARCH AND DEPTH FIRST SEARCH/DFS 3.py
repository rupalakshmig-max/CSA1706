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
def dsf(start,visited=None):
    if visited is NONE:
        visited=[]
        visited.append(start)
        for node in graph(start):
            if 
