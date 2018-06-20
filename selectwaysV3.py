import random

from players.B21.makefield import *
from players.B21.piecesinfo import getPiecesSize
from players.B21.makealllegalhands import *

'''
current_legalhands[key][0] = name               = ピースの名前
current_legalhands[key][1] = rot                = 回転度合い
current_legalhands[key][2]                      = 中心までの距離を示す値 #使わないと思う
current_legalhands[key][3] = centeri            = 中心のi座標
current_legalhands[key][4] = centerj            = 中心のj座標
current_legalhands[key][5] = after_field        = そのpieceを入れた後のfield
current_legalhands[key][6] = PPi(Puted Place i) = 置いた場所のi座標
current_legalhands[key][7] = PPj(puted Place j) = 置いた場所のj座標
'''

#角の数でフィルターをかける
def selectByNumberOfExcess(current_legalhands):
    '''
    角の数でフィルターをかける
    '''
    selected_legalhands = {}
    pieces_size = getPiecesSize()
    max_excess = 0
    for key,value in current_legalhands.items() :
        name = value[0]
        if max_excess < pieces_size[name][1] :
            max_excess = pieces_size[name][1]
    
    for key,value in current_legalhands.items() :
        name = value[0]
        if max_excess == pieces_size[name][1] :
            new = {key:value}
            selected_legalhands.update(new)

    return selected_legalhands

#置いた後の場所が一番対角線上で遠くなるようにする
def selectByPutedPlace(current_legalhands,field):

    '''
    ________________________________________________________________________
    ブロックを置いた後の一番遠い場所で絞る
    ______________________________________________________________________
    '''

    selected_legalhands = {}
    max = 0
    products = {}
    
    for key,value in current_legalhands.items():
        after_field = value[5].copy()
        for i in range(20) :
            for j in range(20) :
                if after_field[i][j] == 1 and field[i][j] != 1:
                    evaluation_i = 20 - i
                    evaluation_j = j + 1
                    product =  evaluation_i * evaluation_j #積を格納
                    if max <= product :
                        max = product
                        new = {key:product}
                        products.update(new)
    for key,product in products.items():
        if product == max :
            new = {key:current_legalhands[key]}
            selected_legalhands.update(new)

    return selected_legalhands

#置いた後の場所が一番対角線上で遠くなるようにする
def selectByPutPlace(current_legalhands):
    '''
    ________________________________________________________________________
    ブロックをどこの１１に置くかを決める
    ______________________________________________________________________
    '''

    selected_legalhands = {}
    max = 0
    products = {}
    #最大の積をmaxに格納
    for key,value in current_legalhands.items():
        PPi = value[6]
        PPj = value[7]
        evaluation_i = 20 - PPi
        evaluation_j = PPj + 1
        product = evaluation_i * evaluation_j #積を格納
        if max <= product :
            max = product
            #条件を満たしてそうな奴だけ通す
            new = {key:product}
            products.update(new)
    #maxと等しいものを格納
    for key,product in products.items():
        if product == max :
            new = {key:current_legalhands[key]}
            selected_legalhands.update(new)
    return selected_legalhands

#ピースのサイズで識別
def selectBySizeOfPiece(current_legalhands):

    pieces_size = getPiecesSize()
    selected_legalhands = {}
    
    for num in range(5,0,-1):
        for key,value in current_legalhands.items():
            name = value[0]
            if num == 5 :
                if pieces_size[name][0] == num:
                    new = {key:value}
                    selected_legalhands.update(new)
            elif num == 4 :
                if selected_legalhands == {} :
                    if pieces_size[name][0] == num:
                        new = {key:value}
                        selected_legalhands.update(new)
            elif num == 3 :
                if selected_legalhands == {} :
                    if pieces_size[name][0] == num:
                        new = {key:value}
                        selected_legalhands.update(new)
            elif num == 2 :
                if selected_legalhands == {} :
                    if pieces_size[name][0] == num:
                        new = {key:value}
                        selected_legalhands.update(new)
            elif num == 1 :
                if selected_legalhands == {} :
                    if pieces_size[name][0] == num:
                        new = {key:value}
                        selected_legalhands.update(new)

    return selected_legalhands

