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
    write_data(solution1, solution2)


if __name__ == '__main__':
    main()
