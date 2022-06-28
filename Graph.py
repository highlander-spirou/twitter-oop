from typing import Dict, Tuple, List, Union, NewType
from queue import Queue
from functools import lru_cache

Edge = NewType('Edge', Tuple[str, str])
Edges = NewType('Edges', List[Tuple[str, str]])

class Graph:
    def __init__(self):
        self.edges = []
        self.graph_dict:Dict[str, set] = {}
        self.graph_queue = Queue()
        
    def map_edges(self, start, stop):
        if start in self.graph_dict:
            self.graph_dict[start].add(stop)
        else:
            self.graph_dict[start] = {stop}
    
    def construct_graph_dict(self):
        if self.graph_queue.qsize() > 0:
            for i in range(self.graph_queue.qsize()):
                current_edge = self.graph_queue.get()
                self.map_edges(current_edge[0], current_edge[1])
                
    def add_edge(self, edge:Union[Edge, Edges]):
        if type(edge) == list:
            self.edges.extend(edge)
            for i in edge:
                self.graph_queue.put(i)
        else:
            self.edges.append(edge)
            self.graph_queue.put(edge)
        self.construct_graph_dict()
        
    def get_connected_node(self, name):
        return self.graph_dict.get(name)
    
    @lru_cache(maxsize=None)
    def get_connected_to_node(self, name) -> set:
        """
        Runs an iterative node checking, returns all nodes that connected (point to) "name" node
        """
        nodes = set()
        for index, value in self.graph_dict.items():
            if name in value:
                nodes.add(index)
                
        return nodes

    def remove_edge(self, start, stop) -> str:
        if start in self.graph_dict:
            if stop in self.graph_dict[start]:
                self.graph_dict[start].remove(stop)
                return stop
   
   
   
if __name__ == '__main__':
    routes = [('a', 'b'), ('b', 'c'), ('c', 'd')]
    route = ('a', 'e')


    graph = Graph()
    graph.add_edge(Edges(routes))
    graph.add_edge(Edge(route))
    print(graph.graph_dict)

    new_route = ('e', 'd')
    graph.add_edge(Edge(new_route))
    print(graph.graph_dict)

    conflict_route = ('c', 'd')
    graph.add_edge(Edge(conflict_route))
    print(graph.graph_dict)
    
    print(graph.edges)

    print(graph.get_connected_to_node('d'))
    print(graph.get_connected_to_node('a'))
    print(graph.get_connected_to_node('d'))