#広げたスペースのところにおける場所を確保
def selectPutPlaces(current_places,field):
    '''
    広げたスペースのところに置いていく
    '''

    selected_places = []

    for place in current_places:
        i = place[0]
        j = place[1]
        if 0 < i < 19 and 0 < j < 19 :
            if field[i-1][j] != 0 and field[i-1][j] != 10 and field[i-1][j] != 11 \
                and field[i][j-1] != 0 and field[i][j-1] != 10 and field[i][j-1] != 11\
                and field[i-1][j-1] == 1:
                selected_places.append(place)
            elif field[i][j-1] != 0 and field[i][j-1] != 10 and field[i][j-1] != 11 \
                and field[i+1][j] != 0 and  field[i+1][j] != 10 and field[i+1][j] != 11 \
                and field[i+1][j-1] == 1:
                selected_places.append(place)
            elif field[i+1][j] != 0 and  field[i+1][j] != 10 and field[i+1][j] != 11 \
                and field[i][j+1] != 0 and field[i][j+1] != 10 and field[i][j+1] != 11 \
                and field[i+1][j+1] == 1:
                selected_places.append(place)
            elif field[i][j+1] != 0 and field[i][j+1] != 10 and field[i][j+1] != 11 \
                and field[i-1][j] != 0 and field[i-1][j] != 10 and field[i-1][j] != 11 \
                and field[i-1][j+1] == 1:
                selected_places.append(place)

    if selected_places != [] :
        return selected_places
    else :
        return current_places

#広げたスペースのところに置いていく
def selectSmartlybf(current_legalhands,field,current_places,count):
    '''
    広げたスペースのところに置いていく
    '''
    selected_places = selectPutPlaces(current_places,field)
    selected_legalhands = {}
    judge_w = 0

    for key,value in current_legalhands.items():
        judge_p = 0
        i = value[3]
        j = value[4]
        if 0 < i < 19 and 0 < j < 19 :
            if field[i-1][j] != 0 and field[i-1][j] != 10 and field[i-1][j] != 11 \
                and field[i][j-1] != 0 and field[i][j-1] != 10 and field[i][j-1] != 11\
                and field[i-1][j-1] == 1:
                new = {key:value}
                selected_legalhands.update(new)
                judge_p = 1
            elif field[i][j-1] != 0 and field[i][j-1] != 10 and field[i][j-1] != 11 \
                and field[i+1][j] != 0 and  field[i+1][j] != 10 and field[i+1][j] != 11 \
                and field[i+1][j-1] == 1:
                new = {key:value}
                selected_legalhands.update(new)
                judge_p = 1
            elif field[i+1][j] != 0 and  field[i+1][j] != 10 and field[i+1][j] != 11 \
                and field[i][j+1] != 0 and field[i][j+1] != 10 and field[i][j+1] != 11 \
                and field[i+1][j+1] == 1:
                new = {key:value}
                selected_legalhands.update(new)
                judge_p = 1
            elif field[i][j+1] != 0 and field[i][j+1] != 10 and field[i][j+1] != 11 \
                and field[i-1][j] != 0 and field[i-1][j] != 10 and field[i-1][j] != 11 \
                and field[i-1][j+1] == 1:
                new = {key:value}
                selected_legalhands.update(new)
                judge_p = 1
        if judge_p == 1:
            judge_w += 1   


    if selected_legalhands != {} :
        return selected_legalhands
    else :
        return current_legalhands

#相手の角に入り込む
def selectSmartly(current_legalhands,old_player1):
    '''
    相手の角のところに置くように作っていく
    新しくできた11の領域があいてのスペースの隙間に入っているか確かめる
    '''

    selected_legalhands = {}

    p1 = [1,0]
    p2 = [0,0]
    p3 = [0,0]
    p4 = [0,0]
    for key,value in current_legalhands.items():
        field = value[5].copy()
        (after_field,player1,player2,player3,player4) = getField(field,p1,p2,p3,p4) #new field作成
        judge = 0
        for place in player1:
            if place not in old_player1:
                i = place[0]
                j = place[1]
                if 0 < i < 19 and 0 < j < 19 :
                    if after_field[i-1][j] != 0 and after_field[i-1][j] != 10 and after_field[i-1][j] != 11 \
                        and after_field[i][j-1] != 0 and after_field[i][j-1] != 10 and after_field[i][j-1] != 11\
                        and after_field[i-1][j-1] == 1:
                        judge += 1
                    elif after_field[i][j-1] != 0 and after_field[i][j-1] != 10 and after_field[i][j-1] != 11 \
                        and after_field[i+1][j] != 0 and  after_field[i+1][j] != 10 and after_field[i+1][j] != 11 \
                        and after_field[i+1][j-1] == 1:
                        judge += 1
                    elif after_field[i+1][j] != 0 and  after_field[i+1][j] != 10 and after_field[i+1][j] != 11 \
                        and after_field[i][j+1] != 0 and after_field[i][j+1] != 10 and after_field[i][j+1] != 11 \
                        and after_field[i+1][j+1] == 1:
                        judge += 1
                    elif after_field[i][j+1] != 0 and after_field[i][j+1] != 10 and after_field[i][j+1] != 11 \
                        and after_field[i-1][j] != 0 and after_field[i-1][j] != 10 and after_field[i-1][j] != 11 \
                        and after_field[i-1][j+1] == 1:
                        judge += 1

        if judge != 0:
            new = {key:value}
            selected_legalhands.update(new)
    if selected_legalhands != {} :
        return selected_legalhands
    else :
        return current_legalhands

