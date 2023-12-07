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
    elf_cals = []
    sum_cal = 0
    max_cal = 0

    for elm in data:
        if elm == '':
            elf_cals.append(sum_cal)
            if sum_cal > max_cal:
                max_cal = sum_cal
            sum_cal = 0
        else:
            sum_cal += int(elm)
    
    elf_cals.sort()
    
    solution_1 = str(max_cal)
    solution_2 = str(sum(elf_cals[-3:]))
    write_data(solution_1, solution_2)

    
if __name__ == "__main__":
    main()
