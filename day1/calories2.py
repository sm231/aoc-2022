def partition(array, low, high):
 
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] >= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

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
    #quickSort(calories, 0, len(calories) - 1)
    result = calories[0]
    print(result)
    for i in range(1, 3):
        result += calories[i]
    print(result)

main()
