import matplotlib.pyplot as plt

def PrintGraph(graph):

    """
    Method of visualize the graph created
    :return: plot of the graph
    """
    min_xval, max_xval = 0, 0
    min_yval, max_yval = 0, 0
    if not graph.directed:
        for node in graph.nodes:
            name = node
            location, color = graph.nodes[node]
            if location[0] < min_xval:
                min_xval = location[0]
            if location[0] > max_xval:
                max_xval = location[0]
            if location[1] < min_yval:
                min_yval = location[1]
            if location[1] > max_yval:
                max_yval = location[1]
            plt.scatter(location[0], location[1], color=color)
            plt.text(location[0], location[1] + 0.01, f"{name}")
        for begin_node, destinations in graph.connections.items():
            for end_node, weight in destinations.items():
                begin_x, begin_y = graph.nodes[begin_node][0]
                end_x, end_y = graph.nodes[end_node][0]
                plt.plot([begin_x, end_x], [begin_y, end_y], color="red")
                avg_x, avg_y = (begin_x + end_x) / 2 + 0.01, (begin_y + end_y) / 2 + 0.01
                plt.text(avg_x, avg_y, f"{weight}")
    else:
        for node in graph.nodes:
            name = node
            location, color = graph.nodes[node]
            if location[0] < min_xval:
                min_xval = location[0]
            if location[0] > max_xval:
                max_xval = location[0]
            if location[1] < min_yval:
                min_yval = location[1]
            if location[1] > max_yval:
                max_yval = location[1]
            plt.scatter(location[0], location[1], color=color)
            plt.text(location[0], location[1] + 0.01, f"{name}")
        for begin_node, destinations in graph.connections.items():
            for end_node, weight in destinations.items():
                begin_x, begin_y = graph.nodes[begin_node][0]
                end_x, end_y = graph.nodes[end_node][0]
                dx, dy = end_x-begin_x, end_y-begin_y
                plt.arrow(begin_x, begin_y, dx, dy, color="red", length_includes_head=True, width=0.01)
                avg_x, avg_y = (begin_x + end_x) / 2 + 0.01, (begin_y + end_y) / 2 + 0.01
                plt.text(avg_x, avg_y, f"{weight}")
    plt.show()