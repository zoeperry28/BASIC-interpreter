import pygame

def fun(text, font, color, screen, LOC_X, LOC_Y):
    # but does not put it on the screen yet.
    text = font.render(text,True,color)
    # Put the image of the text on the screen at 250x250
    screen.blit(text, [LOC_X, LOC_Y])
    LOC_Y = LOC_Y + 20        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
        