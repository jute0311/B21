from blokus.piece import Pieces

def getField(board,p1,p2,p3,p4):

    field = board.copy()	#fieldにおける場所、置けない場所を入力していく
    plc = [[0,0,0],[0,0,0],[0,0,0]] #置く場所を中心とした9*9のリストを作成

    #おける場所の座標を保持
    player1=[]
    player2=[]
    player3=[]
    player4=[]

    '''
	______________________________________________________________________________________
	fieldに情報を代入(おける場所、置けない場所)
	・使用変数
	field,board,player1,2,3,4,plc
	_______________________________________________________________________________________
	'''
    for i in range(20):
        for j in range(20):
            for k in range(-1,2):
                for l in range(-1,2):
                    if -1 < i+k < 20 and -1 < j+l < 20:
                        plc[k+1][l+1] = board[i+k][j+l].copy()
                    else:
                        plc[k+1][l+1] = 0
            
            if p2[0]:
                (field,player2) = getCanPut(plc,field,player2,i,j,2)
            if p2[1]:
                field = getCanNotPut(plc,field,i,j,2)

            if p3[0]:
                (field,player3) = getCanPut(plc,field,player3,i,j,3)
            if p3[1]:
                field = getCanNotPut(plc,field,i,j,3)

            if p4[0]:
                (field,player4) = getCanPut(plc,field,player4,i,j,4)
            if p4[1]:
                field = getCanNotPut(plc,field,i,j,4)
            
            #必ず自分の情報をうわがきするようにここに置く
            if p1[0]:
                (field,player1) = getCanPut(plc,field,player1,i,j,1)
            if p1[1]:
                field = getCanNotPut(plc,field,i,j,1)
				

    return field,player1,player2,player3,player4

def getCanPut(plc,field,player,i,j,x):
    '''
	________________________________________________________________________________
    おける場所の把握
	3つの条件を満たすときに成り立つ。
	1. plcの真ん中が0である。
	2. [[x,0,x], 
	    [0,0,0],　の4座標のどこかにxが存在すればよい
	    [x,0,x]]
	3. [[0,x,0],
		[x,0,x], の4座標
		[0,x,0]]
	_________________________________________________________________________________
	'''

    if plc[1][1] == 0 :
        if plc[0][0] == x or plc[0][2] == x or plc[2][0] == x or plc[2][2] == x :
            if plc[0][1] != x and plc[1][0] != x and plc[1][2] != x and plc[2][1] != x :
                field[i][j] = x*10 +1
                player.append([i,j])

    return field,player

def getCanNotPut(plc,field,i,j,x):
    '''
    _______________________________________________________________________________________________
    絶対に置けない場所の把握
    1.真ん中が0
    2.[[0,x,0], 
       [x,0,x],　のいずれかの場所にX（playerの値)があった場合plc[1][1]すなわちfield[i][j]には絶対に置けない
       [0,x,0]]
    
    x=1のとき10、
    x=2のとき20、
    x=3のとき30、
    x=4のとき40
    をfield[i][j]に代入
    ________________________________________________________________________________________________
    '''
    if plc[1][1] == 0  :
        if plc[0][1] == x or plc[1][0] == x or plc[1][2] == x or plc[2][1] == x :
            field[i][j] = x*10
    
    return field
