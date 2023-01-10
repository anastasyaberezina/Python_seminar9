import pygame
import random

pygame.init()

def x_crosses(scr):  # Рисую линии толщиной 4 для крестиков
    pygame.draw.line(scr, (0, 0, 0), (100, 0), (100, 300), 4)
    pygame.draw.line(scr, (0, 0, 0), (200, 0), (200, 300), 4)
    pygame.draw.line(scr, (0, 0, 0), (0, 100), (300, 100), 4)
    pygame.draw.line(scr, (0, 0, 0), (0, 200), (300, 200), 4)

def o_circles(scr, items): # Функция рисования кругов для ноликов
    for i in range(3):
        for j in range(3):
            if items[i][j] == 'O':
                pygame.draw.circle(scr, (255, 0, 0), (j*100+50, i*100+50), 45)
            elif items[i][j] == 'X':
                pygame.draw.line(scr, (0, 0, 255), (j* 100 + 5, i * 100 + 5), (j * 100 + 95, i * 100 + 95), 4)
                pygame.draw.line(scr, (0, 0, 255), (j * 100 + 95, i * 100 + 5), (j * 100 + 5, i * 100 + 95), 4)

def winning_options(fd, symbol): # Проверка всех победных вариантов
    flag_win = False
    for line in fd:
        if line.count(symbol) == 3:
            flag_win = True
    for i in range(3):
        if fd[0][i] == fd[1][i] == fd[2][i] == symbol:
            flag_win = True
    if fd[0][0] == fd[1][1] == fd[2][2] == symbol:
        flag_win = True
    if fd[0][2] == fd[1][1] == fd[2][0] == symbol:
        flag_win = True    
    return flag_win


size_window = (300, 300)

window = pygame.display.set_mode(size_window)

size = pygame.Surface(size_window)

pygame.display.set_caption('Крестики-нолики')
size.fill((255, 255, 255))

positions = [['', '', ''],
             ['', '', ''],
             ['', '', '']]

maingame = True
gameover = False

while maingame: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            maingame = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()    
            if positions[pos[1] // 100][pos[0] // 100] == '':
                positions[pos[1] // 100][pos[0] // 100] = 'X'
                x, y = random.randint(0, 2), random.randint(0, 2) # Куда бот будет ставить O
                while positions[x][y] !='':
                    x, y = random.randint(0, 2), random.randint(0, 2) 
                positions[x][y] = 'O'

            player_win = winning_options(positions, 'X') # Проверка выигрыша
            ai_win = winning_options(positions, 'O')
            if player_win or ai_win:
                gameover = True
                if player_win:
                    pygame.display.set_caption('Игрок победил!')
                else:
                    pygame.display.set_caption('Бот победил!')
            elif positions[0].count('X') + positions[0].count('O') + positions[1].count('X') + positions[1].count('O') + positions[2].count('X') + positions[2].count('O'):
                gameover = True
                pygame.display.set_caption('Ничья')
            
     
    o_circles(size, positions)    
    x_crosses(size)
    window.blit(size, (0,0))  
    pygame.display.update()      