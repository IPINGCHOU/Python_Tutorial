# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 03:18:04 2018

@author: kami
"""

#%%
import os
import random

#%%
# 用來顯示標題
def print_start_board():
    print('-----------------')
    print(' 剪刀石頭布遊戲')
    print('-----------------')
    print('\n')


#%%
# 用來顯示遊戲結束畫面
def print_end_board(mode, score):
    print('-----------------')
    print(' 遊戲結束 !!')
    print('-----------------')
    print('\n')
    print('最終比數 : ' + str(score[0]) + ' : ' + str(score[1]))
    print('\n')
    
    if score[0] > score[1]:
        print('------------')
        print(' 玩家 1 勝利 ')
        print('------------')
        os.system('pause')
    elif score[1] > score[0]:
        if mode == 1:
            print('------------')
            print(' 玩家 2 勝利 ')
            print('------------')
            os.system('pause')
        elif mode == 2:
            print('------------')
            print(' 電腦 勝利 ')
            print('------------')
            os.system('pause')
        
    elif score[0] == score[1]:
        print('------------')
        print('   平 手    ')
        print('------------')
        os.system('pause')
    
    
#%%
# 2p mode 寫法
# 回傳玩家 1 輸出以及 玩家 2 輸出
def two_player_input():

    while 1:
        input_p1 = input(['玩家 1 請選擇: 剪刀 = 1, 石頭 = 2, 布 = 3 '])
        try:
            input_p1 = int(input_p1)
        except:
            input_p1 = int(4)
        # 偵錯用，防止輸入非 1 2 3的結果
        if input_p1 == 1 or input_p1 == 2 or input_p1 == 3:
            break
        else:
            print('請輸入正確的代號 !')
    
    os.system('cls')
    print_start_board()
    
    while 1:
        input_p2 = input(['玩家 2 請選擇: 剪刀 = 1, 石頭 = 2, 布 = 3 '])
        try:
            input_p2 = int(input_p2)
        except:
            input_p2 = int(4)
        
        if input_p2 == 1 or input_p2 == 2 or input_p2 == 3:
            break
        else:
            print('請輸入正確的代號 !')
    
    return input_p1, input_p2

#%%
# 與電腦對戰模式
def player_com_input():
    
    while 1:
        input_p1 = input(['玩家 1 請選擇: 剪刀 = 1, 石頭 = 2, 布 = 3 '])
        try:
            input_p1 = int(input_p1)
        except:
            input_p1 = int(4)
        
        if input_p1 == 1 or input_p1 == 2 or input_p1 == 3:
            break
        else:
            print('請輸入正確的代號 !')
    
    # 讓電腦隨機出拳
    com = random.randint(1, 3)
    
    if com == 1:
        print('電腦出 剪刀')
    elif com == 2:
        print('電腦出 石頭')
    elif com == 3:
        print('電腦出 布')
    
    return input_p1, com

#%%
# 顯示雙方各出了甚麼
def display_the_chose(input_1, input_2, mode):
    print('\n')
    input_1 = int(input_1)
    input_2 = int(input_2)

    if input_1 == 1:
        input_1 = '剪刀'
    elif input_1 == 2:
        input_1 = '石頭'
    elif input_1 == 3:
        input_1 = '布'
    
    if input_2 == 1:
        input_2 = '剪刀'
    elif input_2 == 2:
        input_2 = '石頭'
    elif input_2 == 3:
        input_2 = '布'
    
    if mode == 1:
        print('玩家 1  v.s.  玩家 2')
        print(' ' + input_1 + '          ' + input_2)
    elif mode == 2:
        print('玩家 1  v.s.  電腦')
        print(' ' + input_1 + '          ' + input_2)
          
#%%
# 用來判斷雙方誰輸誰贏
def win_lose_judge(input_1, input_2):
    input_1 = int(input_1)
    input_2 = int(input_2)
    
    if input_1 == 1:
        if input_2 == 1:
            return [0,0]
        elif input_2 == 2:
            return [0,1]
        elif input_2 == 3:
            return [1,0]
    elif input_1 == 2:
        if input_2 == 1:
            return [1,0]
        elif input_2 == 2:
            return [0,0]
        elif input_2 == 3:
            return [0,1]
    elif input_1 == 3:
        if input_2 == 1:
            return [0,1]
        elif input_2 == 2:
            return [1,0]
        elif input_2 == 3:
            return [0,0]

#%%
# 選擇模式用
def mode_chose_fun():
    mode_chose = input(['請選擇 PVP 或 COM : PVP = 1 , COM = 2, 離開 = 0'])
    try:
        mode_chose = int(mode_chose)
    except:
        mode_chose = int(4)
    
    # 偵錯用，防止輸入非 1 2 0
    if mode_chose == 1 or mode_chose == 2 or mode_chose == 3 or mode_chose == 0:
        return mode_chose
    else:
        print('請輸入正確代號 !')
        mode_chose_fun()
#%%
# main
while 1:
    # os.system('cls')用來清理cmd顯示畫面
    # 清理後顯示開頭畫面以及模式選擇
    os.system('cls')
    print_start_board()
    mode_chose = mode_chose_fun()
    
    # 若是選擇 0 ，便離開 (關閉程式)
    if mode_chose == 0:
        break
    
    # 若非 ，則選擇要玩幾盤
    # 初始化 score 參數
    round_input = int(input(['請輸入遊玩回數: ']))
    score = [0,0]
    os.system('cls')
    
    for i in range(round_input):
        print_start_board()
        # 若選擇 1 為 pvp
        if mode_chose == 1:
            print('當前模式: PVP')
            print('選擇遊玩回數 : ' + str(round_input))
            print('目前比數 : ' + str(score[0]) + ' : ' + str(score[1]))
            # 呼叫 two_player_input 來得到雙方玩家的 input
            # 丟進去 display_the_chose 來顯示雙方的選擇
            # 丟進去 win_lose_judge來判斷輸贏
            input_p1, input_p2 = two_player_input()
            display_the_chose(input_p1, input_p2, mode_chose)
            win_lose = win_lose_judge(input_p1, input_p2)
            
            # 根據 win_lose_judge的結果來顯示該回合輸贏
            if win_lose == [0,0]:
                print('平手!')
            elif win_lose == [1,0]:
                print('玩家 1 勝利!')
                score[0] += 1
            elif win_lose == [0,1]:
                print('玩家 2 勝利!')
                score[1] += 1
        # 若選擇 2 
        elif mode_chose == 2:
            print('當前模式: COM')
            print('選擇遊玩回數 : ' + str(round_input))
            print('目前比數 : ' + str(score[0]) + ' : ' + str(score[1]))
            input_p1, input_p2 = player_com_input()
            display_the_chose(input_p1, input_p2, mode_chose)
            win_lose = win_lose_judge(input_p1, input_p2)
        
            if win_lose == [0,0]:
                print('平手!')
            elif win_lose == [1,0]:
                print('玩家 1 勝利!')
                score[0] += 1
            elif win_lose == [0,1]:
                print('電腦 勝利!')
                score[1] += 1
        
        # 當進行到最後一局
        # 執行 print_end_board 顯示最後結果以及誰輸誰贏
        if i == round_input - 1:     
            print_end_board(mode_chose, score)
            break
        
        # 若是尚未到最後一局
        # 先讓系統暫停 按任意鍵繼續
        # 清空 cmd 畫面
        # 重複迴圈
        else:
            os.system('pause')
            os.system('cls')
            
