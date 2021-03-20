import config
import colorama
from colorama import Fore, Back, Style
from input import *
import termios
import subprocess as sp
import time
import tty
import sys
import os
from board import *
from paddle import *
from ball import *
from brick import *
from powerup import *
from boss import *
from all_func import *
import all_func
colorama.init()

if __name__ == "__main__":
    orig_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin)
    input = input()
    input.hide_cursor()
    config.time_start = time.time()
    while(1):
        all_func.xcoords = []
        all_func.ycoords = []
        # print(all_func.xcoords)
        #taking inputs
        if input.input_to():
            val = input.getch()
            # print(rows)

            if(val == 'q' or val == 'Q'):
                break
            elif(val == "a" or val == "A"):
                if(game_paddle._start > 2):
                    game_paddle.move_left(2)
                else:
                    game_paddle._start = 1
            elif(val == "d" or val == "D"):
                if(game_paddle._start < 88 - game_paddle._paddlelen):
                    game_paddle.move_right(2)
                else:
                    game_paddle._start = 89 - game_paddle._paddlelen  
            elif(val == " "):
                config.grab = 0
            elif(val == "l" or val == "L"):
                config.level+=1
                config.grab = 1
                config.time_start = time.time()
                set_level()
            elif(val == "r" or val == "R"):
                game_boss.reduce_health()

            termios.tcflush(sys.stdin, termios.TCIOFLUSH)
            
        #filling paddle in grid
        for i in range(2):
            for j in range(game_paddle._paddlelen):
                    game_back._grid[25+i][game_paddle._start+j] = game_paddle.get_paddle(i,j)
        
        all_func.ball_x = game_ball.get_xpos()
        all_func.ball_y = game_ball.get_ypos()
        all_func.xcoords.append(all_func.ball_x - game_ball._xvel)
        all_func.xcoords.append(all_func.ball_x)
        all_func.ycoords.append(all_func.ball_y - game_ball._yvel)
        all_func.ycoords.append(all_func.ball_y)
       
               
        show_ball()

        if(config.level < 3):
            show_brick()

            powerup_run()

            coll_powerup()

            activating_powerup()

            powerup_deactivate()
        
            coll_brick()

            coll_explosive()    

            colour_change()
    
            level_up()
        else:
            config.bomb_flag = 1
            for i in range(3):
                for j in range(game_paddle._paddlelen):
                        game_back._grid[5+i][game_paddle._start+j] = game_boss.get_boss(i,j)

            coll_boss()
            
        if(config.bullet_flag == 1):
            show_bullet()
            coll_bullet()

        if(config.bomb_flag == 1):
            show_bomb()
            # coll_bullet()
        
        boss_brickss()

        coll_paddle()


        show_grid()
        
        clear_grid()
        
        if(config.lives == 0 or config.level > 3 or game_boss._health == 0):
            break
        
        time.sleep(0.05)
        

    input.show_cursor()
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)