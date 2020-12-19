# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

def zero_matrix(inp):
    stack =[]
    i = 0
    ly = len(inp[0])
    lx = len(inp)
    while i < lx:
        j = 0
        while j < ly:
            if inp[i][j] == 0:
                stack.append((i,j))
            j += 1
        i += 1
    for x,y in stack:
        i = 0
        while i < lx:
            inp[i][y] = 0
            i += 1
        i = 0
        while i < ly:
            inp[x][i] = 0
            i+= 1
    return inp

if __name__ == "__main__":
    print("ZeroMatrix")
    check = [
        ([[1, 1, 1, 2],
          [4, 0, 9, 2],
          [4, 9, 9, 2],
          [4, 3, 3, 3]]
         ,

         [[1, 0, 1, 2],
          [0, 0, 0, 0],
          [4, 0, 9, 2],
          [4, 0, 3, 3]]
         ),
        ([[1, 1, 1],
          [4, 0, 0],
          [1, 1, 1]]
         ,

         [[1, 0, 0],
          [0, 0, 0],
          [1, 0, 0]]
         ),
        ([[1, 1, 0],
          [4, 2, 2]]
         ,

         [[0, 0, 0],
          [4, 2, 0]]
         )
    ]

    for i in check:
        assert (zero_matrix(i[0]) == i[1])
