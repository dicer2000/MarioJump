import pygame as pg

# Window settings
RES = WIDTH, HEIGHT = 1024, 800
FPS = 0
IMG_FOLDER = "./images"
IMG_URL = ""
GROUND_LEVEL = 500
IMG_REFRESH = 250
GRAVITY = 1.25

# User Defined Events
FLIP_IMAGE = pg.USEREVENT + 1

# Mario Character
MARIO_HEIGHT = 70
MARIO_WIDTH = 80

# Mario Events
STOPPED_R = 0
IN_AIR_R = 1
LANDED_R = 2
JUMPING_R = 3
WALK_R = 4

# Mario Key Frames - [X,Y]
MKF = [
        [[0,1]],
        [[3,1]],
        [[4,1]],
        [[3,1]],
        [[1,1],[2,1],[1,1],[0,1]]
]