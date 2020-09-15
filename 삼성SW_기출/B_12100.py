"""
url : https://www.acmicpc.net/problem/12100
problem : 2048(Easy)
algorithm : 브루트포스
"""
import copy
N = int(input())
B = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1,1,0,0], [0,0,-1,1]
ret = -1
def solution():

    def move_left(board):
        for i in range(N):                      
            p_idx = 0
            p_val = 0
            for j in range(N):                          
                if board[i][j] == 0:                # 현재값이 0이면
                    continue                            # 건너뛴다
                if p_val == 0:                      # prev_val 0이면
                    p_val = board[i][j]                 # p_val 현재값 할당
                else:
                    if p_val == board[i][j]:        # 이전값과 현재값 같다면
                        board[i][p_idx] = 2*p_val       # 이전값 2배
                        p_val = 0                       # prev_val 0으로 초기화
                        p_idx += 1                      # prev_idx 오른쪽으로 이동
                    else:                           # 이전값과 현재값 다르면
                        board[i][p_idx] = p_val         # 이전값에 p_val 할당
                        p_val = board[i][j]             # p_val 현재값 할당
                        p_idx += 1                      # p_idx 오른쪽으로 이동
                board[i][j] = 0                     # 현재값 0으로 초기화
            if p_val != 0:                      # p_val 0이 아니라면
                board[i][p_idx] = p_val             # 이전값에 p_val 할당
        return board

    def move_right(board):
        for i in range(N):
            p_idx = N-1
            p_val = 0
            for q in range(N-1, -1, -1):
                if board[i][q] == 0:                    
                    continue 
                if p_val == 0:                          
                    p_val = board[i][q]                
                else:                                   
                    if p_val == board[i][q]:            
                        board[i][p_idx] = 2*p_val       
                        p_val = 0                       
                        p_idx -= 1                      
                    else:                               
                        board[i][p_idx] = p_val         
                        p_idx -= 1                      
                        p_val = board[i][q]             
                board[i][q] = 0                         
            if p_val != 0: 
                board[i][p_idx] = p_val                 
        return board

    def move_up(board):
        for i in range(N):
            p_idx = 0
            p_val = 0
            for j in range(N):
                if board[j][i] == 0:
                    continue
                if p_val == 0:
                    p_val = board[j][i]
                else:
                    if p_val == board[j][i]:
                        board[p_idx][i] = 2*p_val
                        p_val = 0
                        p_idx += 1
                    else:
                        board[p_idx][i] = p_val
                        p_val = board[j][i]
                        p_idx += 1
                board[j][i] = 0
            if p_val != 0:
                board[p_idx][i] = p_val
        return board
        
    def move_down(board):
        for i in range(N):
            p_idx = N-1
            p_val = 0
            for j in range(N-1, -1, -1):
                if board[j][i] == 0:                    
                    continue 
                if p_val == 0:                          
                    p_val = board[j][i]                
                else:                                   
                    if p_val == board[j][i]:            
                        board[p_idx][i] = 2*p_val       
                        p_val = 0                       
                        p_idx -= 1                      
                    else:                               
                        board[p_idx][i] = p_val         
                        p_idx -= 1                      
                        p_val = board[j][i]             
                board[j][i] = 0     
            if p_val != 0: 
                board[p_idx][i] = p_val                 
        return board
        

    def find_max(arr):
        global ret
        for i in range(N):
            ret = max(ret, max(arr[i]))

    def dfs(arr, cnt):
        if cnt == 5:
            find_max(arr)
            return
        
        dfs(move_up(copy.deepcopy(arr)), cnt+1)
        dfs(move_down(copy.deepcopy(arr)), cnt+1)
        dfs(move_right(copy.deepcopy(arr)), cnt+1)
        dfs(move_left(copy.deepcopy(arr)), cnt+1)


    dfs(B, 0)
    print(ret)


solution()

