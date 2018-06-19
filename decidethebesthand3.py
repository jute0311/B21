import random
import time

from blokus.piece import Pieces
from blokus.utils import encodeFourCode

from players.B21.makealllegalhands import *

from players.B21.selectways import *

'''
合法手の中から最適手を選ぶ関数
'''

def decideTheBestHand3(number,field,player1,pieces,count,board) :

    the_best_hand = ''    #選ばれたピースを格納する変数の初期化

    survived_legalhands = {}

    all_legalhands = getAllLegalhands(field,player1,pieces)

    if all_legalhands == {} :
        return 'pass'

    else:
        survived_legalhands = all_legalhands
        print("{0}回目".format(count))

        if count <= 7:
            if len(survived_legalhands) != 1:
                survived_legalhands = selectBySizeOfPiece(survived_legalhands)
                print("1 : {0}".format(len(survived_legalhands)))

            if len(survived_legalhands) != 1:
                survived_legalhands = getEnterSpace(survived_legalhands,board)
                print("2 : {0}".format(len(survived_legalhands)))

            if len(survived_legalhands) != 1:
                survived_legalhands = interference(survived_legalhands,board)
                print("7 : {0}".format(len(survived_legalhands)))

            if len(survived_legalhands) != 1:
                survived_legalhands = findSpace2(survived_legalhands,player1,board)
                print("11 : {0}".format(len(survived_legalhands)))

            if len(survived_legalhands) != 1:
                survived_legalhands = defence(survived_legalhands,board)
                print("4 : {0}".format(len(survived_legalhands)))

            if len(survived_legalhands) != 1:
                survived_legalhands = selectSmartlybf(survived_legalhands,field,player1,count)
                print("5 : {0}".format(len(survived_legalhands)))
            
            if len(survived_legalhands) != 1:
                survived_legalhands = selectSmartly2(survived_legalhands,player1,pieces,count)
                print("6 : {0}".format(len(survived_legalhands))) 
           
            if len(survived_legalhands) != 1:
                survived_legalhands = stayClose(survived_legalhands,board)
                print("9 : {0}".format(len(survived_legalhands)))

        elif count <= 15 :
            if len(survived_legalhands) != 1:
                survived_legalhands = filter(survived_legalhands,player1)
                print("1 : {0}".format(len(survived_legalhands))) #重い

            if len(survived_legalhands) != 1:
                survived_legalhands = getEnterSpace(survived_legalhands,board)
                print("2 : {0}".format(len(survived_legalhands)))

            if len(survived_legalhands) != 1:
                survived_legalhands  = onlyMe(survived_legalhands,board)
                print("1 : {0}".format(len(survived_legalhands)))

            if len(survived_legalhands) != 1:
                survived_legalhands = selectBySizeOfPiece(survived_legalhands)
                print("2 : {0}".format(len(survived_legalhands)))
        
        elif 15 < count :

            if len(survived_legalhands) != 1:
                survived_legalhands = selectSmartly3(survived_legalhands,player1,pieces,count)
                print("2 : {0}".format(len(survived_legalhands)))

            if len(survived_legalhands) != 1:
                survived_legalhands  = onlyMe(survived_legalhands,board)
                print("1 : {0}".format(len(survived_legalhands)))

            if len(survived_legalhands) != 1:
                survived_legalhands = selectBySizeOfPiece(survived_legalhands)
                print("3 : {0}".format(len(survived_legalhands)))

        print()
        name, val =random.choice(list(survived_legalhands.items()))
        the_best_hand = name

        return encodeFourCode(survived_legalhands[the_best_hand][3],\
                              survived_legalhands[the_best_hand][4],\
                              survived_legalhands[the_best_hand][0],\
                              survived_legalhands[the_best_hand][1])
