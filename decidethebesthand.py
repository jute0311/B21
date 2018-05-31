import random
import time

from blokus.piece import Pieces
from blokus.utils import encodeFourCode

from players.B21.makealllegalhands import *

from players.B21.selectways import *

'''
合法手の中から最適手を選ぶ関数

＜最終目標＞
    countの値、fieldの状況に応じたその時その時にどの評価関数を使うかをAIに決めさせる

残りの課題
・終盤の読み（実際に埋めて考える、自分の領域を把握する）
・自分の領域を広げる（あいての角に入っていく。ある程度完成。のこりは入った後に自分領域が増えているかの評価をつける）


all_legalhands[0] = 'piece name'
all_legalhands[1] = 回転度合い
all_legalhands[2] = 中心までの距離を示す値
all_legalhands[3] = center_i
all_legalhands[4] = center_j
all_legalhands[5] = そのpieceを入れた後のfield
all_legalhands[6] = 置いた場所のi座標
all_legalhands[7] = 置いた場所のj座標

追加禁止

'''

def decideTheBestHand(number,field,player1,pieces,count,board) :

    the_best_hand = ''    #選ばれたピースを格納する変数の初期化

    survived_legalhands = {}

    all_legalhands = getAllLegalhands(field,player1,pieces)

    if all_legalhands == {} :
        print(pieces)
        return 'pass'

    else:
        '''
        ここの評価基準を複雑化していく
        '''

        #1番手と２番手の時だけ適用にする
        if count == 4 :
            survived_legalhands = all_legalhands #実行する条件を選ぶ
            
            if len(survived_legalhands) != 1:
                survived_legalhands = selectBySizeOfPiece(survived_legalhands)
                #print("1 : {0}".format(len(survived_legalhands)))

            if len(survived_legalhands) != 1:
                survived_legalhands = interference(survived_legalhands,board)
                #print("4 : {0}".format(len(survived_legalhands)))

            if len(survived_legalhands) != 1:
                survived_legalhands = selectByPutPlace(survived_legalhands)
                #print("2 : {0}".format(len(survived_legalhands)))

            if len(survived_legalhands) != 1:
                survived_legalhands = selectByPutedPlace(survived_legalhands,field)
                #print("3 : {0}".format(len(survived_legalhands)))

        elif count <= 10 :
            survived_legalhands = all_legalhands
            
            if len(survived_legalhands) != 1:
                survived_legalhands = selectBySizeOfPiece(survived_legalhands)
                #print("1 : {0}".format(len(survived_legalhands)))

            if len(survived_legalhands) != 1:
                survived_legalhands = filter(survived_legalhands,player1)
                #print("2 : {0}".format(len(survived_legalhands))) #重い
            
            if len(survived_legalhands) != 1:
                survived_legalhands = selectSmartlybf(survived_legalhands,field,player1)
                #print("3 : {0}".format(len(survived_legalhands)))
            
            if len(survived_legalhands) != 1:
                survived_legalhands = selectSmartly2(survived_legalhands,player1,pieces,count)
                #print("4 : {0}".format(len(survived_legalhands))) #重い

            if len(survived_legalhands) != 1:
                survived_legalhands = interference(survived_legalhands,board)
                #print("4 : {0}".format(len(survived_legalhands)))
            
            if len(survived_legalhands) != 1:
                survived_legalhands = selectByPutedPlace(survived_legalhands,field)
                #print("7 : {0}".format(len(survived_legalhands)))

        elif 11 <= count <= 15 :
            survived_legalhands = all_legalhands

            if len(survived_legalhands) != 1:
                survived_legalhands = filter(survived_legalhands,player1)
                #print("2 : {0}".format(len(survived_legalhands))) #重い

            if len(survived_legalhands) != 1:
                survived_legalhands = selectSmartly2(survived_legalhands,player1,pieces,count)
                #print("4 : {0}".format(len(survived_legalhands))) #重い
            
            if len(survived_legalhands) != 1:
                survived_legalhands = selectBySizeOfPiece(survived_legalhands)
                #print("1 : {0}".format(len(survived_legalhands)))

            if len(survived_legalhands) != 1:
                survived_legalhands = selectSmartlybf(survived_legalhands,field,player1)
                #print("3 : {0}".format(len(survived_legalhands)))

            if len(survived_legalhands) != 1:
                survived_legalhands = interference(survived_legalhands,board)
                #print("4 : {0}".format(len(survived_legalhands)))
            
            if len(survived_legalhands) != 1:
                survived_legalhands = selectByPutedPlace(survived_legalhands,field)
                #print("7 : {0}".format(len(survived_legalhands)))
        
        elif 15 < count :
            survived_legalhands = all_legalhands #実行する条件を選ぶ
            if len(survived_legalhands) != 1:
                survived_legalhands  = filter(survived_legalhands,player1)
                #print("1 : {0}".format(len(survived_legalhands)))
            
            if len(survived_legalhands) != 1:
                survived_legalhands  = onlyMe(survived_legalhands,board)
                #print("1 : {0}".format(len(survived_legalhands)))

            if len(survived_legalhands) != 1:
                survived_legalhands = selectSmartly2(survived_legalhands,player1,pieces,count)
                #print("2 : {0}".format(len(survived_legalhands)))

            if len(survived_legalhands) != 1:
                survived_legalhands = selectBySizeOfPiece(survived_legalhands)
                #print("3 : {0}".format(len(survived_legalhands)))


        name, val =random.choice(list(survived_legalhands.items()))
        the_best_hand = name

        return encodeFourCode(survived_legalhands[the_best_hand][3],\
                              survived_legalhands[the_best_hand][4],\
                              survived_legalhands[the_best_hand][0],\
                              survived_legalhands[the_best_hand][1])
