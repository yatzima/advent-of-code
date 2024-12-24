def load_data(filename: str = 'input.txt') -> list:
    with open(filename, 'r') as f:
        data = f.read().splitlines()
    return data
    

def write_data(solution1: int, solution2: int) -> None:
    with open('output.txt', 'w') as f:
        f.write(str(solution1))
        f.write('\n')
        f.write(str(solution2))


def main():
    data = load_data()
    #write_data(s1, s2)


if __name__ == '__main__':
    main()
