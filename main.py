
#  /\_/\  Mario Jump
# ( o o ) Programming Project
#  =( )=  Spring 2023
#   ~*~   (Cat by ChatGPT)

import pygame as pg
import sys
from settings import *

# Main game object
class Game:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def load_sprite_sheet(self):
        # Load the sprite sheet once for entire game.  Double its size to make playable
        try:
            img_load = pg.image.load(IMG_FOLDER + "/mariosheet.gif")
            self.sprite_sheet = pg.transform.scale(img_load, (img_load.get_width()*2,img_load.get_height()*2)) # Make img 2X bigger
        except:
            print("Could not load sprite sheet")


    def new_game(self):
        # Create a new game
        self.load_sprite_sheet()
        self.current_image = 0
        self.movey = self.movex = 0
        self.mario_pos_x = 50
        self.mario_pos_y = 100
        self.mario_x_move = 5.0
        self.mario_y_move = -10.0
        self.mario_dir = RIGHT
        pg.time.set_timer(FLIP_IMAGE, IMG_REFRESH)

    def update(self):
        # Update the game physics
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'Sluggo Mario - {self.clock.get_fps():.1f}')

        ###### Set the states ######
        if self.mario_pos_y+MARIO_HEIGHT < GROUND_LEVEL:
            self.mario_state = MARIO_IN_AIR
            self.mario_y_move += GRAVITY
            self.current_image = 0
        elif self.mario_state == MARIO_IN_AIR and self.mario_pos_y+MARIO_HEIGHT >= GROUND_LEVEL:
            self.mario_state = MARIO_LANDED
            self.mario_x_move = 0
            self.mario_y_move = 0
        elif self.mario_state == MARIO_STOPPED:
            self.mario_x_move = 0
            self.mario_y_move = 0
        elif self.mario_state == MARIO_LANDED:
            self.mario_state = MARIO_STOPPED
            self.mario_x_move = 0
            self.mario_y_move = 0
        elif self.mario_state == MARIO_JUMPING:
            self.mario_y_move -= MARIO_WALK_JUMP_VEL
            self.mario_state == MARIO_IN_AIR
            self.current_image = 0
        elif self.mario_state == MARIO_WALK:
            if self.mario_dir == LEFT:
                self.mario_x_move = MARIO_WALK_SPEED * -1
            else:
                self.mario_x_move = MARIO_WALK_SPEED
        elif self.mario_state == MARIO_RUN:
            if self.mario_dir == LEFT:
                self.mario_x_move = MARIO_RUN_SPEED * -1
            else:
                self.mario_x_move = MARIO_RUN_SPEED

        ###### End Setting states ######

        self.mario_pos_x += self.mario_x_move
        self.mario_pos_y += self.mario_y_move
        # Keep from edge of the screen
        if self.mario_pos_x < 1:
            self.mario_pos_x = 1
        if self.mario_pos_x+MARIO_WIDTH > WIDTH-1:
            self.mario_pos_x = WIDTH-MARIO_WIDTH-1

        if self.mario_pos_y + MARIO_HEIGHT > GROUND_LEVEL:
            self.mario_pos_y = GROUND_LEVEL-MARIO_HEIGHT


    def draw(self):
        # Draw to the main Screen
        self.screen.fill('black')

        # Draw the current Mario
        self.drawMario()

        # Draw the ground layer
        pg.draw.rect(self.screen,pg.Color(75, 245, 66),(0,GROUND_LEVEL,WIDTH,HEIGHT-GROUND_LEVEL))

        # Drawn screen to forefront
        pg.display.update()            

    def drawMario(self):
        # Draw Mario himself from sprites
        # Get all frames of current state
        mario_current_frames = MKF[self.mario_state]
        
        # Get the direction of Mario frames
        mario_direction_frames = mario_current_frames[self.mario_dir]

        # Get current frame from state frames
        '''
        if self.current_image > len(mario_direction_frames)-1:
            self.current_image = 0

        mario_current_frame = mario_direction_frames[self.current_image]
        '''
        
        mario_current_frame = mario_direction_frames[self.current_image % len(mario_direction_frames)]

        # Get the current sub-sprite to show
        start_box = (mario_current_frame[0]*MARIO_WIDTH, mario_current_frame[1]*MARIO_HEIGHT,
        MARIO_WIDTH,MARIO_HEIGHT)

        # Blit it to the screen
        self.screen.blit(self.sprite_sheet, (self.mario_pos_x, self.mario_pos_y),start_box)
            

    def check_events(self):
        # Check for keyboard events
        for event in pg.event.get():
            if event.type == FLIP_IMAGE:
                # Update the frame to show next
                self.current_image += 1

            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                # Jump
                if self.mario_state != MARIO_IN_AIR:
                    self.mario_state = MARIO_JUMPING
#                    self.current_image = 0
            elif event.type == pg.KEYDOWN and (event.key == pg.K_RIGHT or event.key == pg.K_LEFT):
                # Set his direction
                if event.key == pg.K_RIGHT:
                    self.mario_dir = RIGHT
                else:
                    self.mario_dir = LEFT
                # Check for Shift Key (Running)
                shift = pg.key.get_mods()
                if shift & pg.KMOD_LSHIFT or shift & pg.KMOD_RSHIFT:
                    self.mario_state = MARIO_RUN
                else:
                    self.mario_state = MARIO_WALK
            elif event.type == pg.KEYUP and (event.key == pg.K_RIGHT or event.key == pg.K_LEFT):
                self.mario_state = MARIO_STOPPED

    def run(self):
        # Called once to manage whole game
        while True:
            self.check_events()
            self.update()
            self.draw()

def main():
    # Main function; Creates game object and runs it
    game = Game()
    game.run()

if __name__ == '__main__':
    main()