#相手の角に入り込み、次のピースがおけるか確認
def selectSmartly2(current_legalhands,old_player1,pieces,count):
    '''
    相手の角のところに置くように作っていく
    新しくできた11の領域があいてのスペースの隙間に入っているか確かめる
    さらにそのスペースにおけるピースを確認する
    '''

    selected_legalhands5 = {}
    selected_legalhands4 = {}
    selected_legalhands3 = {}

    p1 = [1,0]
    p2 = [0,0]
    p3 = [0,0]
    p4 = [0,0]
    for key,value in current_legalhands.items():
        current_pieces = [] #次に置くpieceを格納
        now_legalhands = {}
        field = value[5].copy()
        (after_field,player1,player2,player3,player4) = getField(field,p1,p2,p3,p4) #new field作成
        judge = 0
        final_judge = 0
        for place in player1: #おける場所
            if place not in old_player1: #置けた場所
                i = place[0] #新しくおける場所
                j = place[1]
                if 0 < i < 19 and 0 < j < 19 :
                    if after_field[i-1][j] != 0 and after_field[i-1][j] != 10 and after_field[i-1][j] != 11 \
                        and after_field[i][j-1] != 0 and after_field[i][j-1] != 10 and after_field[i][j-1] != 11\
                        and after_field[i-1][j-1] == 1:
                        judge += 1
                    elif after_field[i][j-1] != 0 and after_field[i][j-1] != 10 and after_field[i][j-1] != 11 \
                        and after_field[i+1][j] != 0 and  after_field[i+1][j] != 10 and after_field[i+1][j] != 11 \
                        and after_field[i+1][j-1] == 1:
                        judge += 1
                    elif after_field[i+1][j] != 0 and  after_field[i+1][j] != 10 and after_field[i+1][j] != 11 \
                        and after_field[i][j+1] != 0 and after_field[i][j+1] != 10 and after_field[i][j+1] != 11 \
                        and after_field[i+1][j+1] == 1:
                        judge += 1
                    elif after_field[i][j+1] != 0 and after_field[i][j+1] != 10 and after_field[i][j+1] != 11 \
                        and after_field[i-1][j] != 0 and after_field[i-1][j] != 10 and after_field[i-1][j] != 11 \
                        and after_field[i-1][j+1] == 1:
                        judge += 1
                    
                if judge != 0:
                    for piece in pieces:
                        if piece != value[0]:
                            current_pieces.append(piece)

                now_legalhands = getAllLegalhands(after_field,[[i, j]], current_pieces)
                
                if now_legalhands != {} :
                    now_selected_legalhands = selectBySizeOfPiece(now_legalhands)
                    name, val =random.choice(list(now_selected_legalhands.items()))
                    pieces_size = getPiecesSize()
                    if pieces_size[val[0]][0] >= 5 :
                        final_judge = 5
                    elif pieces_size[val[0]][0] >= 4 :
                        final_judge = 4
                    elif pieces_size[val[0]][0] >= 3 and count >= 13:
                        final_judge = 3
                    
        if final_judge == 5:
            new = {key:value}
            selected_legalhands5.update(new)
        elif final_judge >= 4:
            new = {key:value}
            selected_legalhands4.update(new)
        elif final_judge >= 3:
            new = {key:value}
            selected_legalhands3.update(new)

    if selected_legalhands5 != {} :
        return selected_legalhands5
    elif selected_legalhands4 != {} :
        return selected_legalhands4
    elif selected_legalhands3 != {} :
        return selected_legalhands3
    else :
        return current_legalhands

