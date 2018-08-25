# package import
from random import shuffle
import os

# print top
def print_top():
    print('---------------------')
    print(' 暗 棋 遊 戲 ')
    print('---------------------')
    print('\n')

# print main board
def print_board(cur_list):
    print('   0   1   2   3   4   5   6   7')
    for i in range(len(cur_list)):
        print(i, end = '　')
        for j in range(len(cur_list[i])):
            print(cur_list[i][j], end = '　')

            if j == 7:
                print('\n')

# def feed_chess(cur_list, all_chess):
#     counter = 0
#     for i in range(len(cur_list)):
#         for j in range(len(cur_list[i])):
#             cur_list[i][j] = all_chess[counter]
#             counter += 1
#     return cur_list

def player_1_input():
    while 1:
        while 1:
            input_1 = input(['玩家 1 請輸入 x 座標: '])
            try:
                input_1 = int(input_1)
            except:
                input_1 = 'wrong'
        
            if input_1 == 'wrong':
                print('請輸入數值，並介於 0~7 之間')
            elif input_1 > 7 or input_1 < 0:
                print('請勿輸入超出版面大小之 x 座標，需介於 0~7 之間')
            else:
                break

        while 1:
            input_2 = input(['玩家 1 請輸入 y 座標: '])
            try:
                input_2 = int(input_2)
            except:
                input_2 = 'wrong'
        
            if input_2 == 'wrong':
                print('請輸入數值，並介於 0~3 之間')
            elif input_2 > 3 or input_2 < 0:
                print('請勿輸入超出版面大小之 y 座標，需介於 0~3 之間')
            else:
                break

        if cur_list[input_2][input_1] == '　':
            print('請勿選擇空格! 請重新輸入')
        else:
            break

    return [input_1, input_2]

def player_2_input():
    while 1:
        while 1:
            input_1 = input(['玩家 2 請輸入 x 座標: '])
            try:
                input_1 = int(input_1)
            except:
                input_1 = 'wrong'
        
            if input_1 == 'wrong':
                print('請輸入數值，並介於 0~7 之間')
            elif input_1 > 7 or input_1 < 0:
                print('請勿輸入超出版面大小之 x 座標，需介於 0~7 之間')
            else:
                break

        while 1:
            input_2 = input(['玩家 2 請輸入 y 座標: '])
            try:
                input_2 = int(input_2)
            except:
                input_2 = 'wrong'
        
            if input_2 == 'wrong':
                print('請輸入數值，並介於 0~3 之間')
            elif input_2 > 3 or input_2 < 0:
                print('請勿輸入超出版面大小之 y 座標，需介於 0~3 之間')
            else:
                break
    
    return [input_1, input_2]

def chess_beat(x,y):
    while 1:
        while 1:
            input_b_x = input(['請指定 x軸 移動位置: '])
            try:
                input_b_x = int(input_b_x)
            except:
                input_b_x = 'wrong'

            if input_b_x == 'wrong':
                print('請輸入數值，並只能移動一步')
            elif input_b_x > 7 or input_b_x < 0:
                print('超出版面，請介於 0~7 之間')
            else:
                break

        while 1:
            input_b_y = input(['請指定 y軸 移動位置'])
            try:
                input_b_y = int(input_b_y)
            except:
                input_b_y = 'wrong'
        
            if input_b_y == 'wrong':
                print('請輸入數值，並只能移動一步')
            elif input_b_y > 3 or input_b_y < 0:
                print('超出版面，請介於 0~3 之間')
            else:
                break
        
        input_b = [input_b_x, input_b_y]

        if input_b == [x,y]:
            print('你必須移動! 請重新輸入')
        elif input_b != [x-1,y] or input_b != [x+1 ,y] or input_b != [x, y-1] or input_b != [x, y+1]:
            print('你只能移動一步! 請重新輸入')
        elif (cur_list[y][x] in red) and (cur_list[input_b_y][input_b_x] in red):
            print('你不能殺害同隊棋子 (red)! 請重新輸入')
        elif (cur_list[y][x] in black) and (cur_list[input_b_y][input_b_x] in black):
            print('你不能殺害同隊棋子 (black)! 請重新輸入')
        else:
            return input_b
        
# turn or move
def movement_judge(p_input, cur_list):
    x = p_input[0]
    y = p_input[1]
    pos = x * y

    while 1:
        if cur_list[y][x] == '＊':
            cur_list[y][x] = all_chess[pos -1]
            break
        else:
            while 1:
                print('你已經選擇', cur_list[y][x])
                move = chess_beat(x,y)

                cur_chess = cur_list[y][x]
                tar_chess = cur_list[move[1]][move[0]]
            
                try:
                    cur_weight = red.get(cur_chess)
                except:
                    cur_weight = black.get(cur_chess)

                try:
                    tar_weight = red.get(tar_chess)
                except:
                    tar_weight = black.get(tar_chess)

                if cur_weight >= tar_weight:
                    print(cur_chess, ' 吃掉了 ', tar_chess)
                    cur_list[move[1]][move[0]] = cur_list[y][x]
                    break
                else:
                    print('你無法吃掉這顆棋子!', cur_chess, ' 比 ', tar_chess, ' 還要小!')

    return cur_list
            
# para
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

shuffle(all_chess)

# main
os.system('cls')
print_top()
print_board(cur_list)

while 1:
    player_1 = player_1_input()
    cur_list = movement_judge(player_1, cur_list)
    print_board(cur_list)

    player_2 = player_2_input()
    cur_list = movement_judge(player_2, cur_list)
    print_board(cur_list)






    