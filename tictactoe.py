import pygame


# Colors
GRAY  = ( 60,  60,  60)
WHITE = (255, 255, 255)
GREEN = (  0, 200,  20)

clock = pygame.time.Clock()
FPS = 15


def game_win(gameboard):
    
    if gameboard[0][0] == 1 and gameboard[1][0] == 1 and gameboard[2][0] == 1:
        return 1
    if gameboard[0][1] == 1 and gameboard[1][1] == 1 and gameboard[2][1] == 1:
        return 1
    if gameboard[0][2] == 1 and gameboard[1][2] == 1 and gameboard[2][2] == 1:
        return 1
        
    if gameboard[0][0] == 1 and gameboard[0][1] == 1 and gameboard[0][2] == 1:
        return 1
    if gameboard[1][0] == 1 and gameboard[1][1] == 1 and gameboard[1][2] == 1:
        return 1
    if gameboard[2][0] == 1 and gameboard[2][1] == 1 and gameboard[2][2] == 1:
        return 1
        
    
    if gameboard[0][0] == 1 and gameboard[1][1] == 1 and gameboard[2][2] == 1:
        return 1
    if gameboard[0][2] == 1 and gameboard[1][1] == 1 and gameboard[2][0] == 1:
        return 1

    if gameboard[0][0] == 2 and gameboard[1][0] == 2 and gameboard[2][0] == 2:
        return 2
    if gameboard[0][1] == 2 and gameboard[1][1] == 2 and gameboard[2][1] == 2:
        return 2
    if gameboard[0][2] == 2 and gameboard[1][2] == 2 and gameboard[2][2] == 2:
        return 2
        
    if gameboard[0][0] == 2 and gameboard[0][1] == 2 and gameboard[0][2] == 2:
        return 2
    if gameboard[1][0] == 2 and gameboard[1][1] == 2 and gameboard[1][2] == 2:
        return 2
    if gameboard[2][0] == 2 and gameboard[2][1] == 2 and gameboard[2][2] == 2:
        return 2
        
    if gameboard[0][0] == 2 and gameboard[1][1] == 2 and gameboard[2][2] == 2:
        return 2
    if gameboard[0][2] == 2 and gameboard[1][1] == 2 and gameboard[2][0] == 2:
        return 2

    else:
        return 0

