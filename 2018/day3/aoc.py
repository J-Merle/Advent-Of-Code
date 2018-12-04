"""
Day 3 of the Advent of Code 2018
https://adventofcode.com/2018/day/3
"""

def format_claim(claim):
    return [int(item) for item in claim.replace('#', '').replace(',', ' ').replace(':', '').replace('x', ' ').replace('@', '').split()];


def init_room(room_size):
    return [[0 for size in range(room_size)] for size in range(room_size)]

CLAIM_LIST = [format_claim(claim) for claim in open("input.txt", 'r')]

def part_one():
    room = init_room(1000)
    for (_id, x, y, l, h) in CLAIM_LIST:
        for i in range(y, y+h):
            for j in range(x, x+l):
                room[i][j] += 1

    print(sum(1 for sublist in room for x in sublist if x > 1))

def part_two():
    room = init_room(1000)
    overlap_dict = {'overlapped': set(), 'notoverlapped': set()}

    for (_id, x, y, l, h) in CLAIM_LIST:
        overlapped = False
        for i in range(y, y+h):
            for j in range(x, x+l):
                previous_value = room[i][j]
                overlapped |= previous_value > 0
                room[i][j] = _id
                if overlapped:
                    overlap_dict['overlapped'].add(_id)
                    overlap_dict['overlapped'].add(previous_value)
        if not overlapped:
            overlap_dict['notoverlapped'].add(_id)

    print(overlap_dict['notoverlapped']- overlap_dict['overlapped'])

if __name__ == '__main__':
    part_one()
    part_two()