#相手の角に入り込み、次のピースがおけるか確認
def selectSmartly3(current_legalhands,old_player1,pieces,count):
    '''
    相手の角のところに置くように作っていく
    新しくできた11の領域があいてのスペースの隙間に入っているか確かめる
    さらにそのスペースにおけるピースを確認する
    '''

    selected_legalhands = {}
    very_selected_legalhands = {}
    p1 = [1,1]
    p2 = [0,0]
    p3 = [0,0]
    p4 = [0,0]
    now_canput = []

    for key,value in current_legalhands.items():
        if value[0] not in now_canput:
            now_canput.append(value[0])

    for key,value in current_legalhands.items():
        now_pieces = []
        field = value[5].copy()
        for piece in pieces:
            if value[0] != piece:
                now_pieces.append(value[0])

        (after_field,player1,player2,player3,player4) = getField(field,p1,p2,p3,p4) #new field作成
        now_selected_legalhands = getAllLegalhands(after_field,player1,now_pieces)
        for key,value in now_selected_legalhands.items():
            if value[0] not in now_canput:
                new = {key:value}
                selected_legalhands.update(new)
                next_canput = []
                for key1,value1 in selected_legalhands.items():
                    if value1[0] not in next_canput:
                        next_canput.append(value1[0])

                for key1,value1 in current_legalhands.items():
                    field = value[5].copy()
                    next_pieces = []
                    for piece in next_pieces:
                        if value[0] != piece:
                            next_pieces.append(value1[0])

                    (after_field,player1,player2,player3,player4) = getField(field,p1,p2,p3,p4) #new field作成
                    now_selected_legalhands = getAllLegalhands(after_field,player1,now_pieces)
                    for key,value in now_selected_legalhands.items():
                        if value[0] not in next_canput:
                            new = {key:value}
                            very_selected_legalhands.update(new)
                    
    if very_selected_legalhands != {}:
        return selected_legalhands
    elif selected_legalhands != {} :
        return selected_legalhands
    else :
        return current_legalhands 

#置ける場所が増えないやつを削除
def filter(current_legalhands,old_player1):
    '''
    置いた後における場所が増えない手を削除
    '''


    selected_legalhands = {}

    p1 = [1,0]
    p2 = [0,0]
    p3 = [0,0]
    p4 = [0,0]
    for key,value in current_legalhands.items():
        field = value[5].copy()
        (after_field,player1,player2,player3,player4) = getField(field,p1,p2,p3,p4) #new field作成
        judge = 0
        for place in player1:
            if place not in old_player1:
                judge += 1
        if judge >= 1:
            new = {key:value}
            selected_legalhands.update(new)

    if selected_legalhands != {} :
        return selected_legalhands
    else :
        return current_legalhands

#新しくおける場所が多いやつを採用
def manyPutPlace(current_legalhands,old_player1):
    selected_legalhands1 = {}
    selected_legalhands2 = {}
    selected_legalhands3 = {}
    selected_legalhands4 = {}
    selected_legalhands5 = {}

    p1 = [1,0]
    p2 = [0,0]
    p3 = [0,0]
    p4 = [0,0]
    for key,value in current_legalhands.items():
        field = value[5].copy()
        (after_field,player1,player2,player3,player4) = getField(field,p1,p2,p3,p4) #new field作成
        judge = 0
        for place in player1:
            if place not in old_player1:
                judge += 1
        if judge == 5 :
            new = {key:value}
            selected_legalhands5.update(new)
        elif judge == 4:
            new = {key:value}
            selected_legalhands4.update(new)
        elif judge == 3:
            new = {key:value}
            selected_legalhands3.update(new)
        elif judge == 2:
            new = {key:value}
            selected_legalhands2.update(new)
        elif judge == 1:
            new = {key:value}
            selected_legalhands1.update(new)


    if selected_legalhands5 != {} :
        return selected_legalhands5
    elif  selected_legalhands4 != {} :
        return selected_legalhands4
    elif  selected_legalhands3 != {} :
        return selected_legalhands3
    elif  selected_legalhands2 != {} :
        return selected_legalhands2
    elif  selected_legalhands1 != {} :
        return selected_legalhands1
    else :
        return current_legalhands

