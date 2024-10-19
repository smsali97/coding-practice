def make_board(n,queens):
    board = [[False for _ in range(n)] for _ in range(n)]
    
    for _ in queens:
        for n1 in range(n):
            board[n1][i] = True            
            board[j][n1] = True
        
        # Positive diagnol 
        i2 = i
        j2 = j
        while i2 < n and j2 < n:
            print(i2,j2)
            board[i2][j2] = True
            if i2 < n: i2 +=1
            if j2 < n: j2 +=1
            
        print('pos done 1/2 --------')
        
        i2 = i
        j2 = j    
        while i2 > 0 or j2 > 0:
            board[i2][j2] = True
            if i2 > 0: i2 -=1
            if j2 > 0: j2 -=1
            
        print('pos done --------')
        
        # Negative Diagnal
        i2 = i
        j2 = j
        while i2 < n or j2 > 0:
            board[i2][j2] = True
            if i2 < n: i2 +=1 
            if j2 > 0: j2 -=1
        
        print('neg done 1/2 --------')

        
        i2 = i
        j2 = j
        while j2 < n or i2 > 0:
            board[i2][j2] = True
            if i2 > 0: i2 -=1
            if j2 < n: j2 +=1
            
        print('neg done --------')

                
    return board


def solution(n, queens, queries):
    board = make_board(n,queens)
    
    for line in board:
        for piece in board:
            if piece: print('1',sep=' ')
            if not piece: print('0',sep=' ')
        print('\n',sep='')
    
    responses = []
    for query in queries:
        i, j = query
        responses.append(board[i][j])
    return responses    
    
