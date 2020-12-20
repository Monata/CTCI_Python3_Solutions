# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
# write a method to rotate the image by 90 degrees. Can you do this in place?

def rotate_matrix(inp):
    i = 0
    l = len(inp[0])
    res = [[0 for i in range(l)] for j in range(l)]
    l -= 1
    while i <= l:
        j = 0
        while j <= l:
            res[i][j] = inp[l-j][i]
            j += 1
        i += 1
    return res

def rotate_matrix_in_place(inp):
    i = 0
    l = len(inp[0])
    l -= 1
    while i < l:
        j = i
        while j < l - i:
            temp = inp[i][j]
            inp[i][j] = inp[l-j][i]
            inp[l-j][i] = inp[l-i][l-j]
            inp[l - i][l - j] = inp[j][l-i]
            inp[j][l - i] = temp
            j += 1
        i += 1
    return inp



if __name__ == "__main__":
    print("MatrixRotate")
    check = [
        ([[1, 1, 1, 2],
          [4, 0, 9, 2],
          [4, 9, 0, 2],
          [4, 3, 3, 3]]
         ,

         [[4, 4, 4, 1],
          [3, 9, 0, 1],
          [3, 0, 9, 1],
          [3, 2, 2, 2]]
         ),
        ([[1, 1, 1],
          [4, 0, 2],
          [1, 1, 1]]
         ,

         [[1, 4, 1],
          [1, 0, 1],
          [1, 2, 1]]
         )
    ]

    for i in check:
        assert (rotate_matrix(i[0]) == i[1])
        assert (rotate_matrix_in_place(i[0]) == i[1])