#相手のブロックの邪魔をする
def interference(current_legalhands,board):
    p1 = [0,0]
    p2 = [1,0]
    p3 = [1,0]
    p4 = [1,0]
    field = board.copy()
    selected_legalhands1 = {}
    selected_legalhands2 = {}
    (inter_field,player1,player2,player3,player4) = getField(field,p1,p2,p3,p4)
    for key,value in current_legalhands.items():

        nowfield = value[5].copy()
        judge = 0

        for i in range(20):
            for j in range(20):
                if nowfield[i][j] == 1 and field[i][j] != 1 and inter_field[i][j] % 10 == 1  :
                    judge += 1

        if judge >= 2 :
            new = {key:value}
            selected_legalhands2.update(new)
        if judge >= 1:
            new = {key:value}
            selected_legalhands1.update(new)
    
    if selected_legalhands2 != {} :
        return selected_legalhands2
    elif  selected_legalhands1 != {} :
        return selected_legalhands1
    else :
        return current_legalhands

#相手の侵入を防ぐ(未完成)
def interferenceEnter(current_legalhands,board):
    p1 = [0,0]
    p2 = [1,0]
    p3 = [1,0]
    p4 = [1,0]
    field = board.copy()
    selected_legalhands = {}
    (inter_field,player1,player2,player3,player4) = getField(field,p1,p2,p3,p4)
    for key,value in current_legalhands.items():
        current_pieces = [] #次に置くpieceを格納
        now_legalhands = {}
        nowfield = value[5].copy()

        judge = 0
        for i in range(20):
            for j in range(20):
                if nowfield[i][j] == 1 and field[i][j] != 1 and inter_field[i][j] % 10 == 1  :
                    judge = 1
        if judge >= 1 :
            new = {key:value}
            selected_legalhands.update(new)
    
    if selected_legalhands != {} :
        return selected_legalhands
    else :
        return current_legalhands

#相手の駒に寄り添う
def stayClose(current_legalhands,board):
    selected_legalhands1 = {}
    selected_legalhands2 = {}
    selected_legalhands3 = {}
    selected_legalhands4 = {}
    selected_legalhands5 = {}

    for key,value in current_legalhands.items():
        field = board.copy()
        now_field = value[5].copy()
        max = 0
        judge = 0
        for i in range(20):
            for j in range(20):
                if field[i][j] != 1 and now_field[i][j] == 1:
                    for k in range(-1,2):
                        for l in range(-1,2):
                            if 0 <= i+k <= 19 and 0 <= j+l <= 19 :
                                if (k == -1 and l == 0) or (k == 0 and (l == -1 or l == 1)) or (k == 1 and l == 0):
                                    if now_field[i+k][j+l] == 2 \
                                    or now_field[i+k][j+l] == 3 \
                                    or now_field[i+k][j+l] == 4 :
                                        judge += 1
        if judge == 5 :
            new = {key:value}
            selected_legalhands5.update(new)
        elif judge == 4:
            new = {key:value}
            selected_legalhands4.update(new)
        elif judge == 3:
            new = {key:value}
            selected_legalhands3.update(new)
        elif judge == 2:
            new = {key:value}
            selected_legalhands2.update(new)
        elif judge == 1:
            new = {key:value}
            selected_legalhands1.update(new)
                
                
    if selected_legalhands5 != {} :
        return selected_legalhands5
    elif  selected_legalhands4 != {} :
        return selected_legalhands4
    elif  selected_legalhands3 != {} :
        return selected_legalhands3
    elif  selected_legalhands2 != {} :
        return selected_legalhands2
    elif  selected_legalhands1 != {} :
        return selected_legalhands1
    else :
        return current_legalhands

#侵入スペースの確保
def getEnterSpace(current_legalhands,board):
    selected_legalhands = {}
    field = board.copy()

    p1 = [1,1]
    p2 = [0,0]
    p3 = [0,0]
    p4 = [0,0]
    (field,player1,player2,player3,player4) = getField(field,p1,p2,p3,p4)

    for key,value in current_legalhands.items():
        now_field = value[5].copy()
        (now_field,player1,player2,player3,player4) = getField(now_field,p1,p2,p3,p4) #new field作成
        judge = 0
        for i in range(2,19):
            for j in range(1,18):
                if field[i][j] != 10 and now_field[i][j] == 10 :
                    if now_field[i-1][j-1] == 0 and (now_field[i-1][j] == 2 or now_field[i-1][j] == 3 or now_field[i-1][j] == 4) \
                                                and (now_field[i][j-1] == 2 or now_field[i][j-1] == 3 or now_field[i][j-1] == 4) :
                        judge = 1
                    if now_field[i-1][j+1] == 0 and (now_field[i-1][j] == 2 or now_field[i-1][j] == 3 or now_field[i-1][j] == 4) \
                                                and (now_field[i][j+1] == 2 or now_field[i][j+1] == 3 or now_field[i][j+1] == 4) :
                        judge = 1
                        
                    if now_field[i+1][j+1] == 0 and (now_field[i+1][j] == 2 or now_field[i+1][j] == 3 or now_field[i+1][j] == 4) \
                                                and (now_field[i][j+1] == 2 or now_field[i][j+1] == 3 or now_field[i][j+1] == 4) :
                        judge = 1
                        
                    if now_field[i+1][j-1] == 0 and (now_field[i+1][j] == 2 or now_field[i+1][j] == 3 or now_field[i+1][j] == 4) \
                                                and (now_field[i][j-1] == 2 or now_field[i][j-1] == 3 or now_field[i][j-1] == 4) :
                        judge = 1
                        
        if judge == 0:
            new = {key:value}
            selected_legalhands.update(new)

    if selected_legalhands != {} :
        return selected_legalhands
    else :
        return current_legalhands

