"""
Day 6 of the adevent of code 2018
"""

def parse_input(input_line):
    """ given an input "x,x" return a formatted input (x,x) where x are numbers """
    coords = input_line.strip().split(',')
    return (int(coords[0]), int(coords[1]))

def create_map(coord_list):
    max_x = max([x[0] for x in coord_list])
    max_y = max([y[1] for y in coord_list])
    _map = [[0 for y in range(max_y + 1)] for x in range(max_x + 1)]
    closest_region_size = 0
    for x in range(len(_map)):
        for y in range(len(_map[x])):
            cardinal_distance_list = [abs(x-coords[0]) + abs(y-coords[1]) for coords in coord_list]

            closest = min(cardinal_distance_list)
            if cardinal_distance_list.count(closest) > 1:
                _map[x][y] = -1
            else:
                _map[x][y] = cardinal_distance_list.index(closest)

            # PART TWO
            current_distance = sum(cardinal_distance_list)
            if current_distance < 10000:
                closest_region_size += 1

    print("Largest finished area = " + str(largest_area(_map, len(coord_list))))
    print("Closest region size :" + str(closest_region_size))

def largest_area(_map, number_of_init_points):
    banned_set = set()
    for item in _map[0]:
        banned_set.add(item)
    for item in _map[len(_map) - 1]:
        banned_set.add(item)
    for item in _map:
        banned_set.add(item[0])
        banned_set.add(item[len(item) - 1])
    return max([sum(x.count(i) for x in _map) for i in {x for x in range(number_of_init_points)} - banned_set])


if __name__ == '__main__':
    COORD_LIST = [parse_input(input_line) for input_line in open('input.txt')]
    create_map(COORD_LIST)
