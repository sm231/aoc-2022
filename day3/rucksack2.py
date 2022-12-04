import linecache

symb = {"a": 1,"b": 2,"c": 3,"d": 4,"e": 5,"f": 6,"g": 7,"h": 8,"i": 9,"j": 10,"k": 11,"l": 12,"m": 13,"n": 14,"o": 15,"p": 16,"q": 17,"r": 18,"s": 19,"t": 20,"u": 21,"v": 22,"w": 23,"x": 24,"y": 25,"z": 26,"A": 27,"B": 28,"C": 29,"D": 30,"E": 31,"F": 32,"G": 33,"H": 34,"I": 35,"J": 36,"K": 37,"L": 38,"M": 39,"N": 40,"O": 41,"P": 42,"Q": 43,"R": 44,"S": 45,"T": 46,"U": 47,"V": 48,"W": 49,"X": 50,"Y": 51,"Z": 52}

def findbadge(elf1, elf2, elf3):
    for i in range(len(elf1)):
        for j in range(len(elf2)):
            if elf1[i] == elf2[j]:
                for k in range(len(elf3)):
                    if elf2[j] == elf3[k]:
                        return elf3[k]

def main():
    path = "/home/sm/advent-of-code/2022/day3/input.txt"
    maxline = len(open(path).readlines())
    result = 0
    for i in range(1, maxline, 3):
        elf1 = linecache.getline(path, i)
        elf2 = linecache.getline(path, i + 1)
        elf3 = linecache.getline(path, i + 2)
        badge = findbadge(elf1[:-1], elf2[:-1], elf3[:-1])
        result += symb[badge]
        i += 3
    print(result)
main()
