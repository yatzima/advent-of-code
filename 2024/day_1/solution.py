def load_data():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
        data = [d.split() for d in data]
    return data
    

def write_data(solution1, solution2):
    with open('output.txt', 'w') as f:
        f.write(str(solution1))
        f.write('\n')
        f.write(str(solution2))


def main():
    data = load_data()
    l1 = [int(d[0]) for d in data]
    l2 = [int(d[1]) for d in data]

    l1.sort()
    l2.sort()
    solution1 = [abs(elm1 - elm2) for elm1, elm2 in zip(l1, l2)]
    solution1 = sum(solution1)

    mult_dict = {}

    for elm in l2:
        mult_dict[elm] = mult_dict.get(elm, 0) + 1

    solution2 = []
    for elm in l1:
        if elm in mult_dict:
            solution2.append(elm * mult_dict.get(elm))
    solution2 = sum(solution2)

    write_data(solution1, solution2)


if __name__ == '__main__':
    main()
