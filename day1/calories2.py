def sort(array):
    i = len(array) - 1
    while i > 0 and array[i] > array[i-1]:
        tmp = array[i]
        array[i] = array[i-1]
        array[i-1] = tmp
        i -= 1
        
def main():
    f = open('input.txt', 'r')
    calories = []
    cal = 0
    for line in f:
        if line == '\n':
            calories.append(cal)
            sort(calories)
            cal = 0
        else:
            cal += int(line)
    f.close()
    result = calories[0]
    print(result)
    for i in range(1, 3):
        result += calories[i]
    print(result)

main()
