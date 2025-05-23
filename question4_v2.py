def load_list_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        # Remove newline characters from each line
        return [line.strip() for line in lines]

def question4_p1(matrix):
    word = 'XMAS'
    n = len(matrix)
    m = len(matrix[0])
    count = 0

    directions = [(-1,-1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1), (1, 0),  (1, 1)]
    
    for i in range(n):
        for j in range(m):
            for rowstep, colstep in directions:
                match = True
                for k in range(len(word)):
                    row = i + rowstep*k
                    col = j + colstep*k
                    if 0 <= row < n and 0 <= col < m:
                        if matrix[row][col] != word[k]:
                            match = False
                            break
                    else:
                        match = False
                        break
                if match:
                    count += 1
    return count

def question4_p2(matrix):
    # word = 'MAS'
    n = len(matrix)
    m = len(matrix[0])
    count = 0
    word = [("M", "A", "S"), ("S", "A", "M")]

    directions = [(-1,-1), (-1, 1),
                  (1, -1), (1, 1)]
    
    for i in range(1, n-1):
        for j in range(1, m-1):
            if matrix[i][j] != "A":
                continue

            OR = matrix[i][j]
            NW = matrix[i-1][j-1]
            NE = matrix[i-1][j+1]
            SW = matrix[i+1][j-1]
            SE = matrix[i+1][j+1]

            if ((NW, OR, SE) in word) and ((NE, OR, SW) in word):
                count += 1
    return count

# for testing purposes only
def printmatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print(" ")
    print(" ")

if __name__ == "__main__":
    file_name = "q4_input.txt"
    giveninput = load_list_from_file(file_name)
    test = ['MMMSXXMASM', 'MSAMXMSMSA','AMXSXMAAMM','MSAMASMSMX','XMASAMXAMM','XXAMMXXAMA','SMSMSASXSS','SAXAMASAAA','MAMMMXMMMM','MXMXAXMASX']

    # print(giveninput)
    # printmatrix(test)
    print(question4_p2(giveninput))