def question2(matrix): # rows: reports, columns: levels
    unsafecount = 0
    increase = False
    for i in range(len(matrix)):
        if (matrix[i][1] - matrix[i][0]) > 0:
            increase = True 
        for j in range(1,len(matrix[i])):
            # print(matrix[i][j], end=' ')                        
            distance = matrix[i][j] - matrix[i][j-1]
            # print(distance)

            if ((distance>0) and (increase == False)) or ((distance <0) and (increase == True)):
                unsafecount +=1
                break
            
            if (abs(distance) < 1) or (abs(distance) > 3):
                unsafecount += 1
                break                
        # print("")
    return len(matrix)-unsafecount

print(question2([[7,6,4,2,1],[1,2,7,8,9],[9,7,6,2,1],[1,3,2,4,5],[8,6,4,4,1],[1,3,6,7,9]]))  