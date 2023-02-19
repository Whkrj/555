import pygame
pygame.init()

screen_width = 690
screen_height = 690
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('바둑판')

background = pygame.image.load('dhahrvks.png')
background = pygame.transform.scale(background, (690,690))
bkxmf = pygame.image.load('bkxmf.png')
wexmf = pygame.image.load('wexmf.png')
tjfwjd = bkxmf

tjfwjd_X_pos = 345
tjfwjd_Y_pos = 369.6428571428572
bkbk = False
wewe = False
i = 0
j = 0

stone = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

runing = True
while runing:
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                tjfwjd_X_pos -= 46
            elif event.key == pygame.K_RIGHT:
                tjfwjd_X_pos += 46
            elif event.key == pygame.K_DOWN:
                tjfwjd_Y_pos += 49.28571428571429
            elif event.key == pygame.K_UP:
                tjfwjd_Y_pos -= 49.28571428571429
            elif event.key == pygame.K_RSHIFT:
                if tjfwjd == bkxmf:
                    print("검정돌")
                    bkbk = True
                    tjfwjd = wexmf
                    i = int(tjfwjd_X_pos/46+0.5)
                    j = int(tjfwjd_Y_pos/49.28571428571429+0.5)
                    stone[j][i]=1
                elif tjfwjd == wexmf:
                    print("하얀돌")
                    wewe = True
                    tjfwjd = bkxmf
                    i=int(tjfwjd_X_pos/46+0.5)
                    j=int(tjfwjd_Y_pos/49.28571428571429+0.5)
                    stone[j][i]=2
            elif event.key == pygame.K_LSHIFT:
                i=int(tjfwjd_X_pos/46+0.5)
                j=int(tjfwjd_Y_pos/49.28571428571429+0.5)
                stone[j][i]=0

    if tjfwjd_X_pos<-23:
        tjfwjd_X_pos=-23
    if tjfwjd_X_pos>690-22:
        tjfwjd_X_pos=690-22
    if tjfwjd_Y_pos<-24.64285714285715:
        tjfwjd_Y_pos=-24.64285714285715
    if tjfwjd_Y_pos>665.3571428571430:
        tjfwjd_Y_pos=665.3571428571430
    screen.blit(tjfwjd, (tjfwjd_X_pos,tjfwjd_Y_pos))
    for i in range(len(stone)):
        for j in range(len(stone[i])):
            if stone[i][j] == 1:
                bk = pygame.image.load('black.png')
                bk = pygame.transform.scale(bk, (46,46))
                screen.blit(bk, (-23+(j*46), -24.64285714285715+(i*49.28571428571429)))
            if stone[i][j] == 2:
                we = pygame.image.load('white.png')
                we = pygame.transform.scale(we, (46,46))
                screen.blit(we, (-23+(j*46), -24.64285714285715+(i*49.28571428571429)))
    pygame.display.update()

pygame.quit()