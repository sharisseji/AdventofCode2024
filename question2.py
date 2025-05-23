def load_matrix_from_file(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            # Strip leading/trailing spaces and split by whitespace
            numbers = [int(num) for num in line.strip().split()]
            if numbers:  # Ignore empty lines
                matrix.append(numbers)
    return matrix


#-----------------------PART 1----------------------#
def check_rowsafe1(row, increase):
    for i in range(1,len(row)):            
        distance = row[i] - row[i-1]
        # print(row[i], end=" ")

        if ((distance>0) and (increase == False)) or ((distance <0) and (increase == True)):
            return 1 # unsafe
             
        if (abs(distance) < 1) or (abs(distance) > 3):
            return 1          
    return 0 # safe

def question2_p1(matrix): # rows: reports, columns: levels
    unsafecount = 0
    for i in range(len(matrix)):
        increase = False
        if (matrix[i][1] - matrix[i][0]) > 0:
            increase = True 
        unsafecount += check_rowsafe1(matrix[i], increase)

    return len(matrix)-unsafecount

    # unsafecount = 0
    # for i in range(len(matrix)):
    #     increase = False
    #     if (matrix[i][1] - matrix[i][0]) > 0:
    #         increase = True 
    #     for j in range(1,len(matrix[i])):
    #         # print(matrix[i][j], end=' ')                        
    #         distance = matrix[i][j] - matrix[i][j-1]
    #         # print(distance)

    #         if ((distance>0) and (increase == False)) or ((distance <0) and (increase == True)):
    #             unsafecount +=1
    #             break
            
    #         if (abs(distance) < 1) or (abs(distance) > 3):
    #             unsafecount += 1
    #             break              
    #     # print("")
    # return len(matrix)-unsafecount


#---------------------PART 2----------------------#
def check_rowsafe2(row, increase):
    for i in range(1,len(row)):            
        distance = row[i] - row[i-1]
        if ((distance>0) and (increase == False)) or ((distance <0) and (increase == True)):
            return False # unsafe
            
        if (abs(distance) < 1) or (abs(distance) > 3):
            return False # unsafe         
    return True # safe

def check_safe_with_skip(row,increase):
    if check_rowsafe2(row, increase):
        # print(f"{row}: Safe without removing")
        return True
    else:
        for i in range(len(row)):
            print(row[:i] + row[i+1:])
            if check_rowsafe2(row[:i] + row[i+1:], increase):
                print(f"{row}: Safe after removing level {i+1}, {row[i]}")
                return True
    print(f"{row}: Unsafe regardless of which level is removed")
    return False


def question2_p2(matrix): # rows: reports, columns: levels
    safecount = 0
    for i in range(len(matrix)):
        increase = False
        removed = 0
        if (matrix[i][1] - matrix[i][0]) > 0:
            increase = True
        
        if check_safe_with_skip(matrix[i],increase) == True:
            safecount +=1
            removed = 1
    return safecount


#--------------------------MAIN---------------------------#
if __name__ == "__main__":
    file_path = "q2_input.txt"  # Replace with your actual file path
    matrix = load_matrix_from_file(file_path)

    # print(question2_p2([[7,6,4,2,1],[1,2,7,8,9],[9,7,6,2,1],[1,3,2,4,5],[8,6,4,4,1],[1,3,6,7,9]]))

    # print(matrix)

    print(question2_p2(matrix))
    # test = [0,1,2,3,4,5]
    # print(test[3+1:])