def main():
    with open('data.txt', 'r') as f:
        data = f.read().splitlines()
        
    elf_cals = []
    cal = 0
    max_cal = 0

    for elm in data:
        if elm == '':
            elf_cals.append(cal)
            if cal > max_cal:
                max_cal = cal
            cal = 0
        else:
            cal += int(elm)
    
    elf_cals.sort()
    
    solution_a = str(max_cal)
    solution_b = str(sum(elf_cals[-3:]))
    print('The total calories of the elf who carries the most is: ' + solution_a + 'calories')
    print('The total calories carried by the top three elfs is: ' + solution_b + 'calories')

    
if __name__ == "__main__":
    main()