#自分の開始地点を守る
def defence(current_legalhands,board):

    p1 = [0,0]
    p2 = [1,0]
    p3 = [1,0]
    p4 = [1,0]

    selected_legalhands = {}

    field = board.copy()
    (cpfield,player1,player2,player3,player4) = getField(field,p1,p2,p3,p4)
    judge = 0
    for i in range(13,20):
            for j in range(7):
                if cpfield[i][j] % 10 ==  1  :
                    judge = 1
    if judge == 0:
        return current_legalhands
    else :
        
        for key,value in current_legalhands.items():
            if 13 <= value[6]  and value[7] <= 6 :
                nowfield = value[5].copy()
                judge = 0
                for i in range(20):
                    for j in range(20):
                        if nowfield[i][j] == 1 and field[i][j] != 1 and cpfield[i][j] % 10 == 1  :
                            judge = 1
                if judge == 1:
                    new = {key:value}
                    selected_legalhands.update(new)
    
        if selected_legalhands != {} :
            return selected_legalhands
        else :
            return current_legalhands

def defence2(current_legalhands,old_player1,board):
    selected_legalhands = {}
    field = board.copy()
    p1 = [1,0]
    p2 = [1,0]
    p3 = [1,0]
    p4 = [1,0]

    (field,player1,player2,player3,player4) = getField(field,p1,p2,p3,p4)
    
    for piece in old_player1:
        i = piece[0]
        j = piece[1]
        judge = 0
        if 0 <= i-1 <= 19 and 0 <= j-1 <= 19:
            if field[i-1][j-1] == 1:
                for k in range(5):
                    for l in range(5):
                        if 0 <= i+k <= 19 and 0 <= j+l <= 19:
                            if field[i+k][j+l] == 11:
                                judge += 1 
        if 0 <= i-1 <= 19 and 0 <= j+1 <= 19:
            if field[i-1][j+1] == 1:
                for k in range(5):
                    for l in range(5):
                        if 0 <= i+k <= 19 and 0 <= j-l <= 19:
                            if field[i+k][j-l] == 11:
                                judge += 1 
        if 0 <= i+1 <= 19 and 0 <= j-1 <= 19:
            if field[i+1][j-1] == 1:
                for k in range(5):
                    for l in range(5):
                        if 0 <= i-k <= 19 and 0 <= j+l <= 19:
                            if field[i-k][j+l] == 11:
                                judge += 1  
        if 0 <= i+1 <= 19 and 0 <= j+1 <= 19:
            if field[i+1][j+1] == 1:
                for k in range(5):
                    for l in range(5):
                        if 0 <= i+k <= 19 and 0 <= j+l <= 19:
                            if field[i+k][j+l] == 11:
                                judge += 1 
        if judge <= 3:
            for key,value in current_legalhands.items():
                if value[6] == i and value[7] == j:
                    new = {key:value}
                    selected_legalhands.update(new)

    if selected_legalhands != {} :
        return selected_legalhands
    else :
        return current_legalhands


