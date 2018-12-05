import string

pattern_set = {a+a.upper() for a in string.ascii_lowercase}
pattern_set.update({a.upper()+a for a in string.ascii_lowercase})

def find_length(string):
    polymere = string    
    previous_len = -1
    s = set()
    while len(polymere) != previous_len:
        previous_len = len(polymere)
        for pattern in pattern_set:
            polymere = polymere.replace(pattern, '')
 
    return len(polymere)

def part_two(polymere):
    _min = 1000000000
    for letter in string.ascii_lowercase:
        shorten_polymere = polymere.replace(letter, '').replace(letter.upper(), '')
        _len = find_length(shorten_polymere)
        if _len < _min:
            _min = _len

    print(_min)



if __name__ == '__main__':
    polymere = open('input.txt', 'r').read().strip()
    print(find_length(polymere))
    part_two(polymere)
    
