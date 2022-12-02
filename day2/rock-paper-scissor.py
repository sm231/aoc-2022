
symb1 = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}

symb2 = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}

def main():
    f = open('input.txt', 'r')
    score1 = 0
    score2 = 0
    for line in f:
        score1 += symb1[line[:3]]
        score2 += symb2[line[:3]]
    f.close()
    print(score1, score2)
main()



