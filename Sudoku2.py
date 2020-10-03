sudoku = [

    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]

]

def mostrameglio (sudoku):
    for i in range (0, len(sudoku)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range (0, len(sudoku[0])):
            if j % 3 == 0 and j!= 0:
                print(" | ", end="")
            if j == 8:
                print(sudoku[i][j])
            else:
                print(str(sudoku[i][j])+ " ", end="")




def solve(sudoku):
    find = findblank(sudoku)
    if not find:
        return True
    else:
        row, col = find
    for i in range (1,10):
        if valid(sudoku, i,(row, col)):
            sudoku[row][col] = i
            if solve(sudoku):
                return True
            sudoku[row][col] = 0
    return False


def valid (sudoku, num, pos):
    for i in range (0, len(sudoku[0])):
        if sudoku[pos[0]][i] == num and pos[1] != i:
            return False
    for j in range (0, len(sudoku)):
        if sudoku[j][pos[1]] == num and pos[0] != j:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] //3
    for i in range (box_y*3, box_y*3 +3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if sudoku[i][j] == num and (i, j) !=  pos:
                return False
    return True



def findblank (sudoku):
    for i in range (0, len(sudoku)):
        for j in range (0, len(sudoku[0])):
            if sudoku[i][j] == 0:
                return (i, j)  #raw colon
    return None
print(mostrameglio(sudoku))
solve(sudoku)
print("\n\n")
print(mostrameglio(sudoku))