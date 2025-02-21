import pygame

# Inicializa Pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Movimento do Círculo")

# Posição inicial e vetor de deslocamento
posicao = pygame.Vector2(100, 100)
vetor_deslocamento = pygame.Vector2(5, 3)

# Loop para mover um objeto
running = True
while running:
    # Verifica eventos, como fechar a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualiza a tela
    screen.fill((0, 0, 0))  # Fundo preto
    pygame.draw.circle(screen, (0, 255, 0), (int(posicao.x), int(posicao.y)), 10)  # Desenha o círculo

    # Atualiza a posição
    posicao += vetor_deslocamento

    # Mantém o círculo dentro da tela
    if posicao.x <= 0 or posicao.x >= 500:
        vetor_deslocamento.x *= -1  # Inverte a direção no eixo X
    if posicao.y <= 0 or posicao.y >= 500:
        vetor_deslocamento.y *= -1  # Inverte a direção no eixo Y

    pygame.display.flip()  # Atualiza a exibição
    pygame.time.delay(50)  # Pequeno atraso na atualização

pygame.quit()
