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
    
    print("graph", graph.vertices)

