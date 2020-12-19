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


if __name__ == "__main__":
    print("MatrixRotate")
    check = [
        ([[1, 1, 1, 2],
          [4, 0, 0, 2],
          [4, 0, 0, 2],
          [4, 3, 3, 3]]
         ,

         [[4, 4, 4, 1],
          [3, 0, 0, 1],
          [3, 0, 0, 1],
          [3, 2, 2, 2]]
         )]

    for i in check:
        assert (rotate_matrix(i[0]) == i[1])
