import pygame
import BASIC_Disp
import start as FILE
# Define some colors
BLACK = (112,164,178)
WHITE = (112,164,178)
GREEN = (0, 255, 0)
RED = 	(0, 0, 170)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("C64 BASIC")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    pygame.draw.rect(screen, RED, [20, 20, 650, 450], 0)
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 16, True, False)
    
    # Render the text. "True" means anti-aliased text.
    # Black is the color. The variable BLACK was defined
    # above as a list of [0, 0, 0]
    # Note: This line creates an image of the letters,
    LOC_X = 30
    LOC_Y = 90


    #res = FILE.BASIC_Load_Lines()
    #print(res)

    BASIC_Disp.fun("hello",font, BLACK, screen, LOC_X, LOC_Y)

    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()

