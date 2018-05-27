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

    selected_legalhands = []

    for place in current_places:
        i = place[0]
        j = place[1]
        if 0 < i < 19 and 0 < j < 19 :
            if field[i-1][j] != 0 and field[i-1][j] != 10 and field[i-1][j] != 11 \
                and field[i][j-1] != 0 and field[i][j-1] != 10 and field[i][j-1] != 11\
                and field[i-1][j-1] == 1:
                selected_legalhands.append(place)
            elif field[i][j-1] != 0 and field[i][j-1] != 10 and field[i][j-1] != 11 \
                and field[i+1][j] != 0 and  field[i+1][j] != 10 and field[i+1][j] != 11 \
                and field[i+1][j-1] == 1:
                selected_legalhands.append(place)
            elif field[i+1][j] != 0 and  field[i+1][j] != 10 and field[i+1][j] != 11 \
                and field[i][j+1] != 0 and field[i][j+1] != 10 and field[i][j+1] != 11 \
                and field[i+1][j+1] == 1:
                selected_legalhands.append(place)
            elif field[i][j+1] != 0 and field[i][j+1] != 10 and field[i][j+1] != 11 \
                and field[i-1][j] != 0 and field[i-1][j] != 10 and field[i-1][j] != 11 \
                and field[i-1][j+1] == 1:
                selected_legalhands.append(place)

    if selected_legalhands != [] :
        return selected_legalhands
    else :
        return current_places

#広げたスペースのところに置いていく
def selectSmartlybf(current_legalhands,field,current_places):
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


    if selected_legalhands != {} and len(selected_places) >= 2:
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
def selectSmartly2(current_legalhands,old_player1,pieces):
    '''
    相手の角のところに置くように作っていく
    新しくできた11の領域があいてのスペースの隙間に入っているか確かめる
    さらにそのスペースにおけるピースを確認する
    '''

    selected_legalhands = {}

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
                if now_legalhands != {}:
                    final_judge += 1
                    
        if final_judge != 0:
            new = {key:value}
            selected_legalhands.update(new)

    if selected_legalhands != {} :
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

#相手のブロックの邪魔をする
def interference(field):
    p1 = [1,0]
    p2 = [1,0]
    p3 = [1,0]
    p4 = [1,0]

    selected_legalhands = {}
    (inter_field,player1,player2,player3,player4) = getField(board,p1,p2,p3,p4)
    for key,value in current_legalhands.items():
        current_pieces = [] #次に置くpieceを格納
        now_legalhands = {}
        field = value[5].copy()
        p1 = [1,0]
        p2 = [0,0]
        p3 = [0,0]
        p4 = [0,0]
        field = value[5].copy()
        (after_field,player1,player2,player3,player4) = getField(field,p1,p2,p3,p4) #new field作成
        judge = 0
        final_judge = 0
        if judge != 0:
            for piece in pieces:
                if piece != value[0]:
                    current_pieces.append(piece)

        now_legalhands = getAllLegalhands(after_field,[[i, j]], current_pieces)
        if now_legalhands != {}:
            final_judge += 1
    