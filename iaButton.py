from pygame_widgets import Button

class IaButton:

    def __init__(self, scr, name, pos):
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
            onClick = lambda: print('Click')
        )

        self.button.draw()