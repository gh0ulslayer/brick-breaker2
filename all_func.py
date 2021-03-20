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
from bullet import *
from bombs import *
from paddle import *
from ball import *
from boss import *
from brick import *
from powerup import *
from random import *
colorama.init()

#variables start from here
xcoords = []
ycoords = []
rows = config.rows
frames = config.frames
columns = config.columns
game_back = board(rows,columns, frames)

b1 = []

rainbow_stop  = []



game_paddle = movee(config.rows,config.columns)
game_boss = boss(game_paddle._start,game_paddle._paddlelen)
game_brick = brick3(config.rows,config.columns)
game_ball = ball_att()
b4 = []
bombs = []

powerup_2 = []
boss_unbreakable = []


powers = []
powerx = []
powery = []

ball_x = game_ball.get_xpos()
ball_y = game_ball.get_ypos()

balllx = []
ballly = []
for i in range(10):
    b1.append(brick1(7  , 8 + i*7))
for i in range(10):
    b1.append(brick1(8  , 11 + i*7))
for i in range(10):
    b1.append(brick1(9  , 15 + i*7))

rainbow_brick = []
for i in range(3):
    rainbow_brick.append(rainbow(11  , 40 + i*7))
    rainbow_stop.append(0)
# for i in range(10):
    # b1.append(brick1(10  , 13 + i*7))
# for i in range(10):
    # b1.append(brick1(11  , 10 + i*7))
bullet_timer = 0

boss_bomb = Bombs(10,12)

bullet_list1 = []
bullet_list2 = []
for i in range(50):
    bullet_list1.append(bullet(24,game_paddle._start))
for i in range(50):
    bullet_list2.append(bullet(24,game_paddle._start + game_paddle._paddlelen - 1))

for i in range(8):
    b4.append(brick4(4  , 10 + i*10))


for i in range(6):
    bombs.append(bomb_brick(5, 30 + i*5))


for i in range(6):
            boss_unbreakable.append(brick4(8  , 20 + i*8))

for i in range(10):
    boss_unbreakable.append(brick1(10  , 10 + i*8))
for i in range(10):
    boss_unbreakable.append(brick2(11  , 10 + i*8))

for i in range(10):
    var = randint(0,2)
    powers.append(shooting_paddle(b1[3*i + var]._xpos,b1[3*i + var]._ypos))
    powerx.append(b1[3*i+var]._xpos)
    powery.append(b1[3*i+var]._ypos)


powers[3] = shrink_paddle(powerx[3],powery[3])
powers[4] = fast_ball(powerx[4],powery[4])
powers[5] = thru_ball(powerx[5],powery[5])
powers[0] = grab_ball(powerx[0],powery[0])
powers[7] = fast_ball(powerx[7],powery[7])
powers[9] = shrink_paddle(powerx[9],powery[9])

powerup_timer = []
for i in range(10):
    powerup_timer.append(0)
    powerup_2.append(0)

#set level
def set_level():
    if(config.level == 2):
        
        b1.clear()
        b4.clear()
        bombs.clear()
        powers.clear()
        powerx.clear()
        powery.clear()
        powerup_2.clear()

        for i in range(12):
            b1.append(brick1(7  , 8 + i*6))
        for i in range(12):
            b1.append(brick3(9  , 12 + i*6))
        for i in range(12):
            b1.append(brick2(11  , 10 + i*6))


        for i in range(3):
            b4.append(brick4(4  , 30 + i*10))


        for i in range(6):
            bombs.append(bomb_brick(5, 30 + i*5))

                

        for i in range(10):
            var = randint(0,2)
            powers.append(expand_paddle(b1[3*i + var]._xpos,b1[3*i + var]._ypos))
            powerx.append(b1[3*i+var]._xpos)
            powery.append(b1[3*i+var]._ypos)


        powers[3] = shrink_paddle(powerx[3],powery[3])
        powers[4] = fast_ball(powerx[4],powery[4])
        powers[5] = thru_ball(powerx[5],powery[5])
        powers[0] = grab_ball(powerx[0],powery[0])
        powers[7] = fast_ball(powerx[7],powery[7])
        powers[9] = shrink_paddle(powerx[9],powery[9])

        for i in range(10):
            powerup_2.append(0)
            if(powerup_timer[i] > 0):
                powerup_timer[i]= time.time() - 12

    elif(config.level == 3):
        b1.clear()
        b4.clear()
        bombs.clear()
        powers.clear()
        powerx.clear()
        powery.clear()
        config.bomb_flag = 1
        game_paddle.__init__(5,5)
        

      



#functions start from here

