def sort(array):
    i = 3
    while i > 0 and array[i] > array[i-1]:
        tmp = array[i]
        array[i] = array[i-1]
        array[i-1] = tmp
        i -= 1
        
def main():
    f = open('/home/sm/advent-of-code/2022/day1/input.txt')
    calories = [0, 0, 0, 0]
    cal = 0
    for line in f:
        if line == '\n':
            # calories of the next elf. So place in the list and sort list with insertionSort on the last index. Carry on by resetting cal to 0
            calories[3] = cal
            sort(calories)
            cal = 0
        else:
            # sum the total calories of the elf
            cal += int(line)
    f.close()
    #calories is a sorted array from biggest to smallest for the elfs.
    result = calories[0]
    print(result)
    for i in range(1, 3):
        result += calories[i]
    print(result)

main()
