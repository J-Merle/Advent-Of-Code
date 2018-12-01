""" Day 1 of Advent of code 2018
    https://adventofcode.com/2018/day/1
"""

VARIATION_LIST = [int(variation) for variation in open("input.txt", "r")]

def part_one():
    print("1: " +  str(sum(VARIATION_LIST)))

def part_two():
    reached_values = set()
    frequency = 0
    while True:
        for variation in VARIATION_LIST:
            frequency += variation
            if frequency in reached_values:
                print("2: " + str(frequency))
                exit()
            reached_values.add(frequency)

if __name__ == '__main__':
    part_one()
    part_two()
