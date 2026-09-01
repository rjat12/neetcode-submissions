class Solution:
    def validate_row(self,row:List[str]) -> int:
        arr = []
        for i in range(len(row)):
            if row[i]!='.':
                if(int(row[i])<1 or int(row[i])>9):
                    return 1
                elif(row[i] in arr):
                    return 1
                else:
                    arr.append(row[i])
        return 0
    def validate_box(self,row):
        arr = []
        for i in range(len(row)):
            for j in range(len(row[i])):
                if row[i][j] != '.':
                    if(int(row[i][j])<0 or int(row[i][j])>9):
                        print('D')
                        return 1
                    elif(row[i][j] in arr):
                        print('E')
                        return 1
                    else:
                        arr.append(row[i][j])
        return 0
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            if(self.validate_row(board[i])!=0):
                print('A')
                return False
        for i in range(len(board)):
            arr = []
            for j in range(len(board)):
                arr.append(board[j][i])
            if(self.validate_row(arr)!=0):
                print('B')
                return False
        for i in range(3):
            for j in range(3):
                arr=[]
                arr.append([board[(i*3)][j*3],board[(i*3)][(j*3)+1],board[(i*3)][(j*3)+2]])
                arr.append([board[(i*3)+1][j*3],board[(i*3)+1][(j*3)+1],board[(i*3)+1][(j*3)+2]])
                arr.append([board[(i*3)+2][j*3],board[(i*3)+2][(j*3)+1],board[(i*3)+2][(j*3)+2]])
                print(arr)
                print('/n')
                if(self.validate_box(arr)!=0):
                    print('C')
                    return False
        return True
        
        
            
        

        