def main():
    f = open('input.txt')
    i = 14 # i = 4 part 1
    for line in f:
        for k in range(0, len(line)):
            seq = set(line[0+k:14+k])  #seq = set(line[0+k:4+k]) part 1
            if len(seq) == 14:         #len(seq) == 4 part 1
                print(i)
                break
            i += 1
main()