#bullets
def show_bullet():
    if(config.bullet_flag == 1):
        for i in range(50):
            newbl = bullet_list2[i]
            if(newbl._left == 0):
                newbl.__init__(24,game_paddle._start + game_paddle._paddlelen - 1)
            game_back._grid[newbl._xpos][newbl._ypos] = newbl.position()[0]
        for i in range(50):
            newbl = bullet_list1[i]
            if(newbl._left == 0):
                newbl.__init__(24,game_paddle._start)
            game_back._grid[newbl._xpos][newbl._ypos] = newbl.position()[0]
        config.bullet_var += 1
        if(config.bullet_var % 2 == 0):
            
            newbl = bullet_list1[0]
            newbl._left = 1
            newbl.x_pos()
            game_back._grid[newbl._xpos][newbl._ypos] = newbl.position()[0]

            newbl1 = bullet_list2[0]
            newbl1._left = 1
            newbl1.x_pos()
            game_back._grid[newbl1._xpos][newbl1._ypos] = newbl1.position()[0]
#filling bomb in the grid

def show_bomb():
    if(config.bomb_flag == 1):
        newbl = boss_bomb
        if(newbl._left == 0):
            newbl.__init__(8,game_paddle._start + game_paddle._paddlelen - 10)
        game_back._grid[newbl._xpos][newbl._ypos] = newbl.position()[0]
        config.bomb_var += 1
        print(config.bomb_var)
        if(config.bomb_var % 2 == 0):
            newbl = boss_bomb
            newbl._left = 1
            newbl.x_pos()
            game_back._grid[newbl._xpos][newbl._ypos] = newbl.position()[0]

#filling ball in grid
def show_ball():
    if(config.grab == 1):
        game_ball._xpos = 23 
        game_ball._ypos =  game_paddle._start + 4 
        game_back._grid[game_ball._xpos][game_ball._ypos] = game_ball.get_ball()

    else:
        game_back._grid[xcoords[0]][ycoords[0]] = game_ball.get_ball()


#powerup run
def powerup_run():
    for i in range(10):
        for j in range(len(b1)):
            if(b1[j]._xpos == powerx[i] and b1[j]._ypos == powery[i]):
                newbr = b1[j]
                if(newbr._level == 0):
                    balllx.append(game_ball._xvel)
                    ballly.append(game_ball._yvel)
                    newpr = powers[i]
                    if(powerup_2[i] == 4):
                        x_newpr = newpr.x_pos()
                        game_back._grid[x_newpr][newpr._ypos] = powers[i].position()[0]
                    else:
                        newpr._xpos -= balllx[0]
                        newpr._ypos += ballly[0]
                        if(newpr._ypos > 88):
                            newpr._ypos = 88
                        if(newpr._ypos < 4):
                            newpr._ypos = 4
                        if(newpr._xpos < 2):
                            newpr._xpos = 2
                        game_back._grid[newpr._xpos][newpr._ypos] = powers[i].position()[0]
                        powerup_2[i]+=1
                    balllx.clear()
                    ballly.clear()
                    
#filling bricks in grid
def show_brick():
    for k in range(len(b1)):
        newbr = b1[k]
        for i in range(game_brick._thick):
            for j in range(game_brick._len):
                game_back._grid[newbr._xpos][newbr._ypos + j] = newbr.get_brick(i,j)
    
    for k in range(len(b4)):
        newbr = b4[k]
        for i in range(game_brick._thick):
            for j in range(game_brick._len):
                game_back._grid[newbr._xpos][newbr._ypos + j] = newbr.get_brick(i,j)
    
    for k in range(len(bombs)):
        newbr = bombs[k]
        for i in range(game_brick._thick):
            for j in range(game_brick._len):
                game_back._grid[newbr._xpos][newbr._ypos + j] = newbr.get_brick(i,j)

    for k in range(len(rainbow_brick)):
        newbr = rainbow_brick[k]
        for i in range(game_brick._thick):
            for j in range(game_brick._len):
                game_back._grid[newbr._xpos][newbr._ypos + j] = newbr.get_brick(i,j)

