import pygame
from src.colors import color

def algorithmsButtonsDisplay(screen,buttons, y, position, box_dim, mouse_pos, active, font, sort):
    y = 70 # for the boxes,
    x1, y1, = position[0], position[1] # for the boxes texts
    
    for button in buttons:
        size = pygame.font.Font.size(font, button)
        button_box = pygame.Rect(x1, y, box_dim[0], box_dim[1])
        # checking if the algorithms choice
        click = pygame.mouse.get_pressed()
        if mouse_pos[0]in range(x1,x1+box_dim[0]) and mouse_pos[1] in range(y1,y1+box_dim[1]) and click[0] == 1 and not sort:
            active = button
        # hover button effect
        if mouse_pos[0]in range(x1,x1+box_dim[0]) and mouse_pos[1] in range(y1,y1+box_dim[1]):
            pygame.draw.rect(screen, color.grey.value, button_box)
            line = font.render(button, True, color.white.value)
        else:
            pygame.draw.rect(screen, color.grey.value, button_box, 2)
            line = font.render(button, True, color.white.value)
        
        if(active == button):
            pygame.draw.rect(screen, color.green.value, button_box)
            line = font.render(button, True, color.black.value)
        screen.blit(line, (x1-(size[0]/2)+(box_dim[0]/2), y1))
        y += 45
        y1 += 45 
    return active
