
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
        self.current_frames_count = 0
        self.new_game()

    def load_sprite_sheet(self):
        # Load the sprite sheet once for entire game.  Double its size to make playable
        img_load = pg.image.load(IMG_FOLDER + "/mariosheet.gif")
        self.sprite_sheet = pg.transform.scale(img_load, (img_load.get_width()*2,img_load.get_height()*2)) # Make img 2X bigger

    def new_game(self):
        # Create a new game
        self.current_image = 0
        self.movey = self.movex = 0
        self.load_sprite_sheet()
        self.mario_pos_x = 50
        self.mario_pos_y = 100
        self.mario_x_move = 5.0
        self.mario_y_move = -10.0
        pg.time.set_timer(FLIP_IMAGE, IMG_REFRESH)

    def update(self):
        # Update the game physics
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'Sluggo Mario - {self.clock.get_fps():.1f}')

        ###### Set the states ######
        if self.mario_pos_y+MARIO_HEIGHT < GROUND_LEVEL:
            self.mario_state = IN_AIR_R
            self.mario_y_move += GRAVITY
            self.current_image = 0
        elif self.mario_state == IN_AIR_R and self.mario_pos_y+MARIO_HEIGHT >= GROUND_LEVEL:
            self.mario_state = LANDED_R
            self.mario_x_move = 0
            self.mario_y_move = 0
        elif self.mario_state == STOPPED_R:
            self.mario_x_move = 0
            self.mario_y_move = 0
        elif self.mario_state == LANDED_R:
            self.mario_state = STOPPED_R
            self.mario_x_move = 0
            self.mario_y_move = 0
        elif self.mario_state == JUMPING_R:
            self.mario_y_move -= 15.0
            self.mario_state == IN_AIR_R
            self.current_image = 0
        elif self.mario_state == WALK_R:
            self.mario_x_move = 1.2
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
        pass
            

    def check_events(self):
        # Check for keyboard events
        for event in pg.event.get():
            if event.type == FLIP_IMAGE:
                # Update the frame to show next
                self.current_image += 1
                if self.current_image == len(MKF[self.mario_state]):
                    self.current_image = 0
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                # Jump
                self.mario_state = JUMPING_R
                self.current_image = 0                    
            elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
                self.mario_state = WALK_R
                self.current_image = 0
            elif event.type == pg.KEYUP and event.key == pg.K_RIGHT:
                self.mario_state = STOPPED_R
                self.current_image = 0


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