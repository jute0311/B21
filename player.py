
from blokus.player import Player
from blokus.utils import encodeFourCode

from players.B21.decidethebesthand import decideTheBestHand
from players.B21.makefield import *

import time

class CPlayer(Player):
	def __init__(self):
		super().__init__()

		self.count = 0
		self.logs = []
		self.number = 0 #自分の順番を格納
		
	def log(self, player, move):
		self.logs.append((player, move))

	def move(self, board, pieces):
		self.count += 1
		'''
		__________________________
		自分が何番目のplayerか把握
		__________________________
		'''
		if self.count == 1:
			if board[0][0] != 0:
				self.number = 4
			elif board[0][19] != 0:
				self.number = 3
			elif board[19][19] != 0:
				self.number = 2
			else :
				self.number = 1
		
		'''
		__________________________________________________________________
		field作成
		__________________________________________________________________
		'''
		p1 = [1,1]
		p2 = [0,0]
		p3 = [0,0]
		p4 = [0,0]
		(field,player1,player2,player3,player4) = getField(board,p1,p2,p3,p4)
		'''
		_____________________________________________________________________
		打つ手を決定
		_____________________________________________________________________
		'''
		if self.count == 1:
			hand = encodeFourCode(17, 0, 'o', 0)
		elif self.count == 2:
			hand = encodeFourCode(15, 2, 'u', 0)
		elif self.count == 3:
			hand = encodeFourCode(13, 4, 't', 1)
		else:
			hand = decideTheBestHand(self.number,field,player1,pieces,self.count,board)
			
		return hand
		