from players.B21.piecesinfo import getAllPieces
from players.B21.piecesinfo import getAllPiecesShape
from players.B21.piecesinfo import getPiecesSize
from players.B21.piecesinfo import getUsedPieces

'''
all_exist_piecesの中からルールに適したものを選ぶ
all_legalwaysは実際に置く場所を第3，4に格納している

all_legalhands[key][0] = name               = ピースの名前
all_legalhands[key][1] = rot                = 回転度合い
all_legalhands[key][2]                      = 中心までの距離を示す値 #使わないと思う
all_legalhands[key][3] = centeri            = 中心のi座標
all_legalhands[key][4] = centerj            = 中心のj座標
all_legalhands[key][5] = after_field        = そのpieceを入れた後のfield
all_legalhands[key][6] = PPi(Puted Place i) = 置いた場所のi座標
all_legalhands[key][7] = PPj(puted Place j) = 置いた場所のj座標
となるように作成
'''

def getAllLegalhands(field,player,pieces,count):
    all_legalhands = {}

    exist_hands = getExistHands(pieces)
    put_places = player
    #すべてのおける場所で行うためのfor
    for place in put_places :
        #すべての存在する形で行うためのfor
        for key,value in exist_hands.items():
            
            legal_value = value.copy()
            
            check_field = field.copy()
            
            all_pieces_shape = getAllPiecesShape()
            pieces_size = getPiecesSize()

            legal_value[3]+=place[0] #中心座標= [legal_value[3],legal_value[4]]
            legal_value[4]+=place[1]
            
            '''
            check_fieldにpieceをいれる
            ただし、field上にない場所(x<0,19<x,y<0,19<y)の場合は何もいれない（いれれない）
            '''
            name = legal_value[0] #アルファベット（pieceの名前）が入っている
            rot = legal_value[1] #回転度が格納されている
            centeri = legal_value[3] #中心のi座標
            centerj = legal_value[4] #中心のj座標

            for i in range(pieces_size[name][0]):
                if  -1 < centeri+all_pieces_shape[name][rot][i][0] < 20 \
                    and -1 < centerj+all_pieces_shape[name][rot][i][1] < 20 :

                    check_field[centeri+all_pieces_shape[name][rot][i][0]]\
                               [centerj+all_pieces_shape[name][rot][i][1]] = 1
                    
            count_one = getCountOne(check_field)
            count_correct_one = getCountCorrectOne(pieces,legal_value[0])

            judge = 0 #条件を満たさない場合必ず1になる

            '''
            check_fieldとfieldを比較
            2つの条件をいずれも満たす場合に合法手と認める
             1.もしcheck_fieldの1の部分がfield上で0と11と1だけならばそれは合法手　かつ
             2.の数がcheck_fieldとused_pieces + new_pieceと同じなら合法手
            '''

            if count_one != count_correct_one :
                judge = 1
            else :    
                for i in range(20):
                    for j in range(20):
                        if check_field[i][j] == 1 \
                            and field[i][j] != 0  and field[i][j] != 1 \
                            and field[i][j] != 11 and field[i][j] != 21 \
                            and field[i][j] != 31 and field[i][j] != 41 :
                            judge = 1
                    
            
            if judge == 0 :
                legal_value.append(check_field) #legal_value[5](all_legalhands[key][5])に格納
                #選んだ11の場所をリストに格納
                legal_value.append(place[0]) #legal_value[6](all_legalhands[key][6])に格納
                legal_value.append(place[1]) #legal_value[7](all_legalhands[key][7])に格納

                '''
                keyをkeyとそのピースを置く座標のタプルに変えることで、すべての合法手を格納できるようにしている
                key = (?_?_?,中心の縦軸座標,中心の横軸座標)となってる
                '''
                key = (key,place[0],place[1])

                new = {key:legal_value}
                all_legalhands.update(new)

    return all_legalhands

def getCountOne(check_field):
    count_one = 0
    for i in range(20) :
        for j in range(20):
            if check_field[i][j] == 1 :
                count_one += 1
            
    return count_one

def getCountCorrectOne(pieces,next_piece):
    count_used_pieces_one = 0
    count_correct_one = 0

    used_pieces = getUsedPieces(pieces)
    
    pieces_size = getPiecesSize()

    for used_piece in used_pieces :
        count_used_pieces_one += pieces_size[used_piece][0]

    count_correct_one = count_used_pieces_one + pieces_size[next_piece][0]
    

    '''
    デバッグ用
    print("count_used_pieces_one : {0}".format(count_used_pieces_one))
    print("next_piece : {0}".format(next_piece))
    print("pieces_size[next_piece] : {0}".format(pieces_size[next_piece]))
    print("count_correct_one : {0}".format(count_correct_one))
    '''

    return count_correct_one

def getExistHands(pieces):
    all_pieces = getAllPieces()
    exist_hands = {}
    for piece in pieces:
        for key,value in all_pieces.items():
            if(piece == value[0]):
                new = {key:value}
                exist_hands.update(new)
    
    return exist_hands
    