def boss_brickss():
    if(config.level > 2):
        for k in range(6):
            newbr = boss_unbreakable[k]
            for i in range(game_brick._thick):
                for j in range(game_brick._len):
                    game_back._grid[newbr._xpos][newbr._ypos + j] = newbr.get_brick(i,j)
        for k in range(6):
            newbr = boss_unbreakable[k]
            xstart = newbr._xpos
            xend = newbr._xpos + newbr._thick 
            ystart = newbr._ypos
            yend = newbr._ypos + newbr._len 
            if(newbr._level == 0):
                newbr._visible = 0
            # print(xcoords)
            if(newbr._level > 0):
                if(xcoords[0] > xcoords[1]):
                    if(xcoords[1] == xend):
                            if(yend >= ycoords[1] and  ystart <= ycoords[1]):
                                config.score += 10
                                # print(config.score)
                                if(config.flag_tb == 0):
                                    game_ball._xvel *= -1
                                    newbr._level -= 1
                                else:
                                    newbr._level = 0
                                    newbr._visible = 0
                    if(xcoords[1] == xstart):
                            if(ycoords[1] == ystart or ycoords[1] == yend):
                                config.score += 10
                                # print(config.score)
                                if(config.flag_tb == 0):
                                    game_ball._yvel *= -1
                                    newbr._level -= 1
                                else:
                                    newbr._level = 0
                                    newbr._visible = 0
                else:
                    if(xcoords[1] == xstart):
                        if(yend >= ycoords[1] and  ystart <= ycoords[1]):
                            config.score += 10
                            # print(config.score)
                            if(config.flag_tb == 0):
                                game_ball._xvel *= -1
                                newbr._level -= 1
                            else:
                                newbr._level = 0
                                newbr._visible = 0
                    if(xcoords[1] == xend):
                            if(ycoords[1] == ystart or ycoords[1] == yend):
                                config.score += 10
                                # print(config.score)
                                if(config.flag_tb == 0):
                                    game_ball._yvel *= -1
                                    newbr._level -= 1
                                else:
                                    newbr._level = 0
                                    newbr._visible = 0      
        if(game_boss._health < 7):
            for k in range(6,16):
                newbr = boss_unbreakable[k]
                for i in range(game_brick._thick):
                    for j in range(game_brick._len):
                        game_back._grid[newbr._xpos][newbr._ypos + j] = newbr.get_brick(i,j)
            for k in range(16):
                newbr = boss_unbreakable[k]
                xstart = newbr._xpos
                xend = newbr._xpos + newbr._thick 
                ystart = newbr._ypos
                yend = newbr._ypos + newbr._len 
                if(newbr._level == 0):
                    newbr._visible = 0
                # print(xcoords)
                if(newbr._level > 0):
                    if(xcoords[0] > xcoords[1]):
                        if(xcoords[1] == xend):
                                if(yend >= ycoords[1] and  ystart <= ycoords[1]):
                                    config.score += 10
                                    # print(config.score)
                                    if(config.flag_tb == 0):
                                        game_ball._xvel *= -1
                                        newbr._level -= 1
                                    else:
                                        newbr._level = 0
                                        newbr._visible = 0
                        if(xcoords[1] == xstart):
                                if(ycoords[1] == ystart or ycoords[1] == yend):
                                    config.score += 10
                                    # print(config.score)
                                    if(config.flag_tb == 0):
                                        game_ball._yvel *= -1
                                        newbr._level -= 1
                                    else:
                                        newbr._level = 0
                                        newbr._visible = 0
                    else:
                        if(xcoords[1] == xstart):
                            if(yend >= ycoords[1] and  ystart <= ycoords[1]):
                                config.score += 10
                                # print(config.score)
                                if(config.flag_tb == 0):
                                    game_ball._xvel *= -1
                                    newbr._level -= 1
                                else:
                                    newbr._level = 0
                                    newbr._visible = 0
                        if(xcoords[1] == xend):
                                if(ycoords[1] == ystart or ycoords[1] == yend):
                                    config.score += 10
                                    # print(config.score)
                                    if(config.flag_tb == 0):
                                        game_ball._yvel *= -1
                                        newbr._level -= 1
                                    else:
                                        newbr._level = 0
                                        newbr._visible = 0

        if(game_boss._health < 3):
            for k in range(16,26):
                newbr = boss_unbreakable[k]
                for i in range(game_brick._thick):
                    for j in range(game_brick._len):
                        game_back._grid[newbr._xpos][newbr._ypos + j] = newbr.get_brick(i,j)

            for k in range(len(boss_unbreakable)):
                newbr = boss_unbreakable[k]
                xstart = newbr._xpos
                xend = newbr._xpos + newbr._thick 
                ystart = newbr._ypos
                yend = newbr._ypos + newbr._len 
                if(newbr._level == 0):
                    newbr._visible = 0
                # print(xcoords)
                if(newbr._level > 0):
                    if(xcoords[0] > xcoords[1]):
                        if(xcoords[1] == xend):
                                if(yend >= ycoords[1] and  ystart <= ycoords[1]):
                                    config.score += 10
                                    # print(config.score)
                                    if(config.flag_tb == 0):
                                        game_ball._xvel *= -1
                                        newbr._level -= 1
                                    else:
                                        newbr._level = 0
                                        newbr._visible = 0
                        if(xcoords[1] == xstart):
                                if(ycoords[1] == ystart or ycoords[1] == yend):
                                    config.score += 10
                                    # print(config.score)
                                    if(config.flag_tb == 0):
                                        game_ball._yvel *= -1
                                        newbr._level -= 1
                                    else:
                                        newbr._level = 0
                                        newbr._visible = 0
                    else:
                        if(xcoords[1] == xstart):
                            if(yend >= ycoords[1] and  ystart <= ycoords[1]):
                                config.score += 10
                                # print(config.score)
                                if(config.flag_tb == 0):
                                    game_ball._xvel *= -1
                                    newbr._level -= 1
                                else:
                                    newbr._level = 0
                                    newbr._visible = 0
                        if(xcoords[1] == xend):
                                if(ycoords[1] == ystart or ycoords[1] == yend):
                                    config.score += 10
                                    # print(config.score)
                                    if(config.flag_tb == 0):
                                        game_ball._yvel *= -1
                                        newbr._level -= 1
                                    else:
                                        newbr._level = 0
                                        newbr._visible = 0

        for i in range(len(boss_unbreakable)):
                newbr = boss_unbreakable[i]
                if(newbr._level == 3):
                    boss_unbreakable[i] = brick3(newbr._xpos  , newbr._ypos)
                if(newbr._level == 2):
                    boss_unbreakable[i] = brick2(newbr._xpos  , newbr._ypos)
                if(newbr._level == 1):
                    boss_unbreakable[i] = brick1(newbr._xpos  , newbr._ypos)

        

