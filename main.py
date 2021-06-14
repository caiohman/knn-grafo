import pygame
import os

#
#
#
# LOAD IMAGE #

def load_image(image_name, p):
    image_path = os.path.join("assets" , image_name)
    try:
        image = p.image.load(image_path).convert()
        return image, image.get_rect()
    except p.error:
        print("Problema ao carregar imagem")

#
#
#
# CONFIG SCREEN #
def configScreen():
    #init 
    pygame.init()
    #create the screen
    scr = pygame.display.set_mode((600 , 600))
    #title
    pygame.display.set_caption("TRABALHO IA")
    #screen color
    scr.fill("red")
    image = load_image("logo.png" , pygame)
    scr.blit(image[0], image[1])
    pygame.display.flip()

    return pygame  

#
#
#
# GAME LOOP #
def game_loop():
    p = configScreen()
    
    running = True
    #game loop
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False

#
#
#
# MAIN FUNCTION #

if __name__ == "__main__":
    game_loop()