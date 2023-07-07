import networkx as nx
# Function to draw graphs
# nx.draw() does not display the weights
import matplotlib.pyplot as plt


def plot_graph(G, pos_nodes, **kwargs):
    # get optional arguments **kwargs
    if "node_size" in kwargs:
        node_size = kwargs["node_size"]
    else:
        node_size = 50

    if "show_node_id" in kwargs:
        show_node_id = kwargs["show_node_id"]
    else:
        show_node_id = True

    if "show_node_attributes" in kwargs:
        show_node_attributes = kwargs["show_node_attributes"]
    else:
        show_node_attributes = False

    if "show_edge_weights" in kwargs:
        show_edge_weights = kwargs["show_edge_weights"]
    else:
        show_edge_weights = False

    if "show_edge_attributes" in kwargs:
        show_edge_attributes = kwargs["show_edge_attributes"]
    else:
        show_edge_attributes = False

    # plot basic graph
    try:
        node_colorlist = []
        for node in G.nodes:
            gender = G.nodes[node]["gender"]
            if gender == "M":
                node_colorlist.append("blue")
            elif gender == "F":
                node_colorlist.append("pink")
            else:
                node_colorlist.append("grey")
        edge_colorlist = []
        for edge in G.edges():
            linetype = G.edges[edge]["line"]
            if linetype == "dot":
                edge_colorlist.append("red")
            else:
                edge_colorlist.append("black")
    except:
        node_colorlist = "blue"
        edge_colorlist = "grey"
    nx.draw(G, pos_nodes, with_labels=False,
            node_size=node_size, node_color=node_colorlist,
            edge_color=edge_colorlist, arrowsize=30)

    pos_attrs = {}
    for node, coords in pos_nodes.items():
        pos_attrs[node] = (coords[0], coords[1])
    if show_node_id:
        nx.draw_networkx_labels(G, pos_attrs, font_family="serif", font_size=10)

    # plot attributes of nodes
    if show_node_attributes:
        # pos_attrs = {}
        node_attributes = {}
        for node, coords in pos_nodes.items():
            #    pos_attrs[node] = (coords[0], coords[1])
            node_attributes[node] = G.nodes[node]
        # nx.draw_networkx_labels(G, pos_attrs, font_family="serif", font_size=10)
        nx.draw_networkx_labels(G, pos_nodes, node_attributes, font_size=8, bbox={"ec": "k", "fc": "white", "alpha": 0.7})

    # plot weights of edges
    if show_edge_weights:
        # pos_attrs = {}
        # for node, coords in pos_nodes.items():
        #    pos_attrs[node]=(coords[0], coords[1])
        nx.draw_networkx_labels(G, pos_attrs, font_family="serif", font_size=10)
        edge_labels = dict([((a, b,), d["weight"]) for a, b, d in G.edges(data=True)])
        nx.draw_networkx_edge_labels(G, pos_nodes, edge_labels=edge_labels, rotate=False)

    # plot attributes of edges
    if show_edge_attributes:
        edge_attributes = {}
        for edge in G.edges:
            #    pos_attrs[node] = (coords[0], coords[1])
            edge_attributes[edge] = G.edges[edge]
        nx.draw_networkx_edge_labels(G, pos_nodes, edge_labels=edge_attributes, rotate=False)

    plt.axis('off')
    axis = plt.gca()
    axis.set_xlim([1.2 * x for x in axis.get_xlim()])
    axis.set_ylim([1.2 * y for y in axis.get_ylim()])