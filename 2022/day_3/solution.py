import string

def load_data():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    return data
    

def write_data(solution1, solution2):
    with open('output.txt', 'w') as f:
        f.write(solution1)
        f.write('\n')
        f.write(solution2)


def main():
    data = load_data()
    
    items = string.ascii_lowercase + string.ascii_uppercase
    priority_map = {item:i+1 for i, item in enumerate(items)}
    
    total_a = []
    for example in data:
        split = int(len(example)/2)
        first_comp = example[:split]
        second_comp = example[split:]
    
        a = [priority_map[elm] for elm in set(first_comp)]
        b = [priority_map[elm] for elm in set(second_comp)]

        a = set(a)
        b = set(b)

        total_a.append(list(a.intersection(b))[0])
    solution_1 = str(sum(total_a))
    
    total_b = []
    for i in range(0, len(data), 3):
        example = data[i:i+3]

        a = [priority_map[elm] for elm in set(example[0])]
        b = [priority_map[elm] for elm in set(example[1])]
        c = [priority_map[elm] for elm in set(example[2])]

        a = set(a)
        b = set(b)
        c = set(c)

        total_b.append(list(a.intersection(b).intersection(c))[0])

    solution_2 = str(sum(total_b))
    
    write_data(solution_1, solution_2)
                            
    
if __name__ == '__main__':
    main()
