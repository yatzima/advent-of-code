import re


def load_data():
    with open('input.txt', 'r') as f:
        data = f.read()
    return data
    

def write_data(solution1, solution2):
    with open('output.txt', 'w') as f:
        f.write(str(solution1))
        f.write('\n')
        f.write(str(solution2))


def solution1(data):
    all_mul = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)
    mul_list = [mul.strip('mul(').strip(')').split(',') for mul in all_mul]
    mul_list = [int(mul[0]) * int(mul[1]) for mul in mul_list]
    solution1 = sum(mul_list)
    return solution1


def solution2(data):
    all_mul = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)", data)
    keep_mul = []
    bool_flag = True

    for mul in all_mul:
        if mul == 'do()':
            bool_flag = True
            continue
        if mul == 'don\'t()':
            bool_flag = False   
            continue
        if bool_flag:
            keep_mul.append(mul)

    mul_list = [mul.strip('mul(').strip(')').split(',') for mul in keep_mul]
    mul_list = [int(mul[0]) * int(mul[1]) for mul in mul_list]
    solution2 = sum(mul_list)
    return solution2


def main():
    data = load_data()
    solution1 = solution1(data)
    solution2 = solution2(data)
    write_data(solution1, solution2)


if __name__ == '__main__':
    main()
