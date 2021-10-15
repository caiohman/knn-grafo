from pygame_widgets import Button
from funcConfig import FuncConfig

class IaButton:

    def __init__(self, scr, name, pos):
        self.pos = pos
        self.name = name
        self.calc = len(name) * 10
        self.button = Button(
            scr,
            (600 // 2) - self.calc / 2, # x position
            (600 // 2) + (pos * 40) + (pos * 10), # y position = middle + pos * button height + (pos * gap)
            self.calc, #width
            40, #height
            text = name,
            fontSize = 20,
            textColour = (255, 255, 255),
            margin = 20,
            inactiveColour = (72, 72, 72),
            radius = 20,
            onClick = lambda: search_choice(self)
        )
        
        # config edges - 1, vertices , start node , end node
        fun_config = FuncConfig(4 , 500 , 24 , 323)

        #
        #
        #
        # BUTTOM SEARCH REDIRECT #  
        def search_choice(self):
        
            def breadth_first():
                # return True if found value and False if didn't
                result = fun_config.search.breadth_first(fun_config.knn_graph.indices , 
                 fun_config.start_node , fun_config.end_node)
                # plot data    
                fun_config.knn_graph.plot(fun_config.search.breadth_path)
                # print path array from start indice to end
                print(fun_config.search.breadth_path)
                # print True if found final number and print False if didn't
                print(result)
                
                # for test propose
                for test_time in fun_config.search.breath_time:
                    print("Time: %.6f" %test_time)

            def depth_first():
                # return True if found value and False if didn't
                result = fun_config.search.depth_first(fun_config.knn_graph.indices , 
                 fun_config.start_node , fun_config.end_node)
                # plot data    
                fun_config.knn_graph.plot(fun_config.search.depth_path)
                # print path array from start indice to end
                print(fun_config.search.depth_path)
                # print True if found final number and print False if didn't
                print(result)
                
                # for test propose
                for test_time in fun_config.search.depth_time:
                    print("Time: %.6f" %test_time)

            def best_first():
                pass

            def algorithm_a():
                pass

            def algorithm_a_s():
                # plot raw graph
                G = fun_config.knn_graph.plot([])
                # send networkx graph to astar search
                fun_config.search.algorithm_a_s(G, fun_config.start_node , fun_config.end_node)
                # plot data
                fun_config.knn_graph.plot(fun_config.search.astar_path)
                # print path array from start indice to end
                print(fun_config.search.astar_path)

                # for test propose
                for test_time in fun_config.search.astar_time:
                    print("Time: %.6f" %test_time)
                

            # dictionary with methods related to buttons
            dict = {
                0 : breadth_first , 
                1 : depth_first ,
                2 : best_first , 
                3 : algorithm_a ,
                4 : algorithm_a_s ,
            }

            dict.get(self.pos)()

        # draw buttons on screen
        self.button.draw()

    



