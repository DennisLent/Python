import numpy as np
import matplotlib.pyplot as plt
from GraphPrinter import PrintGraph


class Graph:
    def __init__(self, nodes, connections, directed=False):
        """
        Class to create a Graph can be directed or undirected
        :param nodes: dictionary of nodes in form {node1: [(xcord, ycord), color],...}
        :param connections: dictionary of dictionaries in form {node1: {node2: 1, node3: 2}, node2: {node3: 1},...}
        :param directed: Boolean if the graph is directed or not
        """
        self.nodes = nodes
        self.connections = connections
        self.directed = directed
        self.node_list = list(nodes.keys())

    def nodes(self):
        """
        Method to create a list of nodes
        :return: list of all nodes
        """
        return self.node_list

    def add_node(self, node_id, location, color):
        """
        Method to add a node to the graph with specific name, location and color
        :param node_id: name of node
        :param location: (xcord, ycord)
        :param color: string of color
        :return: None
        """
        self.nodes[node_id] = [location, color]
        self.connections[node_id] = {}

    def remove_node(self, node_id):
        """
        Method to remove a node based on the node name
        :param node_id: name of node
        :return: None
        """
        if node_id in self.nodes.keys():
            del self.nodes[node_id]
            del self.connections[node_id]
            for node in self.connections:
                if node_id in self.connections[node]:
                    del self.connections[node][node_id]

    def add_edge(self, begin_node, end_node, weight):
        """
        Method to add an edge between two given nodes
        :param begin_node: name of node
        :param end_node: name of node
        :param weight: edge weight
        :return: None
        """
        if begin_node in self.nodes and end_node in self.nodes:
                self.connections[begin_node][end_node] = weight
                if not self.directed:
                    self.connections[end_node][begin_node] = weight

    def remove_edge(self, begin_node, end_node):
        """
        Method to remove an edge between two given nodes
        :param begin_node: name of node
        :param end_node: name of node
        :return: None
        """
        if begin_node in self.nodes and end_node in self.nodes:
            del self.connections[begin_node][end_node]
            if not self.directed:
                del self.connections[end_node][begin_node]

    def change_edge_weight(self, begin_node, end_node, new_weight):
        """
        Method to change the edge weight between two given nodes
        :param begin_node: name of node
        :param end_node: name of node
        :param new_weight: new weight of the edge
        :return: None
        """
        if begin_node in self.nodes and end_node in self.nodes:
            self.connections[begin_node][end_node] = new_weight
            if not self.directed:
                self.connections[end_node][begin_node] = new_weight

    def is_connected(self, start=None, visited=None):
        """
        Method to check if the graph is connected (all nodes can be reached)
        :param start: starting node (None by default)
        :param visited: set of all visited nodes (None by default)
        :return: T|F
        """
        if start is None:
            start = self.node_list[0]
        if visited is None:
            visited = set()
        visited.add(start)
        if len(visited) != len(self.node_list):
            neighbors = self.connections[start].keys()
            for neighbor in neighbors:
                if neighbor not in visited:
                    if self.is_connected(neighbor, visited):
                        return True
        else:
            return True

        return False

    def is_cyclic(self, node, visited, parent=None):
        """
        Method to check if the graph is cyclic
        :param node: name of node to start with
        :param visited: set of visited nodes (should be an empty set)
        :param parent: parent of the node being visited (None by default)
        :return: T|F
        """
        visited.add(node)
        for neighbor in self.connections[node].keys():
            if neighbor not in visited:
                if self.is_cyclic(neighbor, visited, node):
                    return True
            elif parent != neighbor:
                return True
        return False

    def all_edges(self):
        """
        Method to get all edges that are present in the graph
        :return: list of all edges
        """
        edges = set()
        if self.directed:
            for begin, connection in self.connections.items():
                for end, weight in connection.items():
                    edges.add((begin, end, weight))
        else:
            for begin, connection in self.connections.items():
                for end, weight in connection.items():
                    if begin < end:
                        edges.add((begin, end, weight))
        return list(edges)

    def Kruskal(self):
        queue = sorted(self.all_edges(), key=lambda edge: edge[2])
        #print(f"THIS IS THE QUEUE {queue}")

        graph = Graph(self.nodes, {}, self.directed)
        #print(f"THESE ARE THE NODES {self.node_list}")

        while len(queue) != 0:
            con = queue[0]
            graph.add_edge(con[0], con[1], con[2])
            if graph.is_cyclic(con[0], set(), parent=None):
                graph.remove_edge(con[0], con[1])

            if graph.is_connected():
                PrintGraph(graph)
            else:
                queue.pop(0)








