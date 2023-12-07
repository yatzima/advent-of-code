def load_data():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    data = [d.split(',') for d in data]
    return data
    

def write_data(solution1, solution2):
    with open('output.txt', 'w') as f:
        f.write(solution1)
        f.write('\n')
        f.write(solution2)


def main():
    data = load_data()
    cnt_a = 0
    cnt_b = 0
    for d in data:
        a_split = d[0].split('-')
        b_split = d[1].split('-')
        a = set(list(range(int(a_split[0]), int(a_split[1])+1)))
        b = set(list(range(int(b_split[0]), int(b_split[1])+1)))
        intersect = a.intersection(b)
        if len(intersect) == len(a) or len(intersect) == len(b):
            cnt_a += 1
        if len(intersect) > 0:
            cnt_b += 1
    solution1 = str(cnt_a)
    solution2 = str(cnt_b)
    write_data(solution1, solution2)

    
if __name__ == '__main__':
    main()
