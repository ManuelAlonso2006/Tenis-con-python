import pygame
import random
import time
import sys


def Tenis():
    pygame.init()
    
    # Configuración de la ventana
    ancho_ventana, alto_ventana = 1400, 800
    ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
    pygame.display.set_caption('Tenis')
    
    # Colores
    color_fondo = (0, 51, 0)
    color_player1 = (255, 102, 0)
    color_player2 = (0, 102, 255)
    color_pelota = (255, 255, 255)
    color_fuente = (255, 255, 255)
    # Paletas
    paleta_ancho, paleta_alto = 10, alto_ventana // 5
    x_izq, y_izq = 10, (alto_ventana - paleta_alto) // 2
    x_der, y_der = ancho_ventana - paleta_ancho - 10, (alto_ventana - paleta_alto) // 2
    
    # Pelota
    radio = 10
    pelota_x, pelota_y = ancho_ventana // 2, alto_ventana // 2
    vel_x, vel_y = 5, 5
    
    # Sonidos
    
    rebote = pygame.mixer.Sound('pelota.mp3')
    rebote.set_volume(0.7)
    
    # Puntuación
    player1 = 0
    player2 = 0
    
    fuente = pygame.font.Font(None, 30)
    
    # Temporizador
    inicio = time.time()
    tiempo = 15
    
    # Bucle principal
    ejecutando = True
    
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
    
        # Controles de las paletas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and y_izq > 0:
            y_izq -= 5
        if keys[pygame.K_s] and y_izq < alto_ventana - paleta_alto:
            y_izq += 5
        if keys[pygame.K_UP] and y_der > 0:
            y_der -= 5
        if keys[pygame.K_DOWN] and y_der < alto_ventana - paleta_alto:
            y_der += 5
    
        # Incremento de velocidad periódicamente
        if time.time() - inicio >= tiempo:
            vel_x += 1 if vel_x > 0 else -1
            vel_y += 1 if vel_y > 0 else -1
            tiempo += 15
    
        # Movimiento de la pelota
        pelota_x += vel_x
        pelota_y += vel_y
    
        # Rebote en los bordes superior e inferior
        if pelota_y - radio <= 0 or pelota_y + radio >= alto_ventana:
            vel_y = -vel_y
            rebote.play()
    
        # Rebote en las paletas
        if (pelota_x - radio <= x_izq + paleta_ancho and y_izq < pelota_y < y_izq + paleta_alto) or \
           (pelota_x + radio >= x_der and y_der < pelota_y < y_der + paleta_alto):
            vel_x = -vel_x
            rebote.play()
    
        # Reinicio si la pelota sale por los lados
        if pelota_x - radio <= 0 or pelota_x + radio >= ancho_ventana:
            if pelota_x - radio <= 0:
                player2 += 1
            else:
                player1 += 1
            pelota_x, pelota_y = ancho_ventana // 2, alto_ventana // 2
            vel_x, vel_y = random.choice([3, -3]), random.choice([3, -3])
    
        # Condición de victoria
        if player1 == 5 or player2 == 5:
            ganador = "Jugador rojo" if player1 == 5 else "Jugador azul"
            mensaje = fuente.render(f'{ganador} gana', True, color_fuente)
            ventana.blit(mensaje, (ancho_ventana // 4, alto_ventana // 2))
            pygame.display.flip()
            time.sleep(4)
            pygame.quit()
    
        # Dibujar en pantalla
        ventana.fill(color_fondo)
        score1 = fuente.render(f'Score: {player1}', True, color_fuente)
        ventana.blit(score1, (10, 10))
        score2 = fuente.render(f'Score: {player2}', True, color_fuente)
        ventana.blit(score2, (ancho_ventana - 100, 10))
        pygame.draw.rect(ventana, color_player1, (x_izq, y_izq, paleta_ancho, paleta_alto))
        pygame.draw.rect(ventana, color_player2, (x_der, y_der, paleta_ancho, paleta_alto))
        pygame.draw.line(ventana, (255, 255, 255), (ancho_ventana // 2, 0), (ancho_ventana // 2, alto_ventana), 2)
        pygame.draw.circle(ventana, color_pelota, (pelota_x, pelota_y), radio)
        pygame.display.flip()
    
        # Controlar la velocidad del juego
        pygame.time.Clock().tick(120)
    
    pygame.quit()
    

def Tenis_Bot():
    pygame.init()

    # Configuración de la ventana
    ancho_ventana, alto_ventana = 1400, 800
    ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
    pygame.display.set_caption('Tenis')

    # Colores
    color_fondo = (0, 51, 0)
    color_player1 = (255, 102, 0)
    color_player2 = (0, 102, 255)
    color_pelota = (255, 255, 255)
    color_fuente = (255, 255, 255)

    # Paletas
    paleta_ancho, paleta_alto = 10, alto_ventana // 5
    x_izq, y_izq = 10, (alto_ventana - paleta_alto) // 2
    x_bot, bot_y = ancho_ventana - paleta_ancho - 10, (alto_ventana - paleta_alto) // 2

    # Pelota
    radio = 10
    pelota_x, pelota_y = ancho_ventana // 2, alto_ventana // 2
    vel_x, vel_y = 5, 5

    # Sonidos
    rebote = pygame.mixer.Sound('pelota.mp3')
    rebote.set_volume(0.7)

    # Puntuación
    player1 = 0
    player2 = 0

    fuente = pygame.font.Font(None, 30)

    # Temporizador
    inicio = time.time()
    tiempo = 15

    # Bucle principal
    ejecutando = True

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

        # Controles de las paletas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and y_izq > 0:
            y_izq -= 5
        if keys[pygame.K_s] and y_izq < alto_ventana - paleta_alto:
            y_izq += 5

        # Incremento de velocidad periódicamente
        if time.time() - inicio >= tiempo:
            vel_x += 1 if vel_x > 0 else -1
            vel_y += 1 if vel_y > 0 else -1
            tiempo += 15

        # Movimiento de la pelota
        pelota_x += vel_x
        pelota_y += vel_y

        # Movimiento del bot (IA simple)
        bot_y += (pelota_y - (bot_y + paleta_alto // 2)) * 0.5  # Movimiento suave hacia la pelota

        # Limitar la posición del bot para que no se salga de la ventana
        if bot_y < 0:
            bot_y = 0
        if bot_y > alto_ventana - paleta_alto:
            bot_y = alto_ventana - paleta_alto

        # Rebote en los bordes superior e inferior
        if pelota_y - radio <= 0 or pelota_y + radio >= alto_ventana:
            vel_y = -vel_y
            rebote.play()

        # Rebote en las paletas
        if (pelota_x - radio <= x_izq + paleta_ancho and y_izq < pelota_y < y_izq + paleta_alto) or \
           (pelota_x + radio >= x_bot and bot_y < pelota_y < bot_y + paleta_alto):
            vel_x = -vel_x
            rebote.play()

        # Reinicio si la pelota sale por los lados
        if pelota_x - radio <= 0 or pelota_x + radio >= ancho_ventana:
            if pelota_x - radio <= 0:
                player2 += 1
            else:
                player1 += 1
            pelota_x, pelota_y = ancho_ventana // 2, alto_ventana // 2
            vel_x, vel_y = random.choice([3, -3]), random.choice([3, -3])

        # Condición de victoria
        if player1 == 5 or player2 == 5:
            ganador = "Jugador rojo" if player1 == 5 else "Jugador azul"
            mensaje = fuente.render(f'{ganador} gana', True, color_fuente)
            ventana.blit(mensaje, (ancho_ventana // 2 - 100, alto_ventana // 2))
            pygame.display.flip()
            time.sleep(4)
            pygame.quit()
            break

        # Dibujar en pantalla
        ventana.fill(color_fondo)
        score1 = fuente.render(f'Score: {player1}', True, color_fuente)
        ventana.blit(score1, (10, 10))
        score2 = fuente.render(f'Score: {player2}', True, color_fuente)
        ventana.blit(score2, (ancho_ventana - 100, 10))
        pygame.draw.rect(ventana, color_player1, (x_izq, y_izq, paleta_ancho, paleta_alto))
        pygame.draw.rect(ventana, color_player2, (x_bot, bot_y, paleta_ancho, paleta_alto))
        pygame.draw.line(ventana, (255, 255, 255), (ancho_ventana // 2, 0), (ancho_ventana // 2, alto_ventana), 2)
        pygame.draw.circle(ventana, color_pelota, (pelota_x, pelota_y), radio)
        pygame.display.flip()

        # Controlar la velocidad del juego
        pygame.time.Clock().tick(120)

    pygame.quit()

def Tenis_Dificil():
    pygame.init()

    # Configuración de la ventana
    ancho_ventana, alto_ventana = 1400, 800
    ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
    pygame.display.set_caption('Tenis')

    # Colores
    color_fondo = (0, 51, 0)
    color_player1 = (255, 102, 0)
    color_player2 = (0, 102, 255)
    color_pelota = (255, 255, 255)
    color_fuente = (255, 255, 255)

    # Paletas
    paleta_ancho, paleta_alto = 10, alto_ventana // 5
    x_izq, y_izq = 10, (alto_ventana - paleta_alto) // 2
    x_der, y_der = ancho_ventana - paleta_ancho - 10, (alto_ventana - paleta_alto) // 2

    # Pelota
    radio = 10
    pelota_x, pelota_y = ancho_ventana // 2, alto_ventana // 2
    vel_x, vel_y = 5, 5

    # Sonidos
    rebote = pygame.mixer.Sound('pelota.mp3')
    rebote.set_volume(0.7)

    # Puntuación
    player1 = 0
    player2 = 0

    fuente = pygame.font.Font(None, 30)

    # Temporizador
    inicio = time.time()
    tiempo = 15

    # Bucle principal
    ejecutando = True

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

        # Controles de las paletas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and y_izq > 0:
            y_izq -= 5
        if keys[pygame.K_s] and y_izq < alto_ventana - paleta_alto:
            y_izq += 5
        if keys[pygame.K_a] and x_izq > 0:
            x_izq -= 5
        if keys[pygame.K_d] and x_izq < ancho_ventana // 2 - paleta_ancho:
            x_izq += 5
        if keys[pygame.K_UP] and y_der > 0:
            y_der -= 5
        if keys[pygame.K_DOWN] and y_der < alto_ventana - paleta_alto:
            y_der += 5
        if keys[pygame.K_LEFT] and x_der > ancho_ventana // 2:  # Límite izquierdo para la derecha
            x_der -= 5
        if keys[pygame.K_RIGHT] and x_der < ancho_ventana - paleta_ancho:  # Límite derecho
            x_der += 5

        # Incremento de velocidad periódicamente
        if time.time() - inicio >= tiempo:
            vel_x += 1 if vel_x > 0 else -1
            vel_y += 1 if vel_y > 0 else -1
            tiempo += 15

        # Movimiento de la pelota
        pelota_x += vel_x
        pelota_y += vel_y

        # Rebote en los bordes superior e inferior
        if pelota_y - radio <= 0 or pelota_y + radio >= alto_ventana:
            vel_y = -vel_y
            rebote.play()

        # Rebote en la paleta izquierda
        if pelota_x - radio <= x_izq + paleta_ancho:
            if y_izq <= pelota_y <= y_izq + paleta_alto:  # Si la pelota está dentro de la paleta
                vel_x = -vel_x  # Rebote horizontal
                rebote.play()
            else:  # Si la pelota pasa al otro lado de la paleta
                player2 += 1
                pelota_x, pelota_y = ancho_ventana // 2, alto_ventana // 2
                vel_x, vel_y = random.choice([3, -3]), random.choice([3, -3])

        # Rebote en la paleta derecha
        if pelota_x + radio >= x_der:
            if y_der <= pelota_y <= y_der + paleta_alto:  # Si la pelota está dentro de la paleta
                vel_x = -vel_x  # Rebote horizontal
                rebote.play()
            else:  # Si la pelota pasa al otro lado de la paleta
                player1 += 1
                pelota_x, pelota_y = ancho_ventana // 2, alto_ventana // 2
                vel_x, vel_y = random.choice([3, -3]), random.choice([3, -3])

        # Límite de velocidad para evitar que la pelota vaya demasiado rápido
        vel_x = max(-10, min(10, vel_x))  # Limitar velocidad horizontal
        vel_y = max(-10, min(10, vel_y))  # Limitar velocidad vertical

        # Reinicio si la pelota sale por los lados
        if pelota_x - radio <= 0 or pelota_x + radio >= ancho_ventana:
            if pelota_x - radio <= 0:
                player2 += 1
            else:
                player1 += 1
            pelota_x, pelota_y = ancho_ventana // 2, alto_ventana // 2
            vel_x, vel_y = random.choice([3, -3]), random.choice([3, -3])

        # Condición de victoria
        if player1 == 5 or player2 == 5:
            ganador = "Jugador rojo" if player1 == 5 else "Jugador azul"
            mensaje = fuente.render(f'{ganador} gana', True, color_fuente)
            ventana.blit(mensaje, (ancho_ventana // 4, alto_ventana // 2))
            pygame.display.flip()
            time.sleep(4)
            pygame.quit()

        # Dibujar en pantalla
        ventana.fill(color_fondo)
        score1 = fuente.render(f'Score: {player1}', True, color_fuente)
        ventana.blit(score1, (10, 10))
        score2 = fuente.render(f'Score: {player2}', True, color_fuente)
        ventana.blit(score2, (ancho_ventana - 100, 10))
        pygame.draw.rect(ventana, color_player1, (x_izq, y_izq, paleta_ancho, paleta_alto))
        pygame.draw.rect(ventana, color_player2, (x_der, y_der, paleta_ancho, paleta_alto))
        pygame.draw.line(ventana, (255, 255, 255), (ancho_ventana // 2, 0), (ancho_ventana // 2, alto_ventana), 2)
        pygame.draw.line(ventana, (255, 255, 255), (ancho_ventana // 2, 0), (ancho_ventana // 2, alto_ventana), 2)
        pygame.draw.circle(ventana, color_pelota, (pelota_x, pelota_y), radio)
        pygame.display.flip()

        # Controlar la velocidad del juego
        pygame.time.Clock().tick(120)

    pygame.quit()
    
    
def dibujar_boton(ventana, texto, posicion, color_base, color_hover, fuente, mouse_pos):
    rect_boton = pygame.Rect(posicion)
    color_actual = color_hover if rect_boton.collidepoint(mouse_pos) else color_base
    pygame.draw.rect(ventana, color_actual, rect_boton)
    texto_boton = fuente.render(texto, True, (255, 255, 255))
    ventana.blit(texto_boton, (rect_boton.x + (rect_boton.width - texto_boton.get_width()) // 2,
                               rect_boton.y + (rect_boton.height - texto_boton.get_height()) // 2))
    return rect_boton


def menu_principal():
    pygame.init()
    ancho_ventana, alto_ventana = 1400, 800
    ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
    pygame.display.set_caption("Menu Principal")

    # Colores
    color_fondo = (30, 30, 30)
    color_boton = (70, 130, 180)
    color_hover = (100, 160, 210)

    # Fuente
    fuente = pygame.font.Font(None, 40)

    # Coordenadas y dimensiones de los botones
    boton_tenis = (550, 200, 300, 50)
    boton_tenis_bot = (550, 300, 300, 50)
    boton_tenis_dificil = (550, 400, 300, 50)

    # Bucle principal
    ejecutando = True
    while ejecutando:
        mouse_pos = pygame.mouse.get_pos()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(boton_tenis).collidepoint(mouse_pos):
                    Tenis()  # Llamar a la función del juego básico
                elif pygame.Rect(boton_tenis_bot).collidepoint(mouse_pos):
                    Tenis_Bot()  # Llamar a la función del juego con bot
                elif pygame.Rect(boton_tenis_dificil).collidepoint(mouse_pos):
                    Tenis_Dificil()  # Llamar a la función del juego difícil

        # Dibujar el fondo
        ventana.fill(color_fondo)

        # Dibujar botones
        dibujar_boton(ventana, "Modo Básico", boton_tenis, color_boton, color_hover, fuente, mouse_pos)
        dibujar_boton(ventana, "Contra Bot", boton_tenis_bot, color_boton, color_hover, fuente, mouse_pos)
        dibujar_boton(ventana, "Modo Difícil", boton_tenis_dificil, color_boton, color_hover, fuente, mouse_pos)

        # Actualizar la pantalla
        pygame.display.flip()

    pygame.quit()


# Iniciar el menú principal
if __name__ == "__main__":
    menu_principal()