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


# Game Variables
scroll_speed = 1 # Speed at which the background scrolls
bird_start_position = (100, 300)  # Starting position of the bird

#Create a class for the Bird
class Bird(pygame.sprite.Sprite):
    def __init__(self):  # Initialize the Bird class
        pygame.sprite.Sprite.__init__(self)
        self.image = bird_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = bird_start_position
        self.image_index = 0  # Index for bird animation

    def update(self):  # Update the bird's position and animation
        self.image_index += 1
        if self.image_index >= 30: # Restart the animation after 30 frames (10 frames per image)
            self.image_index = 0
        self.image = bird_images[self.image_index // 10]  # Change the bird image every 10 frames


# Create a class for the Ground
class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y): # Initialize the Ground class
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self): # Update the position of the ground(move the ground)
        self.rect.x -= scroll_speed
        if self.rect.x <= -win_width:
            self.kill()

#Exit Game Function to quit the game
def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

# Main game Method- loop
def main():
    x_pos_ground, y_pos_ground = 0, 700  # Initial x and y position of the ground
    ground = pygame.sprite.Group()  # Create a sprite group for the ground
    ground.add(Ground(x_pos_ground, y_pos_ground))  # Add the ground sprite to the group


    run = True
    while run:
        
        quit_game() #When the window is closed
        window.fill((0, 0, 0))  #Reset frame - fill the window with black

        # Draw the background of the game
        window.blit(background_image, (0, 0))

        

        # Draw the ground
        ground.draw(window)

        #Spawn the ground at the bottom of the screen
        if len(ground) <= 8:
            ground.add(Ground(win_width, y_pos_ground))
        
        #update - TreeTrunks, ground, and bird
        ground.update()

        clock.tick(60)  # Limit the frame rate to 60 FPS
        pygame.display.update()


main()