#絶対における場所の把握
def onlyMe(current_legalhands,board):
    
    field = board.copy()
    selected_legalhands = {}
    p1 = [0,0]
    p2 = [1,1]
    p3 = [0,0]
    p4 = [0,0]
    (p2_field,player1,player2,player3,player4) = getField(field,p1,p2,p3,p4)
    p1 = [0,0]
    p2 = [0,0]
    p3 = [1,1]
    p4 = [0,0]
    (p3_field,player1,player2,player3,player4) = getField(field,p1,p2,p3,p4)
    p1 = [0,0]
    p2 = [0,0]
    p3 = [0,0]
    p4 = [1,1]
    (p4_field,player1,player2,player3,player4) = getField(field,p1,p2,p3,p4)

    for key,value in current_legalhands.items():
        nowfield = value[5].copy()
        removed_pieces = []
        judge = 0
        pieces_size = getPiecesSize()
        
        for i in range(20):
            for j in range(20):
                if nowfield[i][j] == 1 and field[i][j] != 1 and p2_field[i][j] % 10 != 0 \
                                                            and p3_field[i][j] % 10 != 0 \
                                                            and p4_field[i][j] % 10 != 0:
                    judge = 1
        if judge == 0:
            if value[0] not in removed_pieces:
                if pieces_size[value[0]][0] >= 4:
                    removed_pieces.append(value[0])
        else:
            if value[0] not in removed_pieces:
                new = {key:value}
                selected_legalhands.update(new)

    if selected_legalhands != {} :
        return selected_legalhands
    else :
        return current_legalhands

#自分の場所
def mySpace1(current_legalhands,old_player1,board):
    selected_legalhands = {}
    field = board.copy()
    p1 = [0,0]
    p2 = [1,0]
    p3 = [1,0]
    p4 = [1,0]

    (field,player1,player2,player3,player4) = getField(field,p1,p2,p3,p4)
    
    for place in old_player1 :
        i = place[0]
        j = place[1]
        j1=0
        j2=0
        j3=0
        j4=0
        check = 0
        if i >= 1 and j >= 1:
            if field[i-1][j-1] == 1:
                for k in range(4):
                    for l in range(4):
                        if 0 <= i+k-1 <= 19 and 0 <= j+l-1 <= 19:
                            if check == 0 and field[i+k-1][j+l-1]==1:
                                check = 1
                            if field[i+k-1][j+l-1] / 10 >= 2  :
                                j1 += 1
        if i-1 >= 0 and j+1 <= 19:
            if field[i-1][j+1] == 1:
                for k in range(4):
                    for l in range(4):
                        if 0 <= i+k-1 <= 19 and 0 <= j-l+1 <= 19:
                            if field[i+k-1][j-l+1] / 10 >= 2 :
                                j2 += 1
        if i+1 <= 19 and j-1 >= 0:
            if field[i+1][j-1] == 1:
                for k in range(4):
                    for l in range(4):
                        if 0 <= i-k+1 <= 19 and 0 <= j+l-1 <= 19:
                            if field[i-k+1][j+l-1] / 10 >= 2 :
                                j3 += 1
        if i+1 <= 19 and j+1 <= 19:
            if field[i+1][j+1] == 1:
                for k in range(4):
                    for l in range(4):
                        if 0 <= i-k+1 <= 19 and 0 <= j-l+1 <= 19:
                            if field[i-k+1][j-l+1] / 10 >= 2 :
                                j4 += 1
                            
        if j1 != 0  or j2 != 0 or j3 != 0 or j4 != 0:
            for key,value in current_legalhands.items():
                if value[6] == i and value[7] == j:
                    new = {key:value}
                    selected_legalhands.update(new)

    if selected_legalhands != {} :
        return selected_legalhands
    else :
        return current_legalhands

#広い領域を見つけて、そこを見直す
def findSpace(current_legalhands,field,count):
    selected_legalhands = {}
    judge = [
                [0,0,0,0], \
                [0,0,0,0], \
                [0,0,0,0], \
                [0,0,0,0], \
            ]

    for i1 in range(4):
        for j1 in range(4):
            for i2 in range(5):
                for j2 in range(5):
                    if field[i1*5 + i2][j1*5 + j2] == 0:
                        judge[i1][j1] += 1

    for i1 in range(4):
        for j1 in range(4):
            if(count < 10):
                check = 20
            else:
                check = 15
            if(judge[i1][j1] > check):
                 for key,value in current_legalhands.items():
                     if(i1*4 <= value[6]<= (i1+1)*4 and j1*4 <= value[7] <= (j1+1)*4 ):
                        new = {key:value}
                        selected_legalhands.update(new)

    if selected_legalhands != {} :
        return selected_legalhands
    else :
        return current_legalhands

