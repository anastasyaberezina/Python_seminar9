import pygame
import random

pygame.init()

def draw_grid(scr):  # Рисую линии толщиной 4
    pygame.draw.line(scr, (0, 0, 0), (100, 0), (100, 300), 4)
    pygame.draw.line(scr, (0, 0, 0), (200, 0), (200, 300), 4)
    pygame.draw.line(scr, (0, 0, 0), (0, 100), (300, 100), 4)
    pygame.draw.line(scr, (0, 0, 0), (0, 200), (300, 200), 4)

def draw_tic_tac_toe(scr, items): # Функция рисования кругов
    for i in range(3):
        for j in range(3):
            if items[i][j] == 'O':
                pygame.draw.circle(scr, (255, 0, 0), (j*100+50, i*100+50), 45)
            elif items[i][j] == 'X':
                pygame.draw.line(scr, (0, 0, 255), (j* 100 + 5, i * 100 + 5), (j * 100 + 95, i * 100 + 95), 4)
                pygame.draw.line(scr, (0, 0, 255), (j * 100 + 95, i * 100 + 5), (j * 100 + 5, i * 100 + 95), 4)

def get_win_check(fd, symbol): # Проверка всех победных вариантов
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

SCREEN_SIZE = (300, 300)

window = pygame.display.set_mode(SCREEN_SIZE)

screen = pygame.Surface(SCREEN_SIZE)

pygame.display.set_caption('Крестики-нолики')
screen.fill((255, 255, 255))

field = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

mainloop = True
game_over = False

while mainloop: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()    
            if field[pos[1] // 100][pos[0] // 100] == '':
                field[pos[1] // 100][pos[0] // 100] = 'X'
                x, y = random.randint(0, 2), random.randint(0, 2) # Куда бот будет ставить O
                while field[x][y] !='':
                    x, y = random.randint(0, 2), random.randint(0, 2) 
                field[x][y] = 'O'

            player_win = get_win_check(field, 'X') # Проверка выигрыша
            ai_win = get_win_check(field, 'O')
            if player_win or ai_win:
                game_over = True
                if player_win:
                    pygame.display.set_caption('Игрок победил!')
                else:
                    pygame.display.set_caption('Бот победил!')
            elif field[0].count('X') + field[0].count('O') + field[1].count('X') + field[1].count('O') + field[2].count('X') + field[2].count('O'):
                game_over = True
                pygame.display.set_caption('Ничья')
            
     
    draw_tic_tac_toe(screen, field)    
    draw_grid(screen)
    window.blit(screen, (0,0))  
    pygame.display.update()      