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


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))
result=list(bfs_paths(graph, 'malvan', 'dodamarg'))
print("Whole path:\n",result)


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None
result1=shortest_path(graph, 'malvan', 'dodamarg')
print("Shortest path:\n",result1)

