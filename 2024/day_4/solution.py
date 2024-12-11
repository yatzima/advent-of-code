import re
import numpy as np


def load_data():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
        data = [list(x) for x in data]
    return data


def write_data(solution1, solution2):
    with open('output.txt', 'w') as f:
        f.write(str(solution1))
        f.write('\n')
        f.write(str(solution2))


def count_xmas(data: str) -> int:
    count = re.findall(r'XMAS', data)
    count.extend(re.findall(r'SAMX', data))
    return len(count)


def check_horizontal(data) -> int:
    count = 0
    for d in data:
        line = ''.join(d)
        count += count_xmas(line)
    return count


def check_vertical(data) -> int:
    count = 0
    for d in np.rollaxis(data, 1):
        line = ''.join(d)
        count += count_xmas(line)
    return count


def check_diagonal(data) -> int:
    count = 0
    n = len(data)
    first_diagonal = [np.diagonal(data, offset=i) for i in range(-n, n)]
    second_diagonal = [np.diagonal(np.fliplr(data), offset=i) for i in range(-n, n)]

    for d in first_diagonal:
        line = ''.join(d)
        count += count_xmas(line)

    for d in second_diagonal:
        line = ''.join(d)
        count += count_xmas(line)

    return count
    

def solution1(data) -> int:
    count = 0
    count += check_horizontal(data)
    count += check_vertical(data)
    count += check_diagonal(data)
    return count


def check_mas(first_diag, second_diag) -> bool:
    first_diag = ''.join(first_diag)
    second_diagonal = ''.join(second_diag)
    if ('MAS' in first_diag or 'SAM' in first_diag) and ('MAS' in
            second_diagonal or 'SAM' in second_diagonal):
        return True
    return False


def solution2(data) -> int:
    count = 0
    shape = data.shape
    for i in range(shape[0]-2):
        for j in range(shape[1]-2):
            subset = data[i:i+3, j:j+3]
            first_diag = np.diagonal(subset)
            second_diag = np.diagonal(np.fliplr(subset))
            if check_mas(first_diag, second_diag):
                count += 1
    return count


def main():
    data = load_data()
    data = np.array(data)
    s1 = solution1(data)
    s2 = solution2(data)
    write_data(s1, s2)


if __name__ == '__main__':
    main()
