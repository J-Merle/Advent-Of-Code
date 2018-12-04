INPUT = open("input.txt", 'r').read()

def part_one():
    print("1: " + str(INPUT.count('(') - INPUT.count(')')))

def part_two():
    count = 0
    floor = 0
    for i in INPUT:
        if i == '(':
            floor += 1
        else:
            floor -= 1
        count += 1
        if floor < 0:
            print("2: " + str(count))
            return

if __name__ == '__main__':
    part_one() 
    part_two() 
