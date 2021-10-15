import queue
import time
import networkx as nx

class SearchAlgorithm:

    def __init__(self):
        self.breadth_path = []
        self.depth_path = []
        self.astar_path = []
        self.breath_time = []
        self.depth_time = []
        self.astar_time = []

    #
    #
    #
    # BREADTH FIRST SEARCH #    
    def breadth_first(self , graph , start_point , final_point):
        # define which measurement it is
        actual = len(self.breath_time)
        # initial time to measure
        self.breath_time.append(time.time())
        
        queue = []
        self.breadth_path.append(start_point)
        queue.append(start_point)

        while(queue):
            vertex_index = queue.pop(0)

            for vertex_descent in graph[vertex_index]:
               
                if vertex_descent not in self.breadth_path:
                    self.breadth_path.append(vertex_descent)
                    queue.append(vertex_descent)

                if vertex_descent == final_point:
                    self.breath_time[actual] = time.time() - self.breath_time[actual] #calcule algorithm time
                    return True # it could find     

        self.breath_time[actual] = time.time() - self.breath_time[actual] #calcule algorithm time
        return False # it couldn't find

    #
    #
    #
    # DEPTH FIRST SEARCH # 
    def depth_first(self , graph , start_point , final_point):
        # define which measurement it is
        actual = len(self.depth_time)
        # initial time to measure
        self.depth_time.append(time.time())
        
        stack = []
        self.depth_path.append(start_point)
        stack.append(start_point)

        while(stack):
            vertex_index = stack.pop()

            for vertex_descent in graph[vertex_index]:
                
                if vertex_descent not in self.depth_path:
                    self.depth_path.append(vertex_descent)
                    stack.append(vertex_descent)
        
                if vertex_descent == final_point:
                    self.depth_time[actual] = time.time() - self.depth_time[actual] #calcule algorithm time
                    return True
        
        self.depth_time[actual] = time.time() - self.depth_time[actual] #calcule algorithm time
        return False 


    #
    #
    #
    # A* ALGORITHM SEARCH # 
    def algorithm_a_s(self , graph , start_point , final_point):
        # define which measurement it is
        actual = len(self.astar_time)
        # initial time to measure
        self.astar_time.append(time.time())

        self.astar_path = nx.astar_path(graph , source = start_point , target = final_point)
        
        self.astar_time[actual] = time.time() - self.astar_time[actual] #calcule algorithm time



