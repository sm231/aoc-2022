from itertools import islice
import numpy as np
def makemat(f):
    mat = np.empty((8, 9), str)
    i = 0
    for line in islice(f, 8):
        j = 0
        for k in range(1, 34, 4):
            mat[i][j] = line[k]
            j += 1
        i += 1
    mat2 = [None] * 9
    for j in range(9):
        collumn = ""
        for i in range(7, -1, -1):
            collumn += mat[i][j]
        collumn = collumn.strip()
        mat2[j] = list(collumn)
    return mat2

def move(intr, mat):
    for i in range(intr[0]):
        move = mat[intr[1] - 1].pop()
        mat[intr[2] - 1].append(move)
        
def main():
    f = open('input.txt')
    mat = makemat(f)
    for line in islice(f, 2, None):
        nums = [int(x) for x in line.split() if x.isdigit()]
        move(nums, mat)
    result = "" 
    for i in mat:
        result += i[-1]
    print(result)
main()
