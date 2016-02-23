import sys
import random
from random import randint
import time

class Gameboard:
	def __init__(self):
		self.board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
		self.score=0
		self.win=False
		self.lose=False
		self.nodes=[]
		self.moves=[]


	def __lt__(self,other):
			return self.score<other.score

	def __le__(self,other):
			return self.score<=other.score

	def __eq__(self,other):
			return self.score==other.score

	def __ne__(self,other):
			return self.score!=other.score

	def __gt__(self,other):
			return self.score>other.score

	def __ge__(self,other):
			return self.score>=other.score
	
	def copyboard(self, other):
			for col in range (0,4):
					for row in range(0,4):
						self.board[row][col]=other.board[row][col]

	def printboard(self):
		for row in range(0,4):
			print '|',
			for col in range(0,4):
				print '{:4} |'.format(self.board[row][col]),
			print ''
		print'\n'

	def findzero(self):
		result=[[]for i in range(2)]
		for row in range(0,4):
			for col in range(0,4):
				if self.board[row][col]==0:
					result[0].append(row)
					result[1].append(col)
		return result

	

	def upmove(self):
		moved=0
		for col in range(0,4):
			for row in range(1,4):
				if self.board[row][col]!=0:
					temp=row
					while temp-1>-1 and self.board[temp-1][col]==0:
						self.board[temp-1][col]=self.board[temp][col]
						self.board[temp][col]=0
						temp-=1
						moved=moved+1
		for col in range(0,4):
			for row in range(0,3):
				temp=row
				if self.board[row][col]!=0:
					if self.board[row][col]==self.board[temp+1][col]:
						self.board[temp][col]*=2
						self.score+=self.board[temp][col]
						moved=moved+1
						if self.board[row][temp]==2048:
							self.win=True
						
						temp+=1
						while temp<3:
							self.board[temp][col]=self.board[temp+1][col]
							temp+=1
							
						self.board[3][col]=0
		return moved
							

	def downmove(self):
		moved=0
		for col in range(0,4):
			for row in range(3,-1,-1):
				if self.board[row][col]!=0:
					temp=row
					while temp+1<4 and self.board[temp+1][col]==0:
						self.board[temp+1][col]=self.board[temp][col]
						self.board[temp][col]=0
						temp+=1
						moved=moved+1
		for col in range(0,4):
			for row in range(3,0,-1):
				temp=row
				if self.board[row][col]!=0:
					if self.board[row][col]==self.board[temp-1][col]:
						self.board[temp][col]*=2
						self.score+=self.board[temp][col]
						moved=moved+1
						if self.board[row][temp]==2048:
							self.win=True
						temp-=1
						while temp>0:
							self.board[temp][col]=self.board[temp-1][col]
							temp-=1
							
						self.board[0][col]=0
		return moved

	def leftmove(self):
		moved=0
		for row in range(0,4):
			for col in range(1,4):
				if self.board[row][col]!=0:
					temp=col
					while temp-1>-1 and self.board[row][temp-1]==0:
						self.board[row][temp-1]=self.board[row][temp]
						self.board[row][temp]=0
						temp-=1
						moved=moved+1
		for row in range(0,4):
			for col in range(0,3):
				temp=col
				if self.board[row][col]!=0:
					if self.board[row][col]==self.board[row][temp+1]:
						self.board[row][temp]*=2
						self.score+=self.board[row][temp]
						moved=moved+1
						if self.board[row][temp]==2048:
							self.win=True
						temp+=1
						while temp<3:
							self.board[row][temp]=self.board[row][temp+1]
							temp+=1
							
						self.board[row][3]=0
		return moved


	def rightmove(self):
		moved=0
		for row in range(0,4):
			for col in range(3,-1,-1):
				if self.board[row][col]!=0:
					temp=col
					while temp+1<4 and self.board[row][temp+1]==0:
						self.board[row][temp+1]=self.board[row][temp]
						self.board[row][temp]=0
						temp+=1
						moved=moved+1
		for row in range(0,4):
			for col in range(3,0,-1):
				temp=col
				if self.board[row][col]!=0:
					if self.board[row][col]==self.board[row][temp-1]:
						self.board[row][temp]*=2
						self.score+=self.board[row][temp]
						moved=moved+1
						if self.board[row][temp]==2048:
							self.win=True
						temp-=1
						while temp>0:
							self.board[row][temp]=self.board[row][temp-1]
							temp-=1
							
						self.board[row][0]=0
		return moved

	def addnum(self):
		spots=self.findzero()
		rando=randint(0,len(spots[1])-1)
		self.board[spots[0][rando]][spots[1][rando]]=2
	
	def fillmoves(self):
		temp=Gameboard()
		fillscore=0
		for movetries in range(0,4):
			temp.copyboard(self)
			temp.score=0
			if(movetries==0):
				if(temp.upmove()!=0):
					copy=Gameboard()
					copy.copyboard(temp)
					self.nodes.append(copy)
					self.nodes[-1].score=temp.score
					fillscore+=temp.score
					self.moves.append(movetries)
			elif(movetries==1):
				if(temp.downmove()!=0):
					copy=Gameboard()
					copy.copyboard(temp)
					self.nodes.append(copy)
					self.nodes[-1].score=temp.score
					fillscore+=temp.score
					self.moves.append(movetries)
			elif(movetries==2):
				if(temp.rightmove()!=0):
					copy=Gameboard()
					copy.copyboard(temp)
					self.nodes.append(copy)
					self.nodes[-1].score=temp.score
					fillscore+=temp.score
					self.moves.append(movetries)
			elif(movetries==3):
				if(temp.leftmove()!=0):
					copy=Gameboard()
					copy.copyboard(temp)
					self.nodes.append(copy)
					self.nodes[-1].score=temp.score
					fillscore+=temp.score
					self.moves.append(movetries)
		return fillscore

	def filltwos(self):
		temp=Gameboard()
		fillups=self.findzero()
		for zeroes in range(0,len(fillups[1])):
			temp.copyboard(self)
			temp.board[fillups[0][zeroes]][fillups[1][zeroes]]=2
			self.nodes.append(Gameboard())
			self.nodes[-1].copyboard(temp)

	def evalmove(self,depth):
		leftboard=Gameboard()
		leftboard.copyboard(self)
		rightboard=Gameboard()
		rightboard.copyboard(self)
		upboard=Gameboard()
		upboard.copyboard(self)
		downboard=Gameboard()
		downboard.copyboard(self)

		if leftboard.leftmove()!=0:
			curnode=leftboard
			curnode.filltwos()
			for it in range (0,depth):
				for it2 in range(0,len(curnode.nodes)-1):
					returner1=curnode
					curnode=curnode.nodes[it2]
					leftboard.score+=curnode.fillmoves()
					for it3 in range(0,len(curnode.nodes)-1):
						
						returner2=curnode
						curnode=curnode.nodes[it3]
						leftboard.score+=150*len(curnode.findzero()[1])
						#for row in range(0,4):
						#	for col in range(3,-1,-1):
						#		if curnode.board[row][col]==2048:
						#			leftboard.score=leftboard.score^2
						curnode.filltwos()
						curnode=returner2
					curnode=returner1
		

		if rightboard.rightmove()!=0:
			curnode=rightboard
			curnode.filltwos()
			for it in range (0,depth):
				for it2 in range(0,len(curnode.nodes)-1):
					returner1=curnode
					curnode=curnode.nodes[it2]
					rightboard.score+=curnode.fillmoves()
					
					for it3 in range(0,len(curnode.nodes)-1):
						
						returner2=curnode
						curnode=curnode.nodes[it3]
						rightboard.score+=100*len(curnode.findzero()[1])
						#for row in range(0,4):
						#	for col in range(3,-1,-1):
						#		if curnode.board[row][col]==2048:
						#			rightboard.score=rightboard.score^2
						curnode.filltwos()
						curnode=returner2
					curnode=returner1
					
		if upboard.upmove()!=0:
			curnode=upboard
			curnode.filltwos()
			for it in range (0,depth):
				for it2 in range(0,len(curnode.nodes)-1):
					returner1=curnode
					curnode=curnode.nodes[it2]
					upboard.score+=curnode.fillmoves()
					for it3 in range(0,len(curnode.nodes)-1):
						
						returner2=curnode
						curnode=curnode.nodes[it3]
						upboard.score+=50*len(curnode.findzero()[1])
						#for row in range(0,4):
							#for col in range(3,-1,-1):
								#if curnode.board[row][col]==2048:
								#	upboard.score=upboard.score^2
						curnode.filltwos()
						curnode=returner2
					curnode=returner1

		if downboard.downmove()!=0:
			curnode=downboard
			curnode.filltwos()
			for it in range (0,depth):
				for it2 in range(0,len(curnode.nodes)-1):
					returner1=curnode
					curnode=curnode.nodes[it2]
					downboard.score+=curnode.fillmoves()
					for it3 in range(0,len(curnode.nodes)-1):
						
						returner2=curnode
						curnode=curnode.nodes[it3]
						downboard.score+=200*len(curnode.findzero()[1])
						#for row in range(0,4):
							#for col in range(3,-1,-1):
							#	if curnode.board[row][col]==2048:
							#		downboard.score=downboard.score^2
						curnode.filltwos()
						curnode=returner2
					curnode=returner1

		print 'left={}'.format(leftboard.score)
		print 'right={}'.format(rightboard.score)
		print 'down={}'.format(downboard.score)
		print 'up={}'.format(upboard.score)

		lister=[upboard, downboard, leftboard, rightboard]
		lister.sort()
		if (lister[3].score==0):
			lastresort=self.findzero()
			if(lastresort[1][0]==0):
				self.leftmove()
			else:
				self.rightmove()
		else:
			if (lister[3]==upboard):
				self.upmove()
			elif (lister[3]==downboard):
				self.downmove()
			elif(lister[3]==leftboard):
				self.leftmove()
			elif ((lister[3]==rightboard)):
				self.rightmove()
		


