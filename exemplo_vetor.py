import pygame

# Inicializa Pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))

# Posição inicial e vetor de deslocamento
posicao = pygame.Vector2(100, 100)
vetor_deslocamento = pygame.Vector2(5, 3)

# Loop para mover um objeto
running = True
while running:
    screen.fill((0, 0, 0))  # Fundo preto
    pygame.draw.circle(screen, (0, 255, 0), (int(posicao.x), int(posicao.y)), 10)  # Desenha um círculo
    
    posicao += vetor_deslocamento  # Atualiza a posição com o vetor

    pygame.display.flip()
    pygame.time.delay(50)  # Pequeno atraso na atualização

pygame.quit()