def main(): 
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Tic Tac Toe 0.2")

    scoreboard_font = pygame.font.Font("HELR45W.ttf", 24)
    board_font = pygame.font.Font("HELR45W.ttf", 96)    

    x_play = board_font.render("X", True, WHITE)
    o_play = board_font.render("O", True, WHITE)

    press_enter = scoreboard_font.render("Press Enter to start a new game", True, GREEN)

    player_x = 0
    player_y = 0

    # Wins counter
    player_1_count = 0
    player_2_count = 0
    ties = 0

    clicks = 0

    # Forgot something important...  A gameboard
    gameboard = [[0 for x in range(3)] for y in range(3)]

    player1_turn = True
    
    running = True

    win_check = 0

    win_statement = ""
    game_over = False
    
    while running:

        # print ("Win_check: " + str(win_check))

        gui = scoreboard_font.render("X : " + str(player_1_count) + "                              O: " + str(player_2_count) + "                              Ties: " + str(ties), True, WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                player_x, player_y = pygame.mouse.get_pos()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and game_over:
                    player_x = 0
                    player_y = 0
                    win_check = 0
                    clicks = 0
                    gameboard = [[0 for x in range(3)] for y in range(3)]
                    player1_turn = True
                    game_over = False
                    
            # mouse_text = scoreboard_font.render(str(player_x) + " : " + str(player_y), True, WHITE)

        if win_check == 1 and not game_over:
            game_over = True
            player_1_count += 1

        elif win_check == 2 and not game_over:
            game_over = True
            player_2_count += 1
            
        elif clicks == 9 and not game_over:
            game_over = True
            ties += 1

        else:

            # Mouse clicks
            # Top Row
            if (player_x > 250 and player_x < 350 and player_y > 150 and player_y < 250):
                if gameboard[0][0] == 0:
                    if player1_turn:
                        gameboard[0][0] = 1
                        clicks += 1
                        player1_turn = False
                    else:
                        gameboard[0][0] = 2
                        clicks += 1
                        player1_turn = True
                    
            if (player_x > 350 and player_x < 450 and player_y > 150 and player_y < 250):
                if gameboard[1][0] == 0:
                    if player1_turn:
                        gameboard[1][0] = 1
                        clicks += 1
                        player1_turn = False
                    else:
                        gameboard[1][0] = 2
                        clicks += 1
                        player1_turn = True
                    
            if (player_x > 450 and player_x < 550 and player_y > 150 and player_y < 250):
                if gameboard[2][0] == 0:
                    if player1_turn:
                        gameboard[2][0] = 1
                        clicks += 1
                        player1_turn = False
                    else:
                        gameboard[2][0] = 2
                        clicks += 1
                        player1_turn = True
                
            # Middle Row
            if (player_x > 250 and player_x < 350 and player_y > 250 and player_y < 350):
                if gameboard[0][1] == 0:
                    if player1_turn:
                        gameboard[0][1] = 1
                        clicks += 1
                        player1_turn = False
                    else:
                        gameboard[0][1] = 2
                        clicks += 1
                        player1_turn = True
                
            if (player_x > 350 and player_x < 450 and player_y > 250 and player_y < 350):
                if gameboard[1][1] == 0:
                    if player1_turn:
                        gameboard[1][1] = 1
                        clicks += 1
                        player1_turn = False
                    else:
                        gameboard[1][1] = 2
                        clicks += 1
                        player1_turn = True
                    
            if (player_x > 450 and player_x < 550 and player_y > 250 and player_y < 350):
                if gameboard[2][1] == 0:
                    if player1_turn:
                        gameboard[2][1] = 1
                        clicks += 1
                        player1_turn = False
                    else:
                        gameboard[2][1] = 2
                        clicks += 1
                        player1_turn = True

            # Bottom Row
            if (player_x > 250 and player_x < 350 and player_y > 350 and player_y < 450):
                if gameboard[0][2] == 0:
                    if player1_turn:
                        gameboard[0][2] = 1
                        clicks += 1
                        player1_turn = False
                    else:
                        gameboard[0][2] = 2
                        clicks += 1
                        player1_turn = True
                    
            if (player_x > 350 and player_x < 450 and player_y > 350 and player_y < 450):
                if gameboard[1][2] == 0:
                    if player1_turn:
                        gameboard[1][2] = 1
                        clicks += 1
                        player1_turn = False
                    else:
                        gameboard[1][2] = 2
                        clicks += 1
                        player1_turn = True
                    
            if (player_x > 450 and player_x < 550 and player_y > 350 and player_y < 450):
                if gameboard[2][2] == 0:
                    if player1_turn:
                        gameboard[2][2] = 1
                        clicks += 1
                        player1_turn = False
                    else:
                        gameboard[2][2] = 2
                        clicks += 1
                        player1_turn = True


            win_check = game_win(gameboard)
                
            screen.fill(GRAY)

            screen.blit(gui, (100, 10))

            pygame.draw.line(screen, WHITE, (350, 150), (350, 450), 5)
            pygame.draw.line(screen, WHITE, (450, 150), (450, 450), 5)
            pygame.draw.line(screen, WHITE, (250, 250), (550, 250), 5)
            pygame.draw.line(screen, WHITE, (250, 350), (550, 350), 5)


            
            for i in range(3):
                for j in range(3):                    
                    if gameboard[i][j] == 1:
                        screen.blit(x_play, ((i * 100) + 265, (j * 100) + 145))
                    elif gameboard[i][j] == 2:
                        screen.blit(o_play, ((i * 100) + 265, (j * 100) + 145))
            
            
            if win_check == 1:
                player_wins = board_font.render("X WINS!", True, GREEN)
                screen.blit(player_wins, (215, 255))
                screen.blit(press_enter, (210, 355))
            elif win_check == 2:
                player_wins = board_font.render("O WINS!", True, GREEN)
                screen.blit(player_wins, (215, 255))
                screen.blit(press_enter, (210, 355))
            elif clicks == 9:
                player_wins = board_font.render("TIE", True, GREEN)
                screen.blit(player_wins, (315, 255))
                screen.blit(press_enter, (210, 355))

            # screen.blit(x_play, (20, 20))
            # screen.blit(o_play, (120, 20))

            # screen.blit(mouse_text, (300, 20))
            
            pygame.display.update()
            clock.tick(FPS)


if __name__ == "__main__":
    main()
