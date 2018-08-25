# packages
from random import shuffle
import os

# defs

# print main board
def print_board(cur_list, r_b):
    print('---------------------')
    print(' 暗 棋 遊 戲 ')
    print('---------------------')
    print('\n')

    print('   1   2   3   4   5   6   7   8')
    for i in range(len(cur_list)):
        print(i + 1, end = '　')
        for j in range(len(cur_list[i])):
            print(cur_list[i][j], end = '　')

            if j == 7:
                print('\n')

    if r_b == 'red':
        print('玩家 1 為 紅方')
        print('玩家 2 為 黑方')
    elif r_b == 'black':
        print('玩家 1 為 黑方')
        print('玩家 2 為 紅方')
    elif r_b == None:
        pass

    print('紅方失子: ', red_dead)
    print('黑方失子: ', black_dead)

def first_chose(cur_list):
    while 1:
        input_1 = input(['玩家 1 請輸入 x 座標: '])
        try:
            input_1 = int(input_1)
        except:
            input_1 = 'wrong'
        
        if input_1 == 'wrong':
            print('請輸入數值，並介於 1~8 之間')
        elif input_1 > 8 or input_1 < 1:
            print('請勿輸入超出版面大小之 x 座標，需介於 1~8 之間')
        else:
            break

    while 1:
        input_2 = input(['玩家 1 請輸入 y 座標: '])
        try:
            input_2 = int(input_2)
        except:
            input_2 = 'wrong'
        
        if input_2 == 'wrong':
                print('請輸入數值，並介於 1~4 之間')
        elif input_2 > 4 or input_2 < 1:
            print('請勿輸入超出版面大小之 y 座標，需介於 1~4 之間')
        else:
            break
    
    cur_list[input_2 -1][input_1 -1] = all_chess[input_1 * input_2 -1]

    global r_b
    if all_chess[input_1 * input_2 - 1] in red:
        r_b = 'red'
    elif all_chess[input_1 * input_2 -1] in black:
        r_b = 'black'

    return cur_list

def f_movement(side, cur_list):
    situation = None
    while 1:
        while 1:
            input_x = input(['請輸入 x 座標: '])
            try:
                input_x = int(input_x)
            except:
                input_x = 'wrong'

            if input_x == 'wrong':
                print('請輸入數值，並介於 1~8 之間')
            elif input_x > 8 or input_x < 1:
                print('超出版面大小，x 軸請介於 1~8 之間')
            else:
                break
    
        while 1:
            input_y = input(['請輸入 y 座標: '])
            try:
                input_y = int(input_y)
            except:
                input_y = 'wrong'
        
            if input_y == 'wrong':
                print('請輸入數值，並介於 1~4 之間')
            elif input_y > 4 or input_y < 1:
                print('超出版面大小，y 軸請介於 1~4之間')
            else:
                break

        pos = input_y * input_x -1
        input_x = input_x -1
        input_y = input_y -1

        if cur_list[input_y][input_x] == '　':
            print('請勿選擇空格! 請重新輸入')
        elif side == 'red' and (cur_list[input_y][input_x] in black):
            print('請勿選擇非己方之棋子! 請重新輸入 (你現在是紅方)')
        elif side == 'black' and (cur_list[input_y][input_x] in red):
            print('請勿選擇非己方之棋子! 請重新輸入 (你現在是黑方)')
        else:
            break

    cur_chess = cur_list[input_y][input_x]
    if cur_chess == '＊':
        cur_list[input_y][input_x] = all_chess[pos]
        situation = 'flip'
    elif (cur_chess in red) or (cur_chess in black):
        print('你已經選擇 ', cur_chess)
        situation = 'chose'
    
    cur_site = [input_x, input_y]

    return situation, cur_list, cur_site
    
def s_movement(side, cur_site, situation, cur_list, red_dead, black_dead):
    if situation == 'flip':
        pass
    elif situation == 'chose':
        while 1:
            while 1:
                input_x = input(['請輸入行動 x 座標: '])
                try:
                    input_x = int(input_x)
                except:
                    input_x = 'wrong'
        
                if input_x == 'wrong':
                    print('請輸入數值，並介於 1~8 之間')
                elif input_x > 8 or input_x < 1:
                    print('超出版面範圍，請介於 1~8 之間')
                else:
                    break
        
            while 1:
                input_y = input(['請輸入行動 y 座標: '])
                try:
                    input_y = int(input_y)
                except:
                    input_y = 'wrong'

                if input_y == 'wrong':
                    print('請輸入數值，並介於 1~4之間')
                elif input_y > 4 or input_y < 1:
                    print('超出版面範圍，請介於 1~4 之間')
                else:
                    break

            input_x = input_x -1
            input_y = input_y -1
            cur_input = [input_x, input_y]
            x = cur_site[0]
            y = cur_site[1]
            cur_chess = cur_list[y][x]
            tar_chess = cur_list[input_y][input_x]

            if [x+1, y] == cur_input or [x-1, y] == cur_input or [x, y+1] == cur_input or [x,y-1] == cur_input:
                if side == 'black' and (tar_chess in black):
                    print('你無法吃掉同隊的棋子 (黑)!')
                elif side == 'red' and (tar_chess in red):
                    print('你無法吃掉同隊的棋子 (紅)')
                else:
                    if side == 'black':
                        cur_weight = black.get(cur_chess)
                        tar_weight = red.get(tar_chess)
                        break
                    elif side == 'red':
                        cur_weight = red.get(cur_chess)
                        tar_weight = black.get(tar_chess)
                        break
            else:
                print('請勿移動超過一格距離!')
                print(cur_input)
                print([x,y])

        if tar_weight == None:
            cur_list[input_y][input_x] = cur_chess
            cur_list[y][x] = '　'
        elif cur_weight >= tar_weight:
            print(cur_chess, '吃掉了', tar_chess)
            cur_list[input_y][input_x] = cur_list[y][x]
            cur_list[y][x] = '　'
            if side == 'black':
                red_dead.append(tar_chess)
            elif side == 'red':
                black_dead.append(tar_chess)

    return cur_list, red_dead, black_dead
        
