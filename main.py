import pygame
import time
import os

# init pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption("Virtual Pumpkin Launching Simulation")

# window width and height
WIN_WIDTH = 800
WIN_HEIGHT = 600

# bg colors for screens
BG_COLOR = pygame.Color("#ff914d")

# load home screen image
HOME_IMG = pygame.transform.scale(pygame.image.load(os.path.join("images", "PFling_edited.png")), (800, 600))

# home screen class
class Homescreen():
    def __init__(self, win):
        self.win = win
        # general x location of button
        self.btn_location_x = 3*WIN_WIDTH/4
        # general y location of button
        self.btn_location_y = 3*WIN_HEIGHT/4
        # create title object and set render title text
        self.title = pygame.font.SysFont("Corbel", 50, bold=True).render("Virtual Pumpkin Launching Sim", True, (0,0,0))
        self.win.blit(self.title, self.title.get_rect(center=(WIN_WIDTH/2, 50)))

        # button text
        self.btn_text = pygame.font.SysFont("Corbel", 35).render('Start!', True, (255,255,255))

    # fills background with orange and makes background the loaded image
    def fill_bg(self):
        self.win.fill(BG_COLOR)
        self.win.blit(HOME_IMG, [0, 0])

    # renders button and button text
    def render_button(self):
        self.start_btn = pygame.draw.rect(self.win, (0,0,0), [self.btn_location_x-140, self.btn_location_y-40, 140, 40])
        self.win.blit(self.btn_text, self.btn_text.get_rect(center=(self.start_btn.centerx, self.start_btn.centery)))

    # returns true or false if button is clicked
    def check_btn_click(self, mouse):
        return self.btn_location_x-140 <= mouse[0] <= self.btn_location_x and self.btn_location_y-40 <= mouse[1] <= self.btn_location_y

# initializes simulation
def init_game():
    # initializes window and clock
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    # runs game loop
    run = True
    while run:
        # gets all events
        for event in pygame.event.get():
            # quits game
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            # draws homescreen
            homescreen = Homescreen(win)
            homescreen.fill_bg()
            homescreen.render_button()

            # checks if left mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                # gets mouse position
                mouse = pygame.mouse.get_pos()
                # detects if mouse clicked on start button - later this will transition to another screen
                if homescreen.check_btn_click(mouse):
                    print("clicked")

        # updates display
        pygame.display.update()
        clock.tick(60)

# runs when program is run
if __name__ == '__main__':
    init_game()