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
def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n, visited)
            return visited
visited = dfs(graph,'malvan', [])
print(visited)
