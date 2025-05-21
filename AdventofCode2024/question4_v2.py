def question4(matrix):
    word = 'XMAS'
    n = len(matrix)
    m = len(matrix[0])
    count = 0

    directions = [(-1,-1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1), (1, 0),  (1, 1)]
    
    for i in range(n):
        for j in range(m):
            for row, col in directions:
                match = True
                for k in range(len(word)):
                    row = i + row*i