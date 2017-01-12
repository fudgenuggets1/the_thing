import pygame, Functions
from yo_buttons import Button

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 200)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
LIGHT_PURPLE = (255, 0, 255)
ORANGE = (220, 120, 0)
YELLOW = (200, 200, 0)
BRIGHT_YELLOW = (255, 255, 0)
BRIGHT_ORANGE = (255, 155, 0)
BRIGHT_GREEN = (0, 255, 0)
BRIGHT_BLUE = (0, 0, 255)
BRIGHT_RED = (255, 0, 0)
DARK_RED = (139, 0, 0)
DODGER_BLUE = (44, 144, 255)
BRIGHT_SNOW_WHITE = (228, 223, 223)
SNOW_WHITE = (205, 201, 201)
MAROON = (128, 0, 0)
SKY_BLUE = (135, 206, 235)
LIGHT_SKY_BLUE = (135, 206, 250)
PURPLE = (148, 0, 211)
TAN = (210, 180, 140)
BURLY_WOOD = (222, 184, 135)
DEEP_PINK = (255, 20, 147)
HOT_PINK = (255, 105, 180)
TOMATO = (200, 100, 100)
TOMATO_GREEN = (100, 200, 100)
GRAY = (128, 128, 128)


class Block(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color=BLUE):
        """ Constructor function """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Make a block, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.width = width
        self.height = height

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.x = x
        self.y = y


class Visible(object):

    def __init__(self):

        self.Button_List = []
        self.Block_List = pygame.sprite.Group()

        blocks = [
            [0, 0, 2, 480],
            [0, 0, 640, 2],
            [638, 0, 2, 480],
            [0, 478, 640, 2]
        ]

        for item in blocks:
            block = Block(item[0], item[1], item[2], item[3])
            self.Block_List.add(block)


