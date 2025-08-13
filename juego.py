import pygame
from random import randint

#TEMPORIZADOR   

def display_score():


   
    current_time = int(pygame.time.get_ticks() /1000)- start_time
    score_surface = test_font.render(f'{current_time}',False,(255, 255, 255))
    score_rect =  score_surface.get_rect(midbottom = (960,100))
    screen.blit(score_surface,score_rect)
    return current_time
def obstacle_movement(obstacle_list):
    

    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 10
            if obstacle_rect.bottom == 600:
                screen.blit(enemy_surface,obstacle_rect)
            else:
                screen.blit(enemy_surface2,obstacle_rect) 
            obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
            
        return  obstacle_list   
    else:

        return []
def coliision(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False    
    return True
def player_animation():
    global player_surface,player_index  

    if player_rect.bottom < 480:
        player_surface = player_jump[player_jump_index]
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)]



#musica
pygame.mixer.init()
sound = pygame.mixer.Sound('primer-juego/musica/lies.mp3')
sound.set_volume(0.1)


#logo
pygame.display.set_icon(pygame.image.load('primer-juego/icono/berserk.png'))


pygame.init()

# Crear la ventana del juego 
screen = pygame.display.set_mode((1480,900))

# Titulo del juego
pygame.display.set_caption("Berserker")

#reloj del juego
clock = pygame.time.Clock()

#estados de juego
game_active = True

#Fuentes 
test_font = pygame.font.Font('primer-juego/fuente/Bad_Boys.ttf',80)

#puntuacion 
score = 0


#background
sky_surface = pygame.image.load('primer-juego/fondo/background.png').convert_alpha()
ground_surface = pygame.image.load('primer-juego/fondo/graveyard.png').convert_alpha()
ground_surface2 = pygame.image.load('primer-juego/fondo/graveyard.png').convert_alpha()
ground_surface3 = pygame.image.load('primer-juego/fondo/graveyard.png').convert_alpha()
ground_surface4 = pygame.image.load('primer-juego/fondo/graveyard.png').convert_alpha()
ground_surface5 = pygame.image.load('primer-juego/fondo/graveyard.png').convert_alpha()
ground_surface6 = pygame.image.load('primer-juego/fondo/graveyard.png').convert_alpha()
#dead_surface = pygame.image.load('primer-juego/fondo/muerte.png').convert_alpha()
dead_surface = pygame.image.load('primer-juego/fondo/muerte2.jpg').convert_alpha()




#enemigo lobo
enemy_frame = pygame.image.load('primer-juego/enemigos/hell-gato/hell-gato-1.png').convert_alpha()
enemy_frame2 = pygame.image.load('primer-juego/enemigos/hell-gato/hell-gato-2.png').convert_alpha()
enemy_frame3 = pygame.image.load('primer-juego/enemigos/hell-gato/hell-gato-3.png').convert_alpha()
enemy_frame4 = pygame.image.load('primer-juego/enemigos/hell-gato/hell-gato-4.png').convert_alpha()
enemy_frames = [enemy_frame,enemy_frame2,enemy_frame3,enemy_frame4]
enemy_frame_index = 0
enemy_surface = enemy_frames[enemy_frame_index]
# Escalar la imagen del enemigo 
escala = 3
enemy_surface = pygame.transform.scale(enemy_surface, (enemy_surface.get_width() * escala, enemy_surface.get_height() * escala)) 
enemy_rect = enemy_surface.get_rect(midbottom = (1600,491))

enemy_frames = [pygame.transform.scale(img, (img.get_width() * escala, img.get_height() * escala)) for img in enemy_frames]



#enemigo angel
enemy_frame_angel = pygame.image.load('primer-juego/angel/angel1.png').convert_alpha()
enemy_frame_angel_2 = pygame.image.load("primer-juego/angel/angel2.png").convert_alpha()
enemy_frame_angel_3= pygame.image.load('primer-juego/angel/angel3.png').convert_alpha()
enemy_frame_angel_4 = pygame.image.load("primer-juego/angel/angel4.png").convert_alpha()
enemy_frame_angel_5 = pygame.image.load('primer-juego/angel/angel5.png').convert_alpha()
enemy_frame_angel_6 = pygame.image.load("primer-juego/angel/angel6.png").convert_alpha()
enemy_frame_angel_7 = pygame.image.load('primer-juego/angel/angel7.png').convert_alpha()
enemy_frame_angel_8 = pygame.image.load("primer-juego/angel/angel8.png").convert_alpha()
enemy_angel_frames = [enemy_frame_angel,enemy_frame_angel_2,enemy_frame_angel_3,enemy_frame_angel_4,enemy_frame_angel_5,enemy_frame_angel_6,enemy_frame_angel_7,enemy_frame_angel_8]
enemy_frame_2_index = 0
enemy_surface2 = enemy_angel_frames[enemy_frame_2_index]
enemy_rect2 = enemy_surface2.get_rect(midbottom = (1400,491))
# Escalar la imagen del enemigo 
escala = 3
enemy_surface2 = pygame.transform.scale(enemy_surface2, (enemy_surface2.get_width() * escala, enemy_surface2.get_height() * escala)) 
enemy_angel_frames = [pygame.transform.scale(img, (img.get_width() * escala, img.get_height() * escala)) for img in enemy_angel_frames]




#lista de primer-juego/enemigos
obstacle_rect_list = []


score_surface = test_font.render('EdgeRunner',False,(255, 255, 255))
score_rect = score_surface.get_rect(midbottom = (960,100))