def addnum(self):
		spots=self.findzero()
		rando=randint(0,len(spots[1])-1)
		self.board[spots[0][rando]][spots[1][rando]]=2



print'Welcome to my console version of 2048'
var2=raw_input("Press a key to continue, or x to exit\n")

while var2!='X' and var2!='x':
	print'NEW GAME \n'
	test=Gameboard()
	test.addnum()
	test.addnum()
	test.printboard()

	tempboard=Gameboard()


	var=raw_input("Please enter the number of moves you would like to look ahead\n")
	var3=raw_input("Please enter the pause time\n")
	while (var!='X' and var!='x') and test.lose==False and test.win==False:
		
		
		test.evalmove(int(var))
		test.addnum()
		print 'score:{}\n'.format(test.score)
		
		test.printboard()
		if (len(test.findzero()[1])<=1):
			checkloss=0
			for col in range (0,4):
				for row in range(0,4):
					tempboard.board[row][col]=test.board[row][col]

			checkloss=tempboard.upmove()
			checkloss=checkloss+tempboard.downmove()
			checkloss=checkloss+tempboard.leftmove()
			checkloss=checkloss+tempboard.rightmove()
			if checkloss==0:
				print'sorry, you lost'
				test.lose=True
				break
			
		if test.win==True:
			print'Congratulations, you won!'

		time.sleep(float(var3))

	var2=raw_input("Press any key to play again, or x to exit\n")
		