class Home_Screen(Visible):

    def __init__(self):

        Visible.__init__(self)

        buttons = [
            ["Team Builder", 225, 75, 190, 50, BLUE, BRIGHT_BLUE, 1],
            ["Play", 225, 225, 190, 50, RED, BRIGHT_RED, 2],
            ["Change Teams", 225, 375, 190, 50, GREEN, BRIGHT_GREEN, 3],
            ["Gym Leaders", 450, 225, 160, 50, ORANGE, BRIGHT_ORANGE, 4],
        ]

        for item in buttons:
            button = Button(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
            self.Button_List.append(button)


class Team_Builder_Screen(Visible):

    def __init__(self):

        Visible.__init__(self)

        blocks = [

        ]

        buttons = [

            ["Exit", 590, 450, 45, 25, RED, BRIGHT_RED, 0],
            ["-", 480, 142, 15, 15, GREEN, BRIGHT_GREEN, "-health"],
            ["+", 535, 142, 15, 15, GREEN, BRIGHT_GREEN, "+health"],
            ["-", 480, 202, 15, 15, GREEN, BRIGHT_GREEN, "-attack"],
            ["+", 535, 202, 15, 15, GREEN, BRIGHT_GREEN, "+attack"],
            ["-", 480, 262, 15, 15, GREEN, BRIGHT_GREEN, "-defense"],
            ["+", 535, 262, 15, 15, GREEN, BRIGHT_GREEN, "+defense"],
            ["-", 480, 322, 15, 15, GREEN, BRIGHT_GREEN, "-special_attack"],
            ["+", 535, 322, 15, 15, GREEN, BRIGHT_GREEN, "+special_attack"],
            ["-", 480, 382, 15, 15, GREEN, BRIGHT_GREEN, "-special_defense"],
            ["+", 535, 382, 15, 15, GREEN, BRIGHT_GREEN, "+special_defense"],
            ["-", 480, 442, 15, 15, GREEN, BRIGHT_GREEN, "-speed"],
            ["+", 535, 442, 15, 15, GREEN, BRIGHT_GREEN, "+speed"],
            ["<", 5, 80, 20, 20, GREEN, BRIGHT_GREEN, "<move1"],
            [">", 300, 80, 20, 20, GREEN, BRIGHT_GREEN, ">move1"],
            ["<", 5, 180, 20, 20, GREEN, BRIGHT_GREEN, "<move2"],
            [">", 300, 180, 20, 20, GREEN, BRIGHT_GREEN, ">move2"],
            ["<", 5, 280, 20, 20, GREEN, BRIGHT_GREEN, "<move3"],
            [">", 300, 280, 20, 20, GREEN, BRIGHT_GREEN, ">move3"],
            ["<", 5, 380, 20, 20, GREEN, BRIGHT_GREEN, "<move4"],
            [">", 300, 380, 20, 20, GREEN, BRIGHT_GREEN, ">move4"],
            ["<", 55, 30, 20, 20, GREEN, BRIGHT_GREEN, "previous"],
            [">", 325, 30, 20, 20, GREEN, BRIGHT_GREEN, "next"],
            ["previous", 150, 4, 100, 20, GREEN, BRIGHT_GREEN, "up"],
            ["next", 150, 54, 100, 20, GREEN, BRIGHT_GREEN, "down"]

        ]

        for item in blocks:
            block = Block(item[0], item[1], item[2], item[3], item[4])
            self.Block_List.add(block)

        for item in buttons:
            button = Button(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
            self.Button_List.append(button)


class Play_Screen(Visible):

    def __init__(self):

        Visible.__init__(self)

        blocks = [
            [10, 10, 200, 125, TOMATO],
            #[10, 10, 2, 125, RED],
            #[10, 135, 250, 2, RED],
            #[260, 10, 2, 127, RED],
            [430, 230, 200, 125, TOMATO_GREEN],
            #[380, 230, 2, 125, GREEN],
            #[630, 230, 2, 127, GREEN],
            #[380, 355, 250 ,2, GREEN],
            [0, 364, 640, 2, BLUE],
            [0, 421, 510, 2, BLUE],
            [510, 365, 2, 115, BLUE],
            [255, 365, 2, 115, BLUE],
            #[50, 65, 110, 12, RED],
            #[470, 290, 110, 12, RED],
        ]

        buttons = [
            ["Exit", 900, 450, 45, 25, RED, BRIGHT_RED, 0],
            ["OK", 520, 370, 75, 30, BLUE, BRIGHT_BLUE, "ok"],
            ["Party", 520, 410, 75, 30, GREEN, BRIGHT_GREEN, "party"],
            [" ", 2, 366, 253, 55, ORANGE, BRIGHT_ORANGE, "move1"],
            [" ", 2, 423, 253, 55, ORANGE, BRIGHT_ORANGE, "move3"],
            [" ", 257, 366, 253, 55, ORANGE, BRIGHT_ORANGE, "move2"],
            [" ", 257, 423, 253, 55, ORANGE, BRIGHT_ORANGE, "move4"],
            ["<", 700, 25, 30, 30, GREEN, BRIGHT_GREEN, "previous_turn"],
            [">", 875, 25, 30, 30, GREEN, BRIGHT_GREEN, "next_turn"]
        ]

        for item in blocks:
            block = Block(item[0], item[1], item[2], item[3], item[4])
            self.Block_List.add(block)

        for item in buttons:
            button = Button(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
            self.Button_List.append(button)


class Options_Screen(Visible):

    def __init__(self):
        Visible.__init__(self)

        buttons = [
            ["Exit", 590, 450, 45, 25, RED, BRIGHT_RED, 0],
            ["New Team", 50, 350, 200, 30, GREEN, BRIGHT_GREEN, "new_team"],
            ["Random Team", 25, 400, 250, 30, GREEN, BRIGHT_GREEN, "random_team"],
            ["New Opponent", 390, 350, 200, 30, GREEN, BRIGHT_GREEN, "new_opponent"],
            ["Random Opponent", 365, 400, 250, 30, GREEN, BRIGHT_GREEN, "random_opponent"],
        ]

        for item in buttons:
            button = Button(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
            self.Button_List.append(button)

class Gym_Leaders_Screen(Visible):

    def __init__(self):
        Visible.__init__(self)

        buttons = [
            ["Exit", 590, 450, 45, 25, RED, BRIGHT_RED, 0],
            ["Normal", 50, 75, 160, 30, SNOW_WHITE, BRIGHT_SNOW_WHITE, "normal"],
            ["Fight", 50, 115, 160, 30, DARK_RED, MAROON, "fight"],
            ["Ice", 50, 155, 160, 30, SKY_BLUE, LIGHT_SKY_BLUE, "ice"],
            ["Poison", 50, 195, 160, 30, PURPLE, LIGHT_PURPLE, "poison"],
            ["Ground", 50, 235, 160, 30, TAN, BURLY_WOOD, "ground"],
            ["Fire", 50, 275, 160, 30, RED, BRIGHT_RED, "fire"],
            ["Psychic", 50, 315, 160, 30, DEEP_PINK, HOT_PINK, "psychic"],
            ["Grass", 50, 355, 160, 30, GREEN, BRIGHT_GREEN, "grass"],
            ["Electric", 50, 395, 160, 30, YELLOW, BRIGHT_YELLOW, "electric"],

        ]

        for item in buttons:
            button = Button(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
            self.Button_List.append(button)
