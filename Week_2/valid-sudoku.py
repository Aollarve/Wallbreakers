class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        full_board = []
        for i in board:
            for e in i:
                full_board.append(e)
        
        count = 0
        for a in range(0,9,3):
            b = 0
            dic = {}
            for c in range(a,len(full_board),9):
                if b == 3:
                    # print(dic)
                    dic = {}
                    b = 0
                    
                for d in range(0,3):                  
                    # if(a==3):
                    #     print(c)
                    if full_board[c+d] != "." and full_board[c+d] in dic:
                        return False
                    else:
                        dic[full_board[c+d]] = 0
                b += 1
                
            for i in range(0,len(full_board),9):
                dic = {}
                for e in range(i,i+9):
                    if full_board[e] != "." and full_board[e] in dic:
                        return False
                    else:
                        dic[full_board[e]] = 0
                        
            for i in range(0,9):
                dic = {}
                for e in range(i,len(full_board),9):
                    if full_board[e] != "." and full_board[e] in dic:
                        return False
                    else:
                        dic[full_board[e]] = 0
                
        return True