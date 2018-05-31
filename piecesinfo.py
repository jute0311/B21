
def getAllPieces():
    '''
    ____________________________________________

    [  -,  -,  0,  -,  -]
    [  -,  1,  2,  3,  -]
    [  4,  5,  6,  7,  8, 0,-2]
    [  -,  9, 10, 11,  -]
    [  -,  -, 12,  -,  -]

    ____________________________________________
    '''

    '''
    all_pieces = {'piece名_回転具合_中心までの距離':['piece名',回転具合,中心までの距離を示す数字,中心までの行の距離x,中心までの列の距離y]}

    '?_a_b'を行列[x,y]に置きたいとき
    中心の座標は[x+all_pieces['?_a_b'][2],y+all_pieces['?_a_b'][3]]
    よってhand = encodeFourCode(x+all_pieces['?_a_b'][3], y+all_pieces['?_a_b'][4],all_pieces['?_a_b'][0], all_pieces['?_a_b'][1])
    を実行すればよい
    '''

    all_pieces = \
   {'a_0_6' : ['a',0, 6, 0, 0],\
   'b_0_6'  : ['b',0, 6, 0, 0], 'b_0_10' : ['b',0,10,-1, 0], \
   'b_2_6'  : ['b',2, 6, 0, 0], 'b_2_7'  : ['b',2, 7, 0,-1], \
   'c_0_2'  : ['c',0, 2, 1, 0], 'c_0_10' : ['c',0,10,-1, 0], \
   'c_2_5'  : ['c',2, 5, 0, 1], 'c_2_7'  : ['c',2, 7, 0,-1], \
   'd_0_2'  : ['d',0, 2, 1, 0], 'd_0_6'  : ['d',0, 6, 0, 0], 'd_0_7'  : ['d',0, 7, 0,-1], \
   'd_2_2'  : ['d',2, 2, 1, 0], 'd_2_5'  : ['d',2, 5, 0, 1], 'd_2_6'  : ['d',2, 6, 0, 0], \
   'd_4_5'  : ['d',4, 5, 0, 1], 'd_4_6'  : ['d',4, 6, 0, 0], 'd_4_10' : ['d',4,10,-1, 0], \
   'd_6_6'  : ['d',6, 6, 0, 0], 'd_6_7'  : ['d',6, 7, 0,-1], 'd_6_10' : ['d',6,10,-1, 0], \
   'e_0_2'  : ['e',0, 2, 1, 0], 'e_0_12' : ['e',0,12,-2, 0], \
   'e_2_5'  : ['e',2, 5, 0, 1], 'e_2_8'  : ['e',2, 8, 0,-2], \
   'f_0_2'  : ['f',0, 2, 1, 0], 'f_0_9'  : ['f',0, 9,-1, 1], 'f_0_10' : ['f',0,10,-1, 0], \
   'f_1_2'  : ['f',1, 2, 1, 0], 'f_1_10' : ['f',1,10,-1, 0], 'f_1_11' : ['f',1,11,-1,-1], \
   'f_2_5'  : ['f',2, 5, 0, 1], 'f_2_7'  : ['f',2, 7, 0,-1], 'f_2_11' : ['f',2,11,-1,-1], \
   'f_3_3'  : ['f',3, 3, 1,-1], 'f_3_5'  : ['f',3, 5, 0, 1], 'f_3_7'  : ['f',3, 7, 0,-1], \
   'f_4_2'  : ['f',4, 2, 1, 0], 'f_4_3'  : ['f',4, 3, 1,-1], 'f_4_10' : ['f',4,10,-1, 0], \
   'f_5_1'  : ['f',5, 1, 1, 1], 'f_5_2'  : ['f',5, 2, 1, 0], 'f_5_10' : ['f',5,10,-1, 0], \
   'f_6_1'  : ['f',6, 1, 1, 1], 'f_6_5'  : ['f',6, 5, 0, 1], 'f_6_7'  : ['f',6, 7, 0,-1], \
   'f_7_5'  : ['f',7, 5, 0, 1], 'f_7_7'  : ['f',7, 7, 0,-1], 'f_7_9'  : ['f',7, 9,-1, 1], \
   'g_0_2'  : ['g',0, 2, 1, 0], 'g_0_7'  : ['g',0, 7, 0,-1], 'g_0_10' : ['g',0,10,-1, 0], \
   'g_2_2'  : ['g',2, 2, 1, 0], 'g_2_5'  : ['g',2, 5, 0, 1], 'g_2_7'  : ['g',2, 7, 0,-1], \
   'g_4_2'  : ['g',4, 2, 1, 0], 'g_4_5'  : ['g',4, 5, 0, 1], 'g_4_10' : ['g',4,10,-1, 0], \
   'g_6_5'  : ['g',6, 5, 0, 1], 'g_6_7'  : ['g',6, 7, 0,-1], 'g_6_10' : ['g',6,10,-1, 0], \
   'h_0_6'  : ['h',0, 6, 0, 0], 'h_0_7'  : ['h',0, 7, 0,-1], 'h_0_10' : ['h',0,10,-1, 0], 'h_0_11' : ['h',0,11,-1,-1],\
   'i_0_5'  : ['i',0, 5, 0, 1], 'i_0_6'  : ['i',0, 6, 0, 0], 'i_0_10' : ['i',0,10,-1, 0], 'i_0_11' : ['i',0,11,-1,-1],\
   'i_1_6'  : ['i',1, 6, 0, 0], 'i_1_7'  : ['i',1, 7, 0,-1], 'i_1_9'  : ['i',1, 9,-1, 1], 'i_1_10' : ['i',1,10,-1, 0],\
   'i_2_3'  : ['i',2, 3, 1,-1], 'i_2_6'  : ['i',2, 6, 0, 0], 'i_2_7'  : ['i',2, 7, 0,-1], 'i_2_10' : ['i',2,10,-1, 0],\
   'i_3_2'  : ['i',3, 2, 1, 0], 'i_3_6'  : ['i',3, 6, 0, 0], 'i_3_7'  : ['i',3, 7, 0,-1], 'i_3_11' : ['i',3,11,-1,-1],\
   'j_0_0'  : ['j',0, 0, 2, 0], 'j_0_12' : ['j',0,12,-2, 0], \
   'j_2_4'  : ['j',2, 4, 0, 2], 'j_2_8'  : ['j',2, 8, 0,-2], \
   'k_0_0'  : ['k',0, 0, 2, 0], 'k_0_9'  : ['k',0, 9,-1, 1], 'k_0_10' : ['k',0,10,-1, 0], \
   'k_1_0'  : ['k',1, 0, 2, 0], 'k_1_10' : ['k',1,10,-1, 0], 'k_1_11' : ['k',1,11,-1,-1], \
   'k_2_4'  : ['k',2, 4, 0, 2], 'k_2_7'  : ['k',2, 7, 0,-1], 'k_2_11' : ['k',2,11,-1,-1], \
   'k_3_3'  : ['k',3, 3, 1,-1], 'k_3_4'  : ['k',3, 4, 0, 2], 'k_3_7'  : ['k',3, 7, 0,-1], \
   'k_4_2'  : ['k',4, 2, 1, 0], 'k_4_3'  : ['k',4, 3, 1,-1], 'k_4_12' : ['k',4,12,-2, 0], \
   'k_5_1'  : ['k',5, 1, 1, 1], 'k_5_2'  : ['k',5, 2, 1, 0], 'k_5_12' : ['k',5,12,-2, 0], \
   'k_6_1'  : ['k',6, 1, 1, 1], 'k_6_5'  : ['k',6, 5, 0, 1], 'k_6_8'  : ['k',6, 8, 0,-2], \
   'k_7_5'  : ['k',7, 5, 0, 1], 'k_7_8'  : ['k',7, 8, 0,-2], 'k_7_9'  : ['k',7, 9,-1, 1], \
   'l_0_0'  : ['l',0, 0, 2, 0], 'l_0_5'  : ['l',0, 5, 0, 1], 'l_0_6'  : ['l',0, 6, 0, 0], 'l_0_9'  : ['l',0, 9,-1, 1],\
   'l_1_0'  : ['l',1, 0, 2, 0], 'l_1_6'  : ['l',1, 6, 0, 0], 'l_1_7'  : ['l',1, 7, 0,-1], 'l_1_11' : ['l',1,11,-1,-1],\
   'l_2_4'  : ['l',2, 4, 0, 2], 'l_2_6'  : ['l',2, 6, 0, 0], 'l_2_10' : ['l',2,10,-1, 0], 'l_2_11' : ['l',2,11,-1,-1],\
   'l_3_2'  : ['l',3, 2, 1, 0], 'l_3_3'  : ['l',3, 3, 1,-1], 'l_3_4'  : ['l',3, 4, 0, 2], 'l_3_6'  : ['l',3, 6, 0, 0],\
   'l_4_3'  : ['l',4, 3, 1,-1], 'l_4_6'  : ['l',4, 6, 0, 0], 'l_4_7'  : ['l',4, 7, 0,-1], 'l_4_12' : ['l',4,12,-2, 0],\
   'l_5_1'  : ['l',5, 1, 1, 1], 'l_5_5'  : ['l',5, 5, 0, 1], 'l_5_6'  : ['l',5, 6, 0, 0], 'l_5_12' : ['l',5,12,-2, 0],\
   'l_6_1'  : ['l',6, 1, 1, 1], 'l_6_2'  : ['l',6, 2, 1, 0], 'l_6_6'  : ['l',6, 6, 0, 0], 'l_6_8'  : ['l',6, 8, 0,-2],\
   'l_7_6'  : ['l',7, 6, 0, 0], 'l_7_8'  : ['l',7, 8, 0,-2], 'l_7_9'  : ['l',7, 9,-1, 1], 'l_7_10' : ['l',7,10,-1, 0],\
   'm_0_2'  : ['m',0, 2, 1, 0], 'm_0_5'  : ['m',0, 5, 0, 1], 'm_0_9'  : ['m',0, 9,-1, 1], 'm_0_10' : ['m',0,10,-1, 0],\
   'm_1_2'  : ['m',1, 2, 1, 0], 'm_1_7'  : ['m',1, 7, 0,-1], 'm_1_10' : ['m',1,10,-1, 0], 'm_1_11' : ['m',1,11,-1,-1],\
   'm_2_5'  : ['m',2, 5, 0, 1], 'm_2_7'  : ['m',2, 7, 0,-1], 'm_2_10' : ['m',2,10,-1, 0], 'm_2_11' : ['m',2,11,-1,-1],\
   'm_3_2'  : ['m',3, 2, 1, 0], 'm_3_3'  : ['m',3, 3, 1,-1], 'm_3_5'  : ['m',3, 5, 0, 1], 'm_3_7'  : ['m',3, 7, 0,-1],\
   'm_4_2'  : ['m',4, 2, 1, 0], 'm_4_3'  : ['m',4, 3, 1,-1], 'm_4_7'  : ['m',4, 7, 0,-1], 'm_4_10' : ['m',4,10,-1, 0],\
   'm_5_1'  : ['m',5, 1, 1, 1], 'm_5_2'  : ['m',5, 2, 1, 0], 'm_5_5'  : ['m',5, 5, 0, 1], 'm_5_10' : ['m',5,10,-1, 0],\
   'm_6_1'  : ['m',6, 1, 1, 1], 'm_6_2'  : ['m',6, 2, 1, 0], 'm_6_5'  : ['m',6, 5, 0, 1], 'm_6_7'  : ['m',6, 7, 0,-1],\
   'm_7_5'  : ['m',7, 5, 0, 1], 'm_7_7'  : ['m',7, 7, 0,-1], 'm_7_9'  : ['m',7, 9,-1, 1], 'm_7_10' : ['m',7,10,-1, 0],\
   'n_0_1'  : ['n',0, 1, 1, 1], 'n_0_2'  : ['n',0, 2, 1, 0], 'n_0_9'  : ['n',0, 9,-1, 1], 'n_0_10' : ['n',0,10,-1, 0],\
   'n_2_5'  : ['n',2, 5, 0, 1], 'n_2_7'  : ['n',2, 7, 0,-1], 'n_2_9'  : ['n',2, 9,-1, 1], 'n_2_11' : ['n',2,11,-1,-1],\
   'n_4_2'  : ['n',4, 2, 1, 0], 'n_4_3'  : ['n',4, 3, 1,-1], 'n_4_10' : ['n',4,10,-1, 0], 'n_4_11' : ['n',4,11,-1,-1],\
   'n_6_1'  : ['n',6, 1, 1, 1], 'n_6_3'  : ['n',6, 3, 1,-1], 'n_6_5'  : ['n',6, 5, 0, 1], 'n_6_7'  : ['n',6, 7, 0,-1],\
   'o_0_2'  : ['o',0, 2, 1, 0], 'o_0_7'  : ['o',0, 7, 0,-1], 'o_0_12' : ['o',0,12,-2, 0], \
   'o_1_2'  : ['o',1, 2, 1, 0], 'o_1_5'  : ['o',1, 5, 0, 1], 'o_1_12' : ['o',1,12,-2, 0], \
   'o_2_2'  : ['o',2, 2, 1, 0], 'o_2_5'  : ['o',2, 5, 0, 1], 'o_2_8'  : ['o',2, 8, 0,-2], \
   'o_3_5'  : ['o',3, 5, 0, 1], 'o_3_8'  : ['o',3, 8, 0,-2], 'o_3_10' : ['o',3,10,-1, 0], \
   'o_4_0'  : ['o',4, 0, 2, 0], 'o_4_5'  : ['o',4, 5, 0, 1], 'o_4_10' : ['o',4,10,-1, 0], \
   'o_5_0'  : ['o',5, 0, 2, 0], 'o_5_7'  : ['o',5, 7, 0,-1], 'o_5_10' : ['o',5,10,-1, 0], \
   'o_6_4'  : ['o',6, 4, 0, 2], 'o_6_7'  : ['o',6, 7, 0,-1], 'o_6_10' : ['o',6,10,-1, 0], \
   'o_7_2'  : ['o',7, 2, 1, 0], 'o_7_4'  : ['o',7, 4, 0, 2], 'o_7_7'  : ['o',7, 7, 0,-1], \
   'p_0_2'  : ['p',0, 2, 1, 0], 'p_0_9'  : ['p',0, 9,-1, 1], 'p_0_11' : ['p',0,11,-1,-1], \
   'p_2_3'  : ['p',2, 3, 1,-1], 'p_2_5'  : ['p',2, 5, 0, 1], 'p_2_11' : ['p',2,11,-1,-1], \
   'p_4_1'  : ['p',4, 1, 1, 1], 'p_4_3'  : ['p',4, 3, 1,-1], 'p_4_10' : ['p',4,10,-1, 0], \
   'p_6_1'  : ['p',6, 1, 1, 1], 'p_6_7'  : ['p',6, 7, 0,-1], 'p_6_9'  : ['p',6, 9,-1, 1], \
   'q_0_0'  : ['q',0, 0, 2, 0], 'q_0_6'  : ['q',0, 6, 0, 0], 'q_0_8'  : ['q',0, 8, 0,-2], \
   'q_2_0'  : ['q',2, 0, 2, 0], 'q_2_4'  : ['q',2, 4, 0, 2], 'q_2_6'  : ['q',2, 6, 0, 0], \
   'q_4_4'  : ['q',4, 4, 0, 2], 'q_4_6'  : ['q',4, 6, 0, 0], 'q_4_12' : ['q',4,12,-2, 0], \
   'q_6_6'  : ['q',6, 6, 0, 0], 'q_6_8'  : ['q',6, 8, 0,-2], 'q_6_12' : ['q',6,12,-2, 0], \
   'r_0_1'  : ['r',0, 1, 1, 1], 'r_0_2'  : ['r',0, 2, 1, 0], 'r_0_6'  : ['r',0, 6, 0, 0], 'r_0_7'  : ['r',0, 7, 0,-1], 'r_0_11' : ['r',0,11,-1,-1],\
   'r_2_2'  : ['r',2, 2, 1, 0], 'r_2_3'  : ['r',2, 3, 1,-1], 'r_2_5'  : ['r',2, 5, 0, 1], 'r_2_6'  : ['r',2, 6, 0, 0], 'r_2_9'  : ['r',2, 9,-1, 1],\
   'r_4_1'  : ['r',4, 1, 1, 1], 'r_4_5'  : ['r',4, 5, 0, 1], 'r_4_6'  : ['r',4, 6, 0, 0], 'r_4_10' : ['r',4,10,-1, 0], 'r_4_11' : ['r',4,11,-1,-1],\
   'r_6_3'  : ['r',6, 3, 1,-1], 'r_6_6'  : ['r',6, 6, 0, 0], 'r_6_7'  : ['r',6, 7, 0,-1], 'r_6_9'  : ['r',6, 9,-1, 1], 'r_6_10' : ['r',6,10,-1, 0],\
   's_0_1'  : ['s',0, 1, 1, 1], 's_0_5'  : ['s',0, 5, 0, 1], 's_0_7'  : ['s',0, 7, 0,-1], 's_0_11' : ['s',0,11,-1,-1],\
   's_1_3'  : ['s',1, 3, 1,-1], 's_1_5'  : ['s',1, 5, 0, 1], 's_1_7'  : ['s',1, 7, 0,-1], 's_1_9'  : ['s',1, 9,-1, 1],\
   's_2_2'  : ['s',2, 2, 1, 0], 's_2_3'  : ['s',2, 3, 1,-1], 's_2_9'  : ['s',2, 9,-1, 1], 's_2_10' : ['s',2,10,-1, 0],\
   's_3_1'  : ['s',3, 1, 1, 1], 's_3_2'  : ['s',3, 2, 1, 0], 's_3_10' : ['s',3,10,-1, 0], 's_3_11' : ['s',3,11,-1,-1],\
   't_0_1'  : ['t',0, 1, 1, 1], 't_0_5'  : ['t',0, 5, 0, 1], 't_0_7'  : ['t',0, 7, 0,-1], 't_0_10' : ['t',0,10,-1, 0],\
   't_1_3'  : ['t',1, 3, 1,-1], 't_1_5'  : ['t',1, 5, 0, 1], 't_1_7'  : ['t',1, 7, 0,-1], 't_1_10' : ['t',1,10,-1, 0],\
   't_2_2'  : ['t',2, 2, 1, 0], 't_2_7'  : ['t',2, 7, 0,-1], 't_2_9'  : ['t',2, 9,-1, 1], 't_2_10' : ['t',2,10,-1, 0],\
   't_3_1'  : ['t',3, 1, 1, 1], 't_3_2'  : ['t',3, 2, 1, 0], 't_3_7'  : ['t',3, 7, 0,-1], 't_3_10' : ['t',3,10,-1, 0],\
   't_4_2'  : ['t',4, 2, 1, 0], 't_4_5'  : ['t',4, 5, 0, 1], 't_4_7'  : ['t',4, 7, 0,-1], 't_4_11' : ['t',4,11,-1,-1],\
   't_5_2'  : ['t',5, 2, 1, 0], 't_5_5'  : ['t',5, 5, 0, 1], 't_5_7'  : ['t',5, 7, 0,-1], 't_5_9'  : ['t',5, 9,-1, 1],\
   't_6_2'  : ['t',6, 2, 1, 0], 't_6_3'  : ['t',6, 3, 1,-1], 't_6_5'  : ['t',6, 5, 0, 1], 't_6_10' : ['t',6,10,-1, 0],\
   't_7_2'  : ['t',7, 2, 1, 0], 't_7_5'  : ['t',7, 5, 0, 1], 't_7_10' : ['t',7,10,-1, 0], 't_7_11' : ['t',7,11,-1,-1],\
   'u_0_2'  : ['u',0, 2, 1, 0], 'u_0_5'  : ['u',0, 5, 0, 1], 'u_0_7'  : ['u',0, 7, 0,-1], 'u_0_10' : ['u',0,10,-1, 0],\
   }


    
    return all_pieces