#jugador 
player_walk_1 = pygame.image.load('primer-juego/hero/hero-run/hero-run-1.png').convert_alpha()
player_walk_2 = pygame.image.load('primer-juego/hero/hero-run/hero-run-2.png').convert_alpha()
player_walk_3 = pygame.image.load('primer-juego/hero/hero-run/hero-run-3.png').convert_alpha()
player_walk_4 = pygame.image.load('primer-juego/hero/hero-run/hero-run-4.png').convert_alpha()
player_walk_5 = pygame.image.load('primer-juego/hero/hero-run/hero-run-5.png').convert_alpha()
player_walk_6 = pygame.image.load('primer-juego/hero/hero-run/hero-run-6.png').convert_alpha()
player_walk = [player_walk_2,player_walk_2,player_walk_3,player_walk_4,player_walk_5,player_walk_6]
player_index = 0
player_jump1 = pygame.image.load('primer-juego/hero/hero-jump/hero-jump-1.png').convert_alpha()
player_jump2 = pygame.image.load('primer-juego/hero/hero-jump/hero-jump-2.png').convert_alpha()
player_jump3 = pygame.image.load('primer-juego/hero/hero-jump/hero-jump-3.png').convert_alpha()
player_jump = [player_jump1,player_jump2,player_jump3]
player_jump_index = 0
player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom = (100,491))
player_stand = pygame.image.load('primer-juego/angel/angel5.png').convert_alpha()

# Escalar la imagen del personaje
escala = 3
player_surface = pygame.transform.scale(player_surface, (player_surface.get_width() * escala, player_surface.get_height() * escala))
player_stand = pygame.transform.scale(player_stand, (player_stand.get_width() * escala, player_stand.get_height() * escala))

# Escalar las imágenes de la animación de caminar
player_walk = [pygame.transform.scale(img, (img.get_width() * escala, img.get_height() * escala)) for img in player_walk]

# Escalar las imágenes de la animación de saltar
player_jump = [pygame.transform.scale(img, (img.get_width() * escala, img.get_height() * escala)) for img in player_jump]



#pantalla de muerte jugador x.y
player_stand_rect = player_stand.get_rect(midbottom = (965,300))

player_gravity = 0  

#tiempo de juego
start_time = int(pygame.time.get_ticks() /1000)

        #nombre del juego
        #game_name = test_font.render('Berserker',False,(0,0,0))
        #game_name_rect = game_name.get_rect(center = (960,100))

#mensaje de juego muerte
game_menssage = test_font.render('Presiona espacio para jugar ',False,(0,0,0))
game_menssage_rect = game_menssage.get_rect(center = (960,390))


#timers 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,2800)



enemy_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(enemy_animation_timer,190)

enemy_angel_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(enemy_angel_animation_timer,300)


#actualizar todo dentro de la ventana
while True: 
    
    for event in pygame.event.get():
        #sound.play()
        #pygame.QUIT = cerrar la ventana
        if event.type == pygame.QUIT:
            pygame.quit()
            quit() 


                #input del teclado
        if game_active:     
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 480:
                    player_gravity = -25
                    
        
            
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
               
                start_time = int(pygame.time.get_ticks() /1000) 



        if game_active:        
            if event.type == obstacle_timer:
                if randint(0,2):
                            obstacle_rect_list.append(enemy_surface.get_rect(midbottom = (randint(600,1910),600)))
                else: obstacle_rect_list.append(enemy_surface2.get_rect(midbottom = (randint(650,1920),400)))
            if event.type == enemy_animation_timer:
                if enemy_frame_index == 0: enemy_frame_index = 1
                else: enemy_frame_index = 0 
                enemy_surface = enemy_frames[enemy_frame_index]



            if event.type == enemy_angel_animation_timer:
                if enemy_frame_2_index == 0: enemy_frame_2_index = 2
                else: enemy_frame_2_index = 0 
                enemy_surface2 = enemy_angel_frames[enemy_frame_2_index]
                

   


        #cordenadas x,y     
    if game_active:   
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,550))
        screen.blit(ground_surface2,(384,550))
        screen.blit(ground_surface3,(768,550))
        screen.blit(ground_surface4,(1152,550))
        screen.blit(ground_surface5,(1536,550))
        score = display_score()

                #movimiento del enemigo
                #screen.blit(enemy_surface,(enemy_rect))
                #enemy_rect.x -= 8
                #if enemy_rect.right <= 0:
                #enemy_rect.left = 1920

        #movimiento del jugador
        screen.blit(player_surface,player_rect)
        player_animation()
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 480:
            player_rect.bottom = 480
            
        #obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

                    #pygame.draw.rect(screen,(255, 163, 143),score_rect)
                    #pygame.draw.rect(screen,(255, 163, 143),score_rect,5)
                    #screen.blit(score_surface,score_rect)

                    #fin del juego si te golpea el enemigo
                    #if enemy_rect.colliderect(player_rect):
                    #game_active = False

        #colision
        game_active = coliision(player_rect,obstacle_rect_list)            
    else:
        pygame.mixer.init()
        #screen.fill((255,255,255))
        obstacle_rect_list.clear()
        player_gravity = 0
        player_rect.midbottom = (100,491)
        screen.blit(dead_surface,(0,-120))
        screen.blit(player_stand,player_stand_rect)
        score_message = test_font.render(f'Puntuacion: {score}',False,(0,0,0))

        score_message_rect = score_message.get_rect(center = (960,390))
        #screen.blit(game_name,game_name_rect)
        if score == 0:
            screen.blit(game_menssage,game_menssage_rect)
        else:
            screen.blit(score_message,score_message_rect)
        #FPS    
    pygame.display.update() 
    clock.tick(75)
        









