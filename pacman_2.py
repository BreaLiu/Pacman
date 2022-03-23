import pygame

pygame.init

screen = pygame.display.set_mode((800, 600), 0)

AMARELO = (255, 255, 0)
PRETO (0, 0, 0)

class Pacman:
    def __init__(self):
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = 50
        self.raio = self.tamanho // 2


def pintar(self, screen):
       # Desenhar o corpo do Pacman
       pygame.draw.circle(screen, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)

       # Desenho da boca do Pacman
       canto_boca = (self.centro_x, self.centro_y)
       labio_superior = (self.centro_x + raio, self.centro_y - raio)
       labio_inferior = (self.centro_x + raio, self.centro_y)
       pontos = [canto_boca, labio_superior, labio_inferior]

       pygame.draw.polygon(screen, PRETO, pontos, 0)

       # Olhos do Pacman
       olho_x = int(self.centro_x + self.raio / 2)
       olho_y = int(self.centro_y - self.raio / 2)
       olho_raio = int(self.raio / 10)
       pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

if __name__ == "__main":
    pacman = Pacman()

    while True:
        # Pintar a tela
        pacman.pintar(screen)
        pygame.display.update()

        for e in pygame.event.get()
            if e.type == pygame.QUIT:
                exit()
