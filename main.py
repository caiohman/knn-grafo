import pygame

def configScreen():
    #init 
    pygame.init()
    #create the screen
    scr = pygame.display.set_mode((600 , 600))
    #title
    pygame.display.set_caption("TRABALHO IA")
    #screen color
    scr.fill("red")
    pygame.display.flip()

    return pygame  

#def firstPage():
        


#
#
#
# MAIN FUNCTION  #

if __name__ == "__main__":
    p = configScreen()

    running = True
    #game loop
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False