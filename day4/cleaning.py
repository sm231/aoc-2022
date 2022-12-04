
def main():
    f = open('input.txt')
    result1 = 0
    result2 = 0
    for line in f:
        arr = line.split(",", 1)
        elf1 = [int(x) for x in arr[0].split("-", 1)]
        elf2 = [int(x) for x in arr[1].split("-", 1)]
        if (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]) or (elf2[0] >= elf1[0] and elf2[1] <= elf1[1]):
            result1 += 1
        if not(elf2[0] > elf1[1] or elf2[1] < elf1[0]):
            result2 += 1
    print(result1, result2)
main()