#brick_run
def brick_run():
    t = time.time()
    if(t - config.time_start > 40):
        for k in range(len(b1)):
            newbr = b1[k]
            xposs = newbr.x_pos()
            for i in range(game_brick._thick):
                for j in range(game_brick._len):
                    game_back._grid[xposs][newbr._ypos + j] = newbr.get_brick(i,j)
        
        for k in range(len(b4)):
            newbr = b4[k]
            for i in range(game_brick._thick):
                for j in range(game_brick._len):
                    game_back._grid[newbr._xpos][newbr._ypos + j] = newbr.get_brick(i,j)
        
        for k in range(len(bombs)):
            newbr = bombs[k]
            for i in range(game_brick._thick):
                for j in range(game_brick._len):
                    game_back._grid[newbr._xpos][newbr._ypos + j] = newbr.get_brick(i,j)
                
        for k in range(len(rainbow_brick)):
            newbr = rainbow_brick[k]
            for i in range(game_brick._thick):
                for j in range(game_brick._len):
                    game_back._grid[newbr._xpos][newbr._ypos + j] = newbr.get_brick(i,j)

#colour change of brick in collision
def colour_change():
    for i in range(len(b1)):
            newbr = b1[i]
            if(newbr._level == 3):
                b1[i] = brick3(newbr._xpos  , newbr._ypos)
            if(newbr._level == 2):
                b1[i] = brick2(newbr._xpos  , newbr._ypos)
            if(newbr._level == 1):
                b1[i] = brick1(newbr._xpos  , newbr._ypos)

    for i in range(len(rainbow_brick)):
            newbr = rainbow_brick[i]
            if(rainbow_stop[i] == 0):
                if(newbr._level == 3):
                    rainbow_brick[i] = brick1(newbr._xpos  , newbr._ypos)
                    newbr._level = 1
                if(newbr._level == 2):
                    rainbow_brick[i] = brick3(newbr._xpos  , newbr._ypos)
                    newbr._level = 3
                if(newbr._level == 1):
                    rainbow_brick[i] = brick2(newbr._xpos  , newbr._ypos)
                    newbr._level = 2
            else:
                if(newbr._level == 3):
                    rainbow_brick[i] = brick3(newbr._xpos  , newbr._ypos)
                if(newbr._level == 2):
                    rainbow_brick[i] = brick2(newbr._xpos  , newbr._ypos)
                if(newbr._level == 1):
                    rainbow_brick[i] = brick1(newbr._xpos  , newbr._ypos)


#collsion between ball and paddle
def coll_paddle():
    if(ball_y > game_paddle._start and ball_y < game_paddle._start + game_paddle._paddlelen and ball_x == 24):
        config.flag = 1
        brick_run()
        os.system('aplay -q main.wav&')

        if(config.flag_gb == 1):
            config.grab = 1
        else:
            if(ball_y < game_paddle._start + game_paddle._paddlelen/4):
                game_ball._yvel -= 2
            elif(ball_y < game_paddle._start + game_paddle._paddlelen/2):
                game_ball._yvel -= 1
            elif(ball_y < game_paddle._start + game_paddle._paddlelen*3/4):
                game_ball._yvel += 1
            else:
                game_ball._yvel += 2


