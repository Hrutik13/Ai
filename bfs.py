graph={
        'malvan': set(['devgad','vengurla','kankavli','kudal']),
        'kudal':set(['kankavli','malvan','sawantwadi','vengurla']),
         'vengurla':set(['malvan','sawantwadi','kudal']),
         'kankavli':set(['devgad','malvan','kudal','vaibhavwadi']),
         'devgad':set(['kankavli','malvan']),
         'vaibhavwadi':set(['kankavli']),
         'sawantwadi':set(['dodamarg','kudal','vengurla']),
         'dodamarg':set(['sawantwadi'])
    }
visited=[]
queue=[]

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end="->")


        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("following is the breadth first search")
bfs(visited,graph,'dodamarg')
