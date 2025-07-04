import pygame
from sys import exit

# Importing the pygame library
# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()


# Set up the window and its dimensions
win_height = 800
win_width = 600
window= pygame.display.set_mode((win_width, win_height))

# Images
bird_images = [pygame.image.load("images/parrotDown.png"),
               pygame.image.load("images/parrotMid.png"),
               pygame.image.load("images/parrotUp.png")]
background_image = pygame.image.load("images/background.png")
ground_image = pygame.image.load("images/ground.png")
top_treetrunk_image = pygame.image.load("images/topTreeTrunk.png")
bottom_treetrunk_image = pygame.image.load("images/bottomTreeTrunk.png")


#Exit Game Function to quit the game
def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

# Main game Method- loop
def main():
    run = True
    while run:
        
        quit_game() #When the window is closed
        window.fill((0, 0, 0))  #Reset frame - fill the window with black

        # Draw the background of the game
        window.blit(background_image, (0, 0))

        clock.tick(60)  # Limit the frame rate to 60 FPS
        pygame.display.update()


main()