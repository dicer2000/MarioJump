import pygame as pg

# Window settings
RES = WIDTH, HEIGHT = 1024, 800
FPS = 120
IMG_FOLDER = "./images"
IMG_URL = ""
GROUND_LEVEL = HEIGHT - 100
IMG_REFRESH = 250
GRAVITY = 1.05
LEFT  = 0
RIGHT = 1

# User Defined Events
FLIP_IMAGE = pg.USEREVENT + 1

# Mario Character
MARIO_HEIGHT = 70
MARIO_WIDTH = 80
MARIO_WALK_SPEED = 3.0
MARIO_RUN_SPEED = 5.0
MARIO_WALK_JUMP_VEL = 15.0
MARIO_RUN_JUMP_VEL = 21.0

# Mario Events
MARIO_STOPPED = 0
MARIO_IN_AIR = 1
MARIO_LANDED = 2
MARIO_JUMPING = 3
MARIO_WALK = 4
MARIO_RUN = 5

# Mario Key Frames - [X,Y]
MKF = [
       [ [[4,2]], [[0,1]] ], # Mario Stopped
       [ [[1,2]], [[3,1]] ], # Mario In Air
       [ [[1,1]], [[4,1]] ], # Mario Landed
       [ [[1,2]], [[3,1]] ], # Mario Jumping
       [ [[3,2], [4,2]], [[1,1], [0,1]] ], #Mario Walking
       [ [[3,2], [4,2]], [[1,1], [0,1]] ]  #Mario Running
]