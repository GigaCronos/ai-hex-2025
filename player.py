import random
import collections as stl
from board import HexBoard
class Player:
    def __init__(self, player_id: int):
        self.player_id = player_id  # Tu identificador (1 o 2)

    def play(self, board: HexBoard) -> tuple:
        raise NotImplementedError("¡Implementa este método!")
    

class myPlayer(Player):
    def __init__(self, player_id: int):
        self.player_id = player_id 

    def play(self, board: HexBoard) -> tuple:
        nboard=board.clone()
        return self.get_best_move(nboard,self.player_id,4)[1]
    
    def get_best_move(self,board: HexBoard, player_id : int, depth: int ):
        bests=[]
        for i in range(0,board.size):
            for j in range(0,board.size):
                if board.board[i][j] == 0:
                    bests.append((max(self.evaluate(board,player_id,i,j),1-self.evaluate(board,3-player_id,i,j)),(i,j)))
        bests=sorted(bests,key=lambda tupla: tupla[0], reverse=True)
        if(depth==0):
            return bests[0]
       
       
        if bests[0][0]>0.99999:
            if player_id == self.player_id:
                return bests[0]
            else:
                return (1-bests[0][0],bests[0][1])
       
        branch=2*depth
        if len(bests)>branch:
            bests=bests[:branch]
        ans=(-1,(0,0))
        if player_id!=self.player_id:
            ans=(2,(0,0))
        
        for tup in bests:
            board.board[tup[1][0]][tup[1][1]]=player_id
            ntup=self.get_best_move(board,3-player_id,depth-1)
            board.board[tup[1][0]][tup[1][1]]=0
            if player_id == self.player_id:
                if ans[0]<ntup[0]:
                    ans=(ntup[0],tup[1])
            else:
                if ans[0]>ntup[0]:
                    ans=(ntup[0],tup[1])
                
        return ans

    def evaluate(self, board: HexBoard, player_id : int, row :int, col :int):
        path_sizes=[]
        originals=[]
        board.board[row][col]=player_id
        originals.append((row,col))
        tot=board.size*board.size
        for _ in range(0,4):
            lis=self.find_path(board,player_id,row,col)
            if lis is None:
                path_sizes.append(tot)
                break
            
            path_sizes.append(len(lis))
            if len(lis)==0:
                break
            tup=random.choice(lis)
            originals.append(tup)
            board.board[tup[0]][tup[1]]=3-player_id
        
        for tup in originals:
            board.board[tup[0]][tup[1]]=0

        ans=0
        mul=1
        
        for i in range(len(path_sizes)):
            ans=ans+mul*(tot-path_sizes[i])/tot
            mul=mul*path_sizes[i]/tot

        return ans

    def find_path(self, board: HexBoard,player_id: int, row : int, col: int):
        Dir = [
            (0, -1),   # Izquierda
            (0, 1),    # Derecha
            (-1, 0),   # Arriba
            (1, 0),    # Abajo
            (-1, 1),   # Arriba derecha
            (1, -1)    # Abajo izquierda
        ]

        D=[[-1 for _ in range(board.size)] for _ in range(board.size)]
        Q=stl.deque()
        D[row][col]=-2
        Q.append((row,col))
        b1=-1
        b2=-1
        while Q.count()!=0:
            u=Q[0]
            Q.popleft()
            for dir in Dir:
                ndir=(u[0]+dir[0],u[1]+dir[1])
                if ndir[0]<0 or ndir[0]>=board.size or ndir[1]<0 or ndir[1]>=board.size:
                    continue
                if board.board[ndir[0]][ndir[1]]==3-player_id:
                    continue
                if board.board[ndir[0]][ndir[1]]==0 and D[ndir[0]][ndir[1]]==-1:
                    Q.append(ndir)
                    D[ndir[0]][ndir[1]]=u[0]*board.size+u[1]
                if board.board[ndir[0]][ndir[1]]==player_id and D[ndir[0]][ndir[1]]==-1:
                    Q.appendleft(ndir)
                    D[ndir[0]][ndir[1]]=u[0]*board.size+u[1]
            
            if u[0]==0 and player_id==2 and b1==-1:
                b1=u[0]*board.size+u[1]
            if u[0]==board.size-1 and player_id==2 and b2==-1:
                b2=u[0]*board.size+u[1]
            if u[1]==0 and player_id==1 and b1==-1:
                b1=u[0]*board.size+u[1]
            if u[1]==board.size-1 and player_id==1 and b2==-1:
                b2=u[0]*board.size+u[1]  

        if b1==-1 or b2==-1:
            return None
        
        ans=[]
        while b1!=-2:
            r=b1//board.size
            c=b1%board.size
            if(board.board[r][c]==0):
                ans.append((r,c))
            b1=D[r][c]
        while b2!=-2:
            r=b2//board.size
            c=b2%board.size
            if(board.board[r][c]==0):
                ans.append((r,c))
            b2=D[r][c]

        return ans