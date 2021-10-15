import pygame
import os
from iaButton import IaButton
from knnGraph import KnnGraph

#
#
#
# LOAD IMAGE #
def load_image(image_name, p):
    image_path = os.path.join("assets" , image_name)
    try:
        image = p.image.load(image_path)
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
    width, height = 600 , 600 
    scr = pygame.display.set_mode((width , height))
    #title
    pygame.display.set_caption("TRABALHO IA")
    #screen color
    scr.fill("gray")
    image , rect = load_image("logo.png" , pygame)
    rect.center = width // 2 , (height // 2) - 100
    scr.blit(image, rect)

    buttons = []

    buttons.append(IaButton(scr, 'Busca Largura', 0))
    buttons.append(IaButton(scr, 'Busca Profundidade', 1))
    buttons.append(IaButton(scr, 'Busca Best First', 2))
    buttons.append(IaButton(scr, 'Agoritmo A', 3))
    buttons.append(IaButton(scr, 'Algoritmo A*', 4))
    
    pygame.display.flip()

    return pygame , buttons  

#
#
#
# GAME LOOP #
def game_loop():
    pGame , buttons = configScreen()

    running = True
    #game loop
    while running:
        for event in pGame.event.get():
            if event.type == pGame.QUIT:
                running = False
            
            # buttons event listeners
            buttons[0].button.listen(event)
            buttons[1].button.listen(event)
            buttons[2].button.listen(event)
            buttons[3].button.listen(event)
            buttons[4].button.listen(event)

#
#
#
# MAIN FUNCTION #

if __name__ == "__main__":
    game_loop()