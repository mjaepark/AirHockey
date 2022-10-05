import constants as const
import pygame
import os

auxDirectory = os.path.join(os.path.dirname(__file__), 'assets')

smallfont = None
score1, score2 = 0, 0

# Sound globals.
paddleHit = None
goal_whistle = None
backgroundMusic = None

# image for mute and unmute
mute_image = pygame.image.load(os.path.join(auxDirectory, 'mute.png'))
unmute_image = pygame.image.load(os.path.join(auxDirectory, 'unmute.png'))

play_image = pygame.image.load(os.path.join(auxDirectory, 'play.png'))
pause_image = pygame.image.load(os.path.join(auxDirectory, 'pause.png'))

info_image = pygame.image.load(os.path.join(auxDirectory, "info.png"))

WnB = [(30, 30, 30), (255, 255, 255)]

# game globals.
clock = None
screen = None

# width and height of the screen.
width, height = const.WIDTH, const.HEIGHT

# button constants
buttonRadius = 60
squareSide = 80

# color globals
# (dimgreen, green) , (dimred, red) , (dimblue, blue ) , (yellow, dimyellow), (orange, dimorange)
colors = [[(46, 120, 50), (66, 152, 60)], [(200, 72, 72), (255, 92, 92)],
          [(0, 158, 239), (100, 189, 219)], [(221, 229, 2), (252, 255, 59)],
          [(232, 114, 46), (244, 133, 51)]]

#   green pink red blue
theme_colors = [[(20, 228, 49), (20, 228, 49)], [(229, 21, 212), (229, 21, 212)],
                [(228, 20, 20), (228, 21, 21)], [(50, 64, 209), (45, 64, 209)]]
green = pygame.image.load("assets/bb_g.jpeg")
pink = pygame.image.load("assets/bb_p.jpeg")
red = pygame.image.load("assets/bb_r.jpeg")
blue = pygame.image.load("assets/bb_b.jpeg")
theme_img = [green, pink, red, blue]
small_g = pygame.transform.scale(green, (300, 150))
small_p = pygame.transform.scale(pink, (300, 150))
small_r = pygame.transform.scale(red, (300, 150))
small_b = pygame.transform.scale(blue, (300, 150))

small_img = [small_g, small_p, small_r, small_b]