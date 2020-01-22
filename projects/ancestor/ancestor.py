from util import Stack, Queue
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    #ancestors will be a list of tuples?
    # print("ancestor print", ancestors)
    graph = Graph()
    for ancestor in ancestors:
        if ancestor[0] not in graph.vertices:
            graph.add_vertex(ancestor[0])
        if ancestor[1] not in graph.vertices:
            graph.add_vertex(ancestor[1])
        # print("parent", ancestor[0], "child", ancestor[1])
        graph.add_edge(ancestor[1], ancestor[0])

    #if no "parent" then return -1
    if graph.vertices[starting_node] == set():
        return -1
    else:
        queue = Queue()

        queue.enqueue([starting_node])
        
        visited = set()
        oldest_ancestor = starting_node
        current_length = 0

        while queue.size() > 0:
            path = queue.dequeue()
            vertex = path[-1]
            if vertex not in visited:
                if graph.vertices[vertex] == set():
                    if vertex > oldest_ancestor and len(path) == current_length:
                        pass
                    else:
                        current_length = len(path)
                        oldest_ancestor = path[-1]
            visited.add(vertex)

            for next_vert in graph.get_neighbors(vertex):
                new_path = list(path)
                new_path.append(next_vert)
                queue.enqueue(new_path)
        if oldest_ancestor == starting_node:
            return None
        else:
            return oldest_ancestor