#collision between powerup and paddle
def coll_powerup():
    for i in range(10):
        newpr = powers[i]
        if( newpr._ypos > game_paddle._start and newpr._ypos < game_paddle._start + game_paddle._paddlelen and newpr._xpos == 24):
            powers[i]._catched = 1
            powerup_timer[i]= time.time()

#activating the powerup
def activating_powerup(): 
    for i in range(10):
        newpr = powers[i]
        if(newpr._catched == 1):
            if(newpr.position()[0] == Fore.WHITE + '►'):
                game_paddle._paddlelen += 2
                game_paddle.change_paddle()
            elif(newpr.position()[0] == Fore.WHITE + '◄'):
                game_paddle._paddlelen -= 2
                game_paddle.change_paddle()
            elif(newpr.position()[0] == Fore.WHITE + 'F'):
                game_ball._yvel += 2
            elif(newpr.position()[0] == Fore.WHITE + 'T'):
                    config.flag_tb = 1
            elif(newpr.position()[0] == Fore.WHITE + 'G'):
                    config.flag_gb = 1
            elif(newpr.position()[0] == Fore.WHITE + 'Y'):
                    config.bullet_flag = 1
                    config.bullett_time = time.time()
                    game_paddle.__init__(1,1)
            newpr._catched = 0 


#powerup deactivate
def powerup_deactivate():
    for i in range(10):
        newpr = powers[i]
        t = time.time()
        
        if(powerup_timer[i] > 0):
            # print(powerup_timer[i],t)

            if(t - powerup_timer[i] > 10 ):
                if(newpr.position()[0] == Fore.WHITE + '►'):
                    game_paddle._paddlelen -= 2
                    game_paddle.change_paddle()
                elif(newpr.position()[0] == Fore.WHITE + '◄'):
                    game_paddle._paddlelen += 2
                    game_paddle.change_paddle()
                elif(newpr.position()[0] == Fore.WHITE + 'F'):
                    game_ball._yvel -= 2
                elif(newpr.position()[0] == Fore.WHITE + 'T'):
                        config.flag_tb = 0
                elif(newpr.position()[0] == Fore.WHITE + 'G'):
                        config.flag_gb = 0
                elif(newpr.position()[0] == Fore.WHITE + 'Y'):
                    config.bullet_flag = 0
                    config.bullett_time = 0
                    game_paddle.__init__(1,1)
                powerup_timer[i] = 0


            newpr._catched = 0 
    
#level_up
def level_up():
    varrrr = 0
    for i in range(len(b1)):
        newbr = b1[i]
        if(newbr._level > 0):
            varrrr = 1
    for i in range(len(bombs)):
        newbr = bombs[i]
        if(newbr._level > 0):
            varrrr = 1

    if(varrrr == 0):
        if(config.level == 1):
            config.level = 2
            config.grab = 1
            game_ball._xvel = -1
            game_ball._yvel = 1
            set_level()
        elif(config.level == 2):
            config.level = 3
            config.grab = 1
            game_ball._xvel = -1
            game_ball._yvel = 1
            set_level()
        elif(config.level == 3):
            config.level = 4
            config.grab = 1
            set_level()
            game_ball._xvel = -1
            game_ball._yvel = 1

#printing grid
def show_grid():
    output_str = ""
    for row in range(rows):
        for col in range(columns):
                output_str += game_back.get_grid(row,col)
        output_str += '\n'
    
    arr = []
    arr.append(config.lives)
    arr.append(config.score)
    config.time_played = time.time() - config.time_start
    arr.append(config.time_played)
    arr.append(config.level)
    arr.append(game_boss._health)
    x = time.time() - config.bullett_time
    if(config.bullett_time == 0):
        x = 10
    arr.append(10-x)


    output_str += "Lives_remaining = "
    output_str += str(arr[0])
    output_str += "     "
    output_str += "Score = "
    output_str += str(arr[1])
    output_str += "     "
    output_str += "Time_played = "
    output_str += str(arr[2])
    output_str += "     "
    output_str += "Level = "
    output_str += str(arr[3])
    output_str += "     "
    output_str += "Boss Health = "
    output_str += str(arr[4])
    output_str += "     "
    output_str += "Bullet Time remaining = "
    output_str += str(arr[5])
    output_str += " "
    output_str += '\n'

    print('\033[H' + output_str)
    

