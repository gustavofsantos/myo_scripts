# Autor: Gustavo Santos
# Email: gfdsantos@inf.ufpel.edu.br

import pygame, random, pyautogui

def desenhar(srf, cor, inicio, fim, raio=1):
    '''
    Desenha uma linha de uma determinada cor, com um determinado
    raio de "inicio" ate "fim"
    '''
    dx = fim[0]-inicio[0]
    dy = fim[1]-inicio[1]
    distancia = max(abs(dx), abs(dy))

    for i in range(distancia):
        x = int(inicio[0]+float(i)/distancia*dx)
        y = int(inicio[1]+float(i)/distancia*dy)
        pygame.draw.circle(srf, cor, (x, y), raio)


def main():
    tela = pygame.display.set_mode(pyautogui.size(), pygame.FULLSCREEN)

    cores = [(255, 60, 60), (0, 220, 0), (30, 60, 255), (240, 0, 130), (230, 220, 50)]
    borracha = (0, 0 ,0)
    usando_borracha = False

    desenhando = False
    last_pos = (0, 0)
    cor = random.choice(cores)
    raio_desenho = 10
    raio_borracha = 20
    raio = 10

    try:
        while True:
            # um handler para qualquer evento do pygame 
            e = pygame.event.wait()

            # debug dos eventos capturados
            print(e)

       	    # se o tipo do evento é de uma tecla pressionada
            if e.type == pygame.KEYDOWN:
                if e.key == 98: # letra B
                    if not usando_borracha:
                        cor = borracha
                        usando_borracha = True
                        raio = raio_borracha
                    else:
                        cor = random.choice(cores)
                        usando_borracha = False
                        raio = raio_desenho
                    if desenhando == True:
                    	pygame.draw.circle(tela, cor, last_pos, raio)
            if e.type == pygame.KEYUP:
                cor = random.choice(cores)
                if desenhando == True:
                	pygame.draw.circle(tela, cor, last_pos, raio)

            if e.type == pygame.QUIT:
                raise StopIteration

            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 3:
                    cor = borracha
                    usando_borracha = True
                    raio = raio_borracha
                else:
                    cor = random.choice(cores)
                    raio = raio_desenho
                pygame.draw.circle(tela, cor, e.pos, raio)
                desenhando = True

            if e.type == pygame.MOUSEBUTTONUP:
                cor = random.choice(cores)
                desenhando = False
                usando_borracha = False

            if e.type == pygame.MOUSEMOTION:
                if desenhando:
                    pygame.draw.circle(tela, cor, e.pos, raio)
                    desenhar(tela, cor, e.pos, last_pos,  raio)
                last_pos = e.pos

            pygame.display.flip()

    except StopIteration:
        pass

    pygame.quit()

if __name__ == '__main__':
    main()