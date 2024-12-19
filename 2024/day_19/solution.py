def load_data(filename='input.txt'):
    with open(filename, 'r') as f:
        data = f.read().split('\n\n')

    towels = data[0]
    towels = towels.split(', ')
    towels = set(towels)

    design = data[1]
    design = design.splitlines()
    return towels, design


def write_data(solution1, solution2):
    with open('output.txt', 'w') as f:
        f.write(str(solution1))
        f.write('\n')
        f.write(str(solution2))


def solve(towels, design):
    min_w, max_w = min(map(len, towels)), max(map(len, towels))
    solved = {}
    solved[0] = 1
    for l in range(len(design) + 1):
        for sl in range(max(0, l - max_w), max(0, l - min_w) + 1):
            if sl in solved and design[sl:l] in towels:
                if l not in solved:
                    solved[l] = 0
                solved[l] += solved[sl]
    return solved.get(len(design), 0)


def main():
    #towels, design = load_data('sample_input.txt')
    towels, design = load_data()
    s1 = sum(solve(towels, d) > 0 for d in design)
    s2 = sum(solve(towels, d) for d in design)
    print(s1)
    print(s2)
    write_data(s1, s2)
            

if __name__ == '__main__':
    main()
