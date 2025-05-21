def antiDiagonalOrder(mat):
    res = []
    n = len(mat)
    m = len(mat[0])

    # First half: starting from the top row, right to left
    for col in range(m - 1, -1, -1):
        i, j = 0, col
        while i < n and j < m:
            res.append(mat[i][j])
            i += 1
            j += 1

    # Second half: starting from the second row (to avoid repeating [0][0])
    for row in range(1, n):
        i, j = row, 0
        while i < n and j < m:
            res.append(mat[i][j])
            i += 1
            j += 1

    return res

if __name__ == "__main__":
    mat = [
        [ 1,  2,  3,  4 ],
        [ 5,  6,  7,  8 ],
        [ 9, 10, 11, 12 ],
        [13, 14, 15, 16 ]
    ]
    res = antiDiagonalOrder(mat)
    print(" ".join(map(str, res)))
