"""
Day 2 of the advent of code 2018
https://adventofcode.com/2018/day/2
"""
from itertools import combinations

ID_LIST = [id.strip('\n') for id in open('input.txt', 'r')]

def part_one():
    l2 = 0
    l3 = 0
    for _id in ID_LIST:
        id_set = set(_id)
        available_occurences = {2, 3}
        for letter in id_set:
            occurence = _id.count(letter)
            if occurence in available_occurences:
                if occurence == 2:
                    l2 += 1
                    available_occurences.remove(2)
                elif occurence == 3:
                    l3 += 1
                    available_occurences.remove(3)
    print('1: ' + str(l2 * l3))

def part_two():
    id_combinations = combinations(ID_LIST, 2)
    for id_1, id_2 in id_combinations:
        id_zip = zip(id_1, id_2)
        matching_letters = [a for (a,b) in id_zip if a == b]
        if(len(matching_letters) == len(id_1) - 1):
            print(''.join(matching_letters))



if __name__ == '__main__':
    part_one()
    part_two()