def black_movement(cur_list, red_dead, black_dead):
    print('黑方行動')
    situation, cur_list, cur_site = f_movement('black', cur_list)
    cur_list, red_dead, black_dead = s_movement('black', cur_site, situation, cur_list, red_dead, black_dead)
    return cur_list, red_dead, black_dead

def red_movement(cur_list, red_dead, black_dead):
    print('紅方行動')
    situation, cur_list, cur_site = f_movement('red', cur_list)
    cur_list, red_dead, black_dead = s_movement('red', cur_site, situation, cur_list, red_dead, black_dead)
    return cur_list, red_dead, black_dead

def end_game(win):
    os.system('cls')
    print('---------------------')
    print(' 遊 戲 結 束 !')
    print('---------------------')
    print_board(cur_list, r_b)

    if win == 'black':
        print('黑方獲勝 !')
    elif win == 'red':
        print('紅方獲勝 !')

def develope_mode(cur_list, red_dead, black_dead):
    start = input(['請按任意鍵開始... '])

    if start == str(99):
        counter = 0
        for i in range(len(cur_list)):
            for j in range(len(cur_list[i])):
                if counter == 31:
                    continue
                cur_list[i][j] = all_chess[counter]
                counter += 1
    
        os.system('cls')
        print_board(cur_list, r_b)

    elif start == str(98):
        counter = 0
        for i in range(len(cur_list)):
            for j in range(len(cur_list[i])):
                if counter == 31:
                    continue
                cur_list[i][j] = all_chess[counter]
                counter += 1
        red_dead = ['test' for x in range(15)]
        black_dead = ['test' for x in range(15)]

        os.system('cls')
        print_board(cur_list, r_b)
    else:
        pass

    return cur_list, red_dead, black_dead

# params
cur_list = [['＊','＊','＊','＊','＊','＊','＊','＊'],
            ['＊','＊','＊','＊','＊','＊','＊','＊'],
            ['＊','＊','＊','＊','＊','＊','＊','＊'],
            ['＊','＊','＊','＊','＊','＊','＊','＊']]

all_chess = ['帥', '仕', '仕', '相', '相', '俥', '俥', '傌', '傌', '炮', '炮', '兵', '兵', '兵', '兵', '兵',
             '將', '士', '士', '象', '象', '車', '車', '馬', '馬', '砲', '砲', '卒', '卒', '卒', '卒', '卒']       

red = {'帥':7, '仕':6, '相':5, '俥':4, '傌':3, '炮':2, '兵':1}
black = {'將':7, '士':6, '象':5, '車':4, '馬':3, '砲':2, '卒':1}

red_dead = []
black_dead = []
win = None
r_b = None

shuffle(all_chess)

# main
os.system('cls')
print_board(cur_list, r_b)
cur_list, red_dead, black_dead = develope_mode(cur_list, red_dead, black_dead)
cur_list = first_chose(cur_list)

if r_b == 'red':
    while 1:
        os.system('cls')
        print_board(cur_list, r_b)
        cur_list, red_dead, black_dead = black_movement(cur_list, red_dead, black_dead)
        
        if len(red_dead) == 16:
            win = 'black'
            break
        elif len(black_dead) == 16:
            win = 'red'
            break
        
        os.system('cls')
        print_board(cur_list, r_b)
        cur_list, red_dead, black_dead = red_movement(cur_list, red_dead, black_dead)
        os.system('cls')

        if len(red_dead) == 16:
            win = 'black'
            break
        elif len(black_dead) == 16:
            win = 'red'
            break
elif r_b == 'black':
    while 1:
        os.system('cls')
        print_board(cur_list, r_b)
        cur_list, red_dead, black_dead = red_movement(cur_list, red_dead, black_dead)
        
        if len(red_dead) == 16:
            win = 'black'
            break
        elif len(black_dead) == 16:
            win = 'red'
            break
        
        os.system('cls')
        print_board(cur_list, r_b)
        cur_list, red_dead, black_dead = black_movement(cur_list, red_dead, black_dead)
        os.system('cls')   

        if len(red_dead) == 16:
            win = 'black'
            break
        elif len(black_dead) == 16:
            win = 'red'
            break

end_game(win)
os.system('pause')