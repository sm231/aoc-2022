#A-X rock -> 1
#B-Y paper -> 2
#C-Z scissor -> 3
#win -> 6
#draw -> 3
#lose -> 0

symb = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}

def main():
    f = open('input.txt', 'r')
    score = 0
    for line in f:
        
        score += symb[line[:3]]
    f.close()
    print(score)

main()