#clearing the grid
def clear_grid():
    for i in range(1,config.rows-1):
            for j in range(1,config.columns-1):
                game_back._grid[i][j] = ' '
        
    if(config.lives == 0 or config.level > 3 or game_boss._health == 0): 
        for i in range(1,config.rows-1):
            for j in range(1,config.columns-1):
                game_back._grid[i][j] = ' '
            
        game_back._grid[15][40] = Fore.RED  + 'G'
        game_back._grid[15][41] = Fore.RED  + 'A'
        game_back._grid[15][42] = Fore.RED  + 'M'
        game_back._grid[15][43] = Fore.RED  + 'E'
        game_back._grid[15][46] = Fore.RED  + 'O'
        game_back._grid[15][47] = Fore.RED  + 'V'
        game_back._grid[15][48] = Fore.RED  + 'E'
        game_back._grid[15][49] = Fore.RED  + 'R'

        output_strr = ""
        for row in range(rows):
            for col in range(columns):
                    output_strr += game_back.get_grid(row,col)
            output_strr += '\n'
        print('\033[H' + output_strr)
        os.system('aplay -q 1.wav&')

        
#collison of brick with ball
def coll_brick():
    for k in range(len(b1)):
        newbr = b1[k]
        xstart = newbr._xpos
        xend = newbr._xpos + newbr._thick 
        ystart = newbr._ypos
        yend = newbr._ypos + newbr._len 
        if(newbr._level == 0):
            newbr._visible = 0
        # print(xcoords)
        if(newbr._level > 0):
            if(xcoords[0] > xcoords[1]):
                if(xcoords[1] == xend):
                        if(yend >= ycoords[1] and  ystart <= ycoords[1]):
                            config.score += 10
                            # print(config.score)
                            if(fire_flag == 1):
                                newbr._level = 0

                            if(config.flag_tb == 0):
                                game_ball._xvel *= -1
                                newbr._level -= 1
                            else:
                                newbr._level = 0
                                newbr._visible = 0
                if(xcoords[1] == xstart):
                        if(ycoords[1] == ystart or ycoords[1] == yend):
                            config.score += 10
                            # print(config.score)
                            if(config.flag_tb == 0):
                                game_ball._yvel *= -1
                                newbr._level -= 1
                            else:
                                newbr._level = 0
                                newbr._visible = 0
            else:
                if(xcoords[1] == xstart):
                    if(yend >= ycoords[1] and  ystart <= ycoords[1]):
                        config.score += 10
                        # print(config.score)
                        if(config.flag_tb == 0):
                            game_ball._xvel *= -1
                            newbr._level -= 1
                        else:
                            newbr._level = 0
                            newbr._visible = 0
                if(xcoords[1] == xend):
                        if(ycoords[1] == ystart or ycoords[1] == yend):
                            config.score += 10
                            # print(config.score)
                            if(config.flag_tb == 0):
                                game_ball._yvel *= -1
                                newbr._level -= 1
                            else:
                                newbr._level = 0
                                newbr._visible = 0
    
    for k in range(len(b4)):
        newbr = b4[k]
        xstart = newbr._xpos
        xend = newbr._xpos + newbr._thick 
        ystart = newbr._ypos
        yend = newbr._ypos + newbr._len 
        if(newbr._level > 0):
            if(xcoords[0] > xcoords[1]):
                if(xcoords[1] == xend):
                    if(yend >= ycoords[1] and  ystart <= ycoords[1]):
                        config.score += 10
                        # print(config.score)
                        if(config.flag_tb == 0):
                            game_ball._xvel *= -1
                        else:
                            newbr._level = 0
                            newbr._visible = 0
                if(xcoords[1] == xstart):
                    if(ycoords[1] == ystart or ycoords[1] == yend):
                        config.score += 10
                        # print(config.score)
                        if(config.flag_tb == 0):
                            game_ball._yvel *= -1
                        else:
                            newbr._level = 0
                            newbr._visible = 0
            else:
                if(xcoords[0] > xcoords[1]):
                    if(xcoords[1] == xstart):
                        if(yend >= ycoords[1] and  ystart <= ycoords[1]):
                            config.score += 10
                            # print(config.score)
                            if(config.flag_tb == 0):
                                game_ball._xvel *= -1
                            else:
                                newbr._level = 0
                                newbr._visible = 0
                    if(xcoords[1] == xend):
                        if(ycoords[1] == ystart or ycoords[1] == yend):
                            config.score += 10
                            # print(config.score)
                            if(config.flag_tb == 0):
                                game_ball._yvel *= -1
                            else:
                                newbr._level = 0
                                newbr._visible = 0
    
    for k in range(len(rainbow_brick)):
        newbr = rainbow_brick[k]
        xstart = newbr._xpos
        xend = newbr._xpos + newbr._thick 
        ystart = newbr._ypos
        yend = newbr._ypos + newbr._len 
        
        if(newbr._level > 0 ):
            if(xcoords[0] > xcoords[1]):
                if(xcoords[1] == xend):
                    if(yend >= ycoords[1] and  ystart <= ycoords[1]):
                        config.score += 10
                        # print(config.score)
                        rainbow_stop[k] = 1
                        if(config.flag_tb == 0):
                            newbr._level -=1
                            game_ball._xvel *= -1
                        else:
                            newbr._level = 0
                            newbr._visible = 0
                if(xcoords[1] == xstart):
                    if(ycoords[1] == ystart or ycoords[1] == yend):
                        config.score += 10
                        rainbow_stop[k] = 1
                        # print(config.score)
                        if(config.flag_tb == 0):
                            newbr._level -=1
                            game_ball._yvel *= -1
                        else:
                            newbr._level = 0
                            newbr._visible = 0
            else:
                if(xcoords[0] > xcoords[1]):
                    if(xcoords[1] == xstart):
                        if(yend >= ycoords[1] and  ystart <= ycoords[1]):
                            config.score += 10
                            rainbow_stop[k] = 1
                            # print(config.score)
                            if(config.flag_tb == 0):
                                newbr._level -=1
                                game_ball._xvel *= -1
                            else:
                                newbr._level = 0
                                newbr._visible = 0
                    if(xcoords[1] == xend):
                        if(ycoords[1] == ystart or ycoords[1] == yend):
                            config.score += 10
                            rainbow_stop[k] = 1
                            # print(config.score)
                            if(config.flag_tb == 0):
                                newbr._level -=1
                                game_ball._yvel *= -1
                            else:
                                newbr._level = 0
                                newbr._visible = 0        
                