def getAllPiecesShape():
    '''
    all_pieces_shape['j'][-2, 0] = [[-2,0(12)],
                            [-1,0(10)],
                            [ 0,0( 6)],
                            [ 1,0( 2)],
                            [ 2,0( 0)]]

    all_pieces_shape['piece'][回転度合い]
    '''
    all_pieces_shape = { \
    'a' : [\
            [[ 0, 0]]\
          ],\
    'b' : [\
            [[ 0, 0],[ 1, 0]],\
            [[]],\
            [[ 0, 0],[ 0, 1]]\
          ],\
    'c' : [\
            [[-1, 0],[ 0, 0],[ 1, 0]],\
            [[]],\
            [[ 0,-1],[ 0, 0],[ 0, 1]]\
          ],\
    'd' : [\
            [[-1, 0],[ 0, 0],[ 0, 1]],\
            [[]],\
            [[-1, 0],[ 0,-1],[ 0, 0]],\
            [[]],\
            [[ 0,-1],[ 0, 0],[ 1, 0]],\
            [[]],\
            [[ 0, 0],[ 0, 1],[ 1, 0]]\
          ],\
    'e' : [\
            [[-1, 0],[ 0, 0],[ 1, 0],[ 2, 0]],\
            [[]],\
            [[ 0,-1],[ 0, 0],[ 0, 1],[ 0, 2]]\
          ],\
    'f' : [\
            [[-1, 0],[ 0, 0],[ 1,-1],[ 1, 0]],\
            [[-1, 0],[ 0, 0],[ 1, 0],[ 1, 1]],\
            [[ 0,-1],[ 0, 0],[ 0, 1],[ 1, 1]],\
            [[-1, 1],[ 0,-1],[ 0, 0],[ 0, 1]],\
            [[-1, 0],[-1, 1],[ 0, 0],[ 1, 0]],\
            [[-1,-1],[-1, 0],[ 0, 0],[ 1, 0]],\
            [[-1,-1],[ 0,-1],[ 0, 0],[ 0, 1]],\
            [[ 0,-1],[ 0, 0],[ 0, 1],[ 1,-1]]\
          ],\
    'g' : [\
            [[-1, 0],[ 0, 0],[ 0, 1],[ 1, 0]],\
            [[]],\
            [[-1, 0],[ 0,-1],[ 0, 0],[ 0, 1]],\
            [[]],\
            [[-1, 0],[ 0,-1],[ 0, 0],[ 1, 0]],\
            [[]],\
            [[ 0,-1],[ 0, 0],[ 0, 1],[ 1, 0]],\
            [[]]\
          ],\
    'h' : [\
            [[ 0, 0],[ 0, 1],[ 1, 0],[ 1, 1]]\
          ],\
    'i' : [\
            [[ 0,-1],[ 0, 0],[ 1, 0],[ 1, 1]],\
            [[ 0, 0],[ 0, 1],[ 1,-1],[ 1, 0]],\
            [[-1, 1],[ 0, 0],[ 0, 1],[ 1, 0]],\
            [[-1, 0],[ 0, 0],[ 0, 1],[ 1, 1]]\
          ],\
    'j' : [\
            [[-2, 0],[-1, 0],[ 0, 0],[ 1, 0],[ 2, 0]],\
            [[]],\
            [[ 0,-2],[ 0,-1],[ 0, 0],[ 0, 1],[ 0, 2]]\
          ],\
    'k' : [\
            [[-2, 0],[-1, 0],[ 0, 0],[ 1,-1],[ 1, 0]],\
            [[-2, 0],[-1, 0],[ 0, 0],[ 1, 0],[ 1, 1]],\
            [[ 0,-2],[ 0,-1],[ 0, 0],[ 0, 1],[ 1, 1]],\
            [[-1, 1],[ 0,-2],[ 0,-1],[ 0, 0],[ 0, 1]],\
            [[-1, 0],[-1, 1],[ 0, 0],[ 1, 0],[ 2, 0]],\
            [[-1,-1],[-1, 0],[ 0, 0],[ 1, 0],[ 2, 0]],\
            [[-1,-1],[ 0,-1],[ 0, 0],[ 0, 1],[ 0, 2]],\
            [[ 0,-1],[ 0, 0],[ 0, 1],[ 0, 2],[ 1,-1]]\
          ],\
    'l' : [\
            [[-2, 0],[-1, 0],[ 0,-1],[ 0, 0],[ 1,-1]],\
            [[-2, 0],[-1, 0],[ 0, 0],[ 0, 1],[ 1, 1]],\
            [[ 0,-2],[ 0,-1],[ 0, 0],[ 1, 0],[ 1, 1]],\
            [[-1, 0],[-1, 1],[ 0,-2],[ 0,-1],[ 0, 0]],\
            [[-1, 1],[ 0, 0],[ 0, 1],[ 1, 0],[ 2, 0]],\
            [[-1,-1],[ 0,-1],[ 0, 0],[ 1, 0],[ 2, 0]],\
            [[-1,-1],[-1, 0],[ 0, 0],[ 0, 1],[ 0, 2]],\
            [[ 0, 0],[ 0, 1],[ 0, 2],[ 1,-1],[ 1, 0]]\
          ],\
    'm' : [\
            [[-1, 0],[ 0,-1],[ 0, 0],[ 1,-1],[ 1, 0]],\
            [[-1, 0],[ 0, 0],[ 0, 1],[ 1, 0],[ 1, 1]],\
            [[ 0,-1],[ 0, 0],[ 0, 1],[ 1, 0],[ 1, 1]],\
            [[-1, 0],[-1, 1],[ 0,-1],[ 0, 0],[ 0, 1]],\
            [[-1, 0],[-1, 1],[ 0, 0],[ 0, 1],[ 1, 0]],\
            [[-1,-1],[-1, 0],[ 0,-1],[ 0, 0],[ 1, 0]],\
            [[-1,-1],[-1, 0],[ 0,-1],[ 0, 0],[ 0, 1]],\
            [[ 0,-1],[ 0, 0],[ 0, 1],[ 1,-1],[ 1, 0]]\
          ],\
    'n' : [\
            [[-1,-1],[-1, 0],[ 0, 0],[ 1,-1],[ 1, 0]],\
            [[]],\
            [[ 0,-1],[ 0, 0],[ 0, 1],[ 1,-1],[ 1, 1]],\
            [[]],\
            [[-1, 0],[-1, 1],[ 0, 0],[ 1, 0],[ 1, 1]],\
            [[]],\
            [[-1,-1],[-1, 1],[ 0,-1],[ 0, 0],[ 0, 1]],\
            [[]]\
          ],\
    'o' : [\
            [[-1, 0],[ 0, 0],[ 0, 1],[ 1, 0],[ 2, 0]],\
            [[-1, 0],[ 0,-1],[ 0, 0],[ 1, 0],[ 2, 0]],\
            [[-1, 0],[ 0,-1],[ 0, 0],[ 0, 1],[ 0, 2]],\
            [[ 0,-1],[ 0, 0],[ 0, 1],[ 0, 2],[ 1, 0]],\
            [[-2, 0],[-1, 0],[ 0,-1],[ 0, 0],[ 1, 0]],\
            [[-2, 0],[-1, 0],[ 0, 0],[ 0, 1],[ 1, 0]],\
            [[ 0,-2],[ 0,-1],[ 0, 0],[ 0, 1],[ 1, 0]],\
            [[-1, 0],[ 0,-2],[ 0,-1],[ 0, 0],[ 0, 1]]\
          ],\
    'p' : [\
            [[-1, 0],[ 0, 0],[ 1,-1],[ 1, 0],[ 1, 1]],\
            [[]],\
            [[-1, 1],[ 0,-1],[ 0, 0],[ 0, 1],[ 1, 1]],\
            [[]],\
            [[-1,-1],[-1, 0],[-1, 1],[ 0, 0],[ 1, 0]],\
            [[]],\
            [[-1,-1],[ 0,-1],[ 0, 0],[ 0, 1],[ 1,-1]],\
            [[]]\
          ],\
    'q' : [\
            [[-2, 0],[-1, 0],[ 0, 0],[ 0, 1],[ 0, 2]],\
            [[]],\
            [[-2, 0],[-1, 0],[ 0,-2],[ 0,-1],[ 0, 0]],\
            [[]],\
            [[ 0,-2],[ 0,-1],[ 0, 0],[ 1, 0],[ 2, 0]],\
            [[]],\
            [[ 0, 0],[ 0, 1],[ 0, 2],[ 1, 0],[ 2, 0]],\
            [[]]\
          ],\
    'r' : [\
            [[-1,-1],[-1, 0],[ 0, 0],[ 0, 1],[ 1, 1]],\
            [[]],\
            [[-1, 0],[-1, 1],[ 0,-1],[ 0, 0],[ 1,-1]],\
            [[]],\
            [[-1,-1],[ 0,-1],[ 0, 0],[ 1, 0],[ 1, 1]],\
            [[]],\
            [[-1, 1],[ 0, 0],[ 0, 1],[ 1,-1],[ 1, 0]],\
            [[]]\
          ],\
    's' : [\
            [[-1,-1],[ 0,-1],[ 0, 0],[ 0, 1],[ 1, 1]],\
            [[-1, 1],[ 0,-1],[ 0, 0],[ 0, 1],[ 1,-1]],\
            [[-1, 0],[-1, 1],[ 0, 0],[ 1,-1],[ 1, 0]],\
            [[-1,-1],[-1, 0],[ 0, 0],[ 1, 0],[ 1, 1]]\
          ],\
    't' : [\
            [[-1,-1],[ 0,-1],[ 0, 0],[ 0, 1],[ 1, 0]],\
            [[-1, 1],[ 0,-1],[ 0, 0],[ 0, 1],[ 1, 0]],\
            [[-1, 0],[ 0, 0],[ 0, 1],[ 1,-1],[ 1, 0]],\
            [[-1,-1],[-1, 0],[ 0, 0],[ 0, 1],[ 1, 0]],\
            [[-1, 0],[ 0,-1],[ 0, 0],[ 0, 1],[ 1, 1]],\
            [[-1, 0],[ 0,-1],[ 0, 0],[ 0, 1],[ 1,-1]],\
            [[-1, 0],[-1, 1],[ 0,-1],[ 0, 0],[ 1, 0]],\
            [[-1, 0],[ 0,-1],[ 0, 0],[ 1, 0],[ 1, 1]]\
          ],\
    'u' : [\
            [[-1, 0],[ 0,-1],[ 0, 0],[ 0, 1],[ 1, 0]]\
          ],\
    }

    return all_pieces_shape

def getPiecesSize():
    '''
    [size,角の数]
    '''
    pieces_size = {\
    'a':[1,1],\
    'b':[2,2],\
    'c':[3,2],\
    'd':[3,3],\
    'e':[4,2],\
    'f':[4,3],\
    'g':[4,3],\
    'h':[4,4],\
    'i':[4,4],\
    'j':[5,2],\
    'k':[5,3],\
    'l':[5,4],\
    'm':[5,4],\
    'n':[5,4],\
    'o':[5,3],\
    'p':[5,3],\
    'q':[5,3],\
    'r':[5,5],\
    's':[5,4],\
    't':[5,4],\
    'u':[5,4]\
    }
    return pieces_size

def getUsedPieces(pieces):
    all_pieces = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u']
    used_pieces = []
    for one_piece in all_pieces :
        judge = 0
        for piece in pieces:
            if one_piece == piece :
                judge = 1
        if judge == 0 :
            used_pieces.append(one_piece)

    return  used_pieces

