from knnGraph import KnnGraph
from searchAlgorithm import SearchAlgorithm

#  
# 
#
# CONFIG CLASS #
class FuncConfig:

    def __init__(self , edges , vertices , start_node , end_node):
        # initialize search object
        self.search = SearchAlgorithm()
        # choose graph edge number and number of nodes (must be incremented by 1 - so if it is 3 - I need 4)
        self.knn_graph = KnnGraph(edges , vertices)

        # start and end indices to search
        self.start_node = start_node
        self.end_node = end_node                