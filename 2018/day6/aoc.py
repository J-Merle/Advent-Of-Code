def parse_input(input_line):
    """ given an input "x,x" return a formatted input (x,x) where x are numbers """
    coords = input_line.strip().split(',')
    return (int(coords[0]), int(coords[1]))

     
def create_map(coord_list):
    max_x = max([x[0] for x in coord_list])
    max_y = max([y[1] for y in coord_list])
    _map = [[0 for y in range(max_y + 1)] for x in range(max_x + 1)]
    for x in range(len(_map)):
        for y in range(len(_map[x])):
            cardinal_distance_list = [cardinal_distance((x, y), coords) for coords in coord_list]
            if cardinal_distance_list.count(min(cardinal_distance_list)) > 1:
                _map[x][y] = -1
            else:
                _map[x][y] = cardinal_distance_list.index(min(cardinal_distance_list))
    return _map

def cardinal_distance(c1, c2):
    return abs(c1[0] - c2[0]) +  abs(c1[1] - c2[1])

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

def closest_region_size(_map, coord_list, max_distance):
    region_size = 0
    for x in range(len(_map)):
        for y in range(len(_map[x])):
            current_distance = 0
            for coord in coord_list:
                current_distance += cardinal_distance(coord, (x, y))
                if current_distance > max_distance:
                    break
            if current_distance < max_distance:
                region_size += 1
    return region_size

if __name__ == '__main__':
    coord_list = [parse_input(input_line) for input_line in open('input.txt')]
    _map = create_map(coord_list)
    print("Largest finished area = " + str(largest_area(_map, len(coord_list))))
    print("Closest region size = " + str(closest_region_size(_map, coord_list, 10000)))
