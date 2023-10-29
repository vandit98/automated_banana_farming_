import pygame
import cv2

# getting image shape
img = cv2.imread("/home/vandit/Downloads/presentation/rl/reinforcement/neat-cars/testing/Backgroundp.jpg")
height,width,_=img.shape


pygame.init()

# Set up the screen
screen_width = width
screen_height = height
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the image
background_image = pygame.image.load("/home/vandit/Downloads/presentation/rl/reinforcement/neat-cars/testing/Backgroundp.jpg")

# Set the image as the background of the screen
screen.blit(background_image, (0, 0))

# Draw on the screen
# ...

# Update the screen
pygame.display.update()

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
