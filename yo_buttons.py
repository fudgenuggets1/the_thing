import pygame, Functions, random, time
pygame.font.init()

class Button():

    List = []
    time = time.time()

    def __init__(self, msg, x, y, w, h, color, highlight, action):

        self.msg = msg
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.regular_color, self.highlight_color = color, highlight
        self.action = action
        self.color = self.regular_color
        self.mouse_on = False
        Button.List.append(self)

    @staticmethod
    def update(screen, list):

        for button in list:
            pygame.draw.rect(screen, button.color, (button.x, button.y, button.w, button.h))
            x = button.w / 2
            y = button.h / 2
            Functions.text_to_screen(screen, button.msg, button.x+x, button.y+y, 20)

    def mouse_over(self):
        self.color = self.highlight_color
        self.mouse_on = True
    def mouse_off(self):
        self.color = self.regular_color
        self.mouse_on = False
    @staticmethod
    def clear_list():
        Button.List[:] = []
    def do_action(self):

        from game import Game
        if self.action == "single_player":    
            Game.playing = True
            Button.clear_list()
            Game.restart()