#collision for explosive bricks
def coll_explosive():
    for k in range(len(bombs)):
        newbr = bombs[k]
        xstart = newbr._xpos
        xend = newbr._xpos + newbr._thick 
        ystart = newbr._ypos
        yend = newbr._ypos + newbr._len 
        
        if(newbr._level == 0):
            newbr._visible = 0
            for i in range(len(b1)):
                topleftx = b1[i]._xpos
                toplefty = b1[i]._ypos
                bottomleftx = b1[i]._xpos + b1[i]._thick 
                bottomlefty = b1[i]._ypos 
                toprightx = b1[i]._xpos
                toprighty = b1[i]._ypos + b1[i]._len
                bottomrightx = b1[i]._xpos + b1[i]._thick
                bottomrighty = b1[i]._ypos + b1[i]._len

                if(xstart == bottomleftx):
                    if(ystart >= bottomlefty and ystart <= bottomrighty):
                        b1[i]._level = 0
                        b1[i]._visible = 0
                    if(yend >= bottomlefty and yend <= bottomrighty):
                        b1[i]._visible = 0
                        b1[i]._level = 0
                if(xend == topleftx):
                    if(ystart >= bottomlefty and ystart <= bottomrighty):
                        b1[i]._visible = 0
                        b1[i]._level = 0
                    if(yend >= bottomlefty and yend <= bottomrighty):
                        b1[i]._visible = 0
                        b1[i]._level = 0
                if(ystart == toprighty):
                    if(xstart == topleftx):
                        b1[i]._visible = 0
                        b1[i]._level = 0
                if(yend == toplefty):
                    if(xstart == topleftx):
                        b1[i]._visible = 0
                        b1[i]._level = 0
            
            for i in range(len(b4)):
                topleftx = b4[i]._xpos
                toplefty = b4[i]._ypos
                bottomleftx = b4[i]._xpos + b1[i]._thick 
                bottomlefty = b4[i]._ypos 
                toprightx = b4[i]._xpos
                toprighty = b4[i]._ypos + b1[i]._len
                bottomrightx = b4[i]._xpos + b1[i]._thick
                bottomrighty = b4[i]._ypos + b1[i]._len

                if(xstart == bottomleftx):
                    if(ystart >= bottomlefty and ystart <= bottomrighty):
                        b4[i]._level = 0
                        b4[i]._visible = 0
                    if(yend >= bottomlefty and yend <= bottomrighty):
                        b4[i]._visible = 0
                        b4[i]._level = 0
                if(xend == topleftx):
                    if(ystart >= bottomlefty and ystart <= bottomrighty):
                        b4[i]._visible = 0
                        b4[i]._level = 0
                    if(yend >= bottomlefty and yend <= bottomrighty):
                        b4[i]._visible = 0
                        b4[i]._level = 0
                if(ystart == toprighty):
                    if(xstart == topleftx):
                        b4[i]._visible = 0
                        b4[i]._level = 0
                if(yend == toplefty):
                    if(xstart == topleftx):
                        b4[i]._visible = 0
                        b4[i]._level = 0
            if(k == 5):
                bombs[k-1]._level = 0
            elif(k==0):
                bombs[k+1]._level = 0
            else:
                bombs[k+1]._level = 0
                bombs[k-1]._level = 0

        
            

        if(newbr._level > 0):
            if(xcoords[0] > xcoords[1]):
                if(xcoords[1] == xend):
                        if(yend >= ycoords[1] and  ystart <= ycoords[1]):
                            config.score += 10
                            # print(config.score)
                            if(config.flag_tb == 0):
                                game_ball._xvel *= -1
                                newbr._level -= 1
                            else:
                                newbr._level = 0
                                newbr._visible = 0
                if(xcoords[1] == xstart):
                        if(ycoords[1] == ystart or ycoords[1] == yend):
                            config.score += 10
                            # print(config.score)
                            if(config.flag_tb == 0):
                                game_ball._yvel *= -1
                                newbr._level -= 1
                            else:
                                newbr._level = 0
                                newbr._visible = 0
            else:
                if(xcoords[1] == xstart):
                    if(yend >= ycoords[1] and  ystart <= ycoords[1]):
                        config.score += 10
                        # print(config.score)
                        if(config.flag_tb == 0):
                            game_ball._xvel *= -1
                            newbr._level -= 1
                        else:
                            newbr._level = 0
                            newbr._visible = 0
                if(xcoords[1] == xend):
                        if(ycoords[1] == ystart or ycoords[1] == yend):
                            config.score += 10
                            # print(config.score)
                            if(config.flag_tb == 0):
                                game_ball._yvel *= -1
                                newbr._level -= 1
                            else:
                                newbr._level = 0
                                newbr._visible = 0

