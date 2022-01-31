import Graph
from GraphPrinter import PrintGraph


nodes = {"v1": [(0,0), "green"],
         "v2": [(1,1), "blue"],
         "v3": [(2,0), "black"],
         "v4": [(0,-4), "pink"],
         "v5": [(-1,0), "yellow"],
         "v6": [(3,3), "brown"],
         "v7": [(2.5, 3), "orange"],
         }
connections = {"v1": {"v2": 1},
               "v2": {"v3": 1, "v4": 2},
               "v3": {"v4": 2, "v7": 3},
               "v4": {"v5": 4},
               "v5": {"v2": 1},
               "v7": {"v6": 2}
               }

my_graph = Graph.Graph(nodes, connections, True)
print(f"Is the graph connected? {my_graph.is_connected()}")
print(f"Is the graph cyclic? {my_graph.is_cyclic('v1', set())}")
print(f"All connections of the graph: {my_graph.all_edges()}")
PrintGraph(my_graph)
my_graph.Kruskal()