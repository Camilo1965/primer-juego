import pygame
import sys
import importlib
import menu_niveles



# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Menu Simple')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define fonts
test_font = pygame.font.Font('fuente/Bad_Boys.ttf', 80)

# Load background image
background = pygame.image.load('fondo/muerte_final.jpg').convert_alpha()

# Define a function to draw text to the screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, False, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


def main_menu():
  
    while True:
        
        screen.blit(background, (0, 0))

        
        draw_text('Menu Principal', test_font, BLACK, 960, 300)

        
        draw_text('1. Jugar', test_font, BLACK, 960, 500)
        draw_text('2. Salir', test_font, BLACK, 960, 650)

        # Update the display
        pygame.display.flip()

        # Check for user input
        for event in pygame.event.get():
            # Handle quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle key presses
            if event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_1:
                   
                    import menu_niveles
                    menu_niveles.main()

                
                if event.key == pygame.K_2:
                    pygame.quit()
                    sys.exit()


if __name__ == '__main__':
    main_menu()
