import pygame
import sys




pygame.init()



screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Menu Simple')

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fuentes
test_font = pygame.font.Font('primer-juego/fuente/Bad_Boys.ttf',80)


background = pygame.image.load('primer-juego/fondo/muerte_final.jpg').convert_alpha()


def draw_text(text, test_font, color, x, y):
    text_surface = test_font.render(text, False,WHITE)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# menu
def main():

   

    while True:
        screen.blit(background,(0,0))

        draw_text('Nivel 1', test_font, BLACK, 960, 300)
        draw_text('Nivel 2', test_font, BLACK, 960, 500)
        draw_text('Nivel 3', test_font, BLACK, 960, 650)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    import juego
                    juego.main()
                elif event.key == pygame.K_2:
                    import nivel_2
                    nivel_2.main()
                elif event.key == pygame.K_3:
                    import nivel_3
                    nivel_3.main()
if __name__ == '__main__':
    main()
