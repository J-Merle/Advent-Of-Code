"""
Day 3 of the Advent of Code 2018
https://adventofcode.com/2018/day/3
"""
import re

RE_FROM = r'#([0-9]{0,10}) @ ([0-9]{0,10}),([0-9]{0,10}): ([0-9]{0,10})x([0-9]{0,10})'
RE_TO = r'\1 \2 \3 \4 \5'

def format_claim():
    claim_list = re.sub(RE_FROM, RE_TO, open('input.txt', 'r').read())
    return [[int(x) for x in claim.split()] for claim in claim_list.strip().split('\n')]


def init_room(room_size):
    return [[0 for size in range(room_size)] for size in range(room_size)]


def main(claim_list):
    room = init_room(1000)
    not_overlapped = set()

    for (_id, x, y, l, h) in claim_list:
        overlapped = False
        for i in range(y, y + h):
            for j in range(x, x + l):
                overlapped |= room[i][j] != 0
                if overlapped and room[i][j] in not_overlapped:
                    not_overlapped.remove(room[i][j])
                room[i][j] = -1 if room[i][j] != 0 else _id

        if not overlapped:
            not_overlapped.add(_id)

    print(sum(1 for sublist in room for x in sublist if x == -1))
    print(not_overlapped)

if __name__ == '__main__':
    main(format_claim())