#collision with bullet
def coll_bullet():
    for k in range(len(b1)):
        newbr = b1[k]
        ystart = newbr._ypos
        yend = newbr._ypos + newbr._len 
        if(newbr._level == 0):
            newbr._visible = 0
        # print(xcoords)
        if(newbr._level > 0):
            bll = bullet_list1[0]
            bll1 = bullet_list2[0]
            if(bll._xpos == newbr._xpos):
                if(bll._ypos > ystart and bll._ypos < yend ):
                    newbr._level -= 1
                    bll._left = 0
            if(bll1._xpos == newbr._xpos):
                if(bll1._ypos > ystart and bll1._ypos < yend ):
                    bll1._left = 0
                    newbr._level -= 1
    for k in range(len(b4)):
        newbr = b4[k]
        ystart = newbr._ypos
        yend = newbr._ypos + newbr._len 
        if(newbr._level == 0):
            newbr._visible = 0
        # print(xcoords)
        if(newbr._level > 0):
            bll = bullet_list1[0]
            bll1 = bullet_list2[0]
            if(bll._xpos == newbr._xpos):
                if(bll._ypos > ystart and bll._ypos < yend ):
                    newbr._level -= 1
                    bll._left = 0
            if(bll1._xpos == newbr._xpos):
                if(bll1._ypos > ystart and bll1._ypos < yend ):
                    bll1._left = 0
                    newbr._level -= 1
    for k in range(len(rainbow_brick)):
        newbr = rainbow_brick[k]
        ystart = newbr._ypos
        yend = newbr._ypos + newbr._len 
        if(newbr._level == 0):
            newbr._visible = 0
        # print(xcoords)
        if(newbr._level > 0):
            bll = bullet_list1[0]
            bll1 = bullet_list2[0]
            if(bll._xpos == newbr._xpos):
                if(bll._ypos > ystart and bll._ypos < yend ):
                    newbr._level -= 1
                    bll._left = 0
            if(bll1._xpos == newbr._xpos):
                if(bll1._ypos > ystart and bll1._ypos < yend ):
                    bll1._left = 0
                    newbr._level -= 1
    
#collision with boss
def coll_boss():
    if(game_boss._health > 0 and config.level > 2):
        xstart = 5
        xend =  8
        ystart = game_paddle._start
        yend = game_paddle._start + game_paddle._paddlelen 
        if(xcoords[0] > xcoords[1]):
                if(xcoords[1] == xend):
                    if(yend >= ycoords[1] and  ystart <= ycoords[1]):
                        config.score += 10
                        game_ball._xvel *= -1
                        game_boss._health -=1
                if(xcoords[1] == xstart):
                    if(ycoords[1] == ystart or ycoords[1] == yend):
                        config.score += 10
                        game_boss._health -=1
                        game_ball._yvel *= -1
        else:
            if(xcoords[1] == xstart):
                if(yend >= ycoords[1] and  ystart <= ycoords[1]):
                    config.score += 10
                    game_boss._health -=1
                    game_ball._xvel *= -1
            if(xcoords[1] == xend):
                if(ycoords[1] == ystart or ycoords[1] == yend):
                    config.score += 10
                    game_boss._health -=1
                    game_ball._yvel *= -1