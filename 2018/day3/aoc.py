"""
Day 3 of the Advent of Code 2018
https://adventofcode.com/2018/day/3
"""
import re



def format_claim(claim):
    # input
    # #1 @ 432,394: 29x14
    regexp = '#([0-9]{0,10}) @ ([0-9]{0,10}),([0-9]{0,10}): ([0-9]{0,10})x([0-9]{0,10})'
    claim_search = re.search(regexp, claim)
    return (int(claim_search.group(1)),
            int(claim_search.group(2)),
            int(claim_search.group(3)),
            int(claim_search.group(4)),
            int(claim_search.group(5))
            )


def init_room(room_size):
    return [[0 for size in range(room_size)] for size in range(room_size)]

CLAIM_LIST = [format_claim(claim) for claim in open("input.txt", 'r')]

def main():
    room = init_room(1000)
    not_overlapped = set()

    for (_id, x, y, l, h) in CLAIM_LIST:
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
    main()