#置ける場所を中心にスペースがどれぐらいあるかを見る
def findSpace2(current_legalhands,old_player1,board):
    selected_legalhands = {}
    selected_places = []
    field = board.copy()
    p1 = [0,1]
    p2 = [0,0]
    p3 = [0,0]
    p4 = [0,0]

    (field,player1,player2,player3,player4) = getField(field,p1,p2,p3,p4)
    
    for place in old_player1 :
        i = place[0]
        j = place[1]
        j1=0
        j2=0
        j3=0
        j4=0
        if i >= 1 and j >= 1:
            if field[i-1][j-1] == 1:
                for k in range(4):
                    for l in range(4):
                        if 0 <= i+k <= 19 and 0 <= j+l <= 19:
                            if field[i+k-1][j+l-1]==0:
                                j1 += 1
        if i-1 >= 0 and j+1 <= 19:
            if field[i-1][j+1] == 1:
                for k in range(4):
                    for l in range(4):
                        if 0 <= i+k <= 19 and 0 <= j-l <= 19:
                            if field[i+k-1][j-l+1]==0:
                                j2 += 1
        if i+1 <= 19 and j-1 >= 0:
            if field[i+1][j-1] == 1:
                for k in range(4):
                    for l in range(4):
                        if 0 <= i-k <= 19 and 0 <= j+l <= 19:
                            if field[i-k+1][j+l-1]==0:
                                j3 += 1
        if i+1 <= 19 and j+1 <= 19:
            if field[i+1][j+1] == 1:
                for k in range(4):
                    for l in range(4):
                        if 0 <= i-k <= 19 and 0 <= j-l <= 19:
                            if field[i-k+1][j-l+1]==0:
                                j4 += 1
                            
        if j1 >= 8 or j2 >= 8 or j3 >= 8 or j4 >= 8:
            for key,value in current_legalhands.items():
                if value[6] == i and value[7] == j:
                    new = {key:value}
                    selected_legalhands.update(new)

    if selected_legalhands != {} :
        return selected_legalhands
    else :
        return current_legalhands

#置いた後の場所を中心にスペースがどれぐらいあるかを見る
def findSpace3(current_legalhands,old_player1,board):
    selected_legalhands = {}
    selected_places = []
    field = board.copy()
    p1 = [0,1]
    p2 = [0,0]
    p3 = [0,0]
    p4 = [0,0]
    for key,value in current_legalhands.items():
        nowfield = value[5]
        (nowfield,player1,player2,player3,player4) = getField(nowfield,p1,p2,p3,p4)
        for place in player1 :
            if place not in old_player1 :
                i = place[0]
                j = place[1]
                j1=0
                j2=0
                j3=0
                j4=0

                if i >= 1 and j >= 1:
                    if nowfield[i-1][j-1] == 1:
                        for k in range(4):
                            for l in range(4):
                                if 0 <= i+k <= 19 and 0 <= j+l <= 19:
                                    if nowfield[i+k][j+l]==0:
                                        j1 += 1

                if i-1 >= 0 and j+1 <= 19:
                    if nowfield[i-1][j+1] == 1:
                        for k in range(4):
                            for l in range(4):
                                if 0 <= i+k-1 <= 19 and 0 <= j-l+1 <= 19:
                                    if nowfield[i+k][j-l]==0:
                                        j2 += 1

                if i+1 <= 19 and j-1 >= 0:
                    if nowfield[i+1][j-1] == 1:
                        for k in range(4):
                            for l in range(4):
                                if 0 <= i-k <= 19 and 0 <= j+l <= 19:
                                    if nowfield[i-k][j+l]==0:
                                        j3 += 1

                if i+1 <= 19 and j+1 <= 19:
                    if nowfield[i+1][j+1] == 1:
                        for k in range(4):
                            for l in range(4):
                                if 0 <= i-k <= 19 and 0 <= j-l <= 19:
                                    if nowfield[i-k][j-l]==0:
                                        j4 += 1
                            
                if j1 >= 6 or j2 >= 6 or j3 >= 6 or j4 >= 6:
                    for key,value in current_legalhands.items():
                        if value[6] == i and value[7] == j:
                            new = {key:value}
                            selected_legalhands.update(new)

    if selected_legalhands != {} :
        return selected_legalhands
    else :
        return current_legalhands

#特定のピースを置く
def findpiece(current_legalhands,piece):
    selected_legalhands = {}
    for key,value in current_legalhands.items():
        if value[0] == piece:
            new = {key:value}
            selected_legalhands.update(new)
    
    if selected_legalhands != {} :
        return selected_legalhands
    else :
        return current_legalhands