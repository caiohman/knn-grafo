import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from sklearn.neighbors import NearestNeighbors

class KnnGraph:

    def __init__(self, k_number, size):
        self.size = size
        self.k_number = k_number
        # chose seed to keep constant for measure propose
        np.random.seed(10)
        graph = np.random.rand(size , k_number)
        self.origin = graph
        # ball tree algorithm is based on euclidean distance 
        # metric euclidean  - sqrt(sum((x - y)^2))
        knn = NearestNeighbors(n_neighbors = k_number , algorithm = 'ball_tree' , metric='euclidean').fit(graph)
        self.distances , self.indices = knn.kneighbors(graph)
        self.sparse = knn.kneighbors_graph(graph)

    #
    #
    #
    # PRINT GRAPH INFOS #
    def print_graph(self):
        print("Distancias")
        print(self.distances)
        print("Indices")
        print(self.indices)
        print("Original")
        print(self.origin)
        print("Matriz esparsa")
        print(self.sparse)   
    
    #
    #
    #
    # PLOT GRAPH #
    def plot(self , path): 
        G = nx.Graph(self.sparse)

        node_colors = []

        # change nodes color given by path variable
        for n in G.nodes():
            if n in path:
                node_colors.append("red")
            else:
                node_colors.append("blue")    

        # choose layout and spring was the best for our project
        pos = nx.spring_layout(G)
        # add nodes with 2 colors (blue , red)
        nx.draw_networkx_nodes(G, pos = pos, node_color = node_colors , node_size = 40)
        # add edges to nodes
        nx.draw_networkx_edges(G, pos = pos)
        # add labels to help to visualize nodes index
        nx.draw_networkx_labels(G, pos = pos , font_size = 8)
        # send to screen
        plt.show()

        return G
  
