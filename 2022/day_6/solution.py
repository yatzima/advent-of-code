def load_data():
    with open('input.txt', 'r') as f:
        data = f.read()
    return data
    

def write_data(solution1, solution2):
    with open('output.txt', 'w') as f:
        f.write(solution1)
        f.write('\n')
        f.write(solution2)


def main():
    data = load_data()
    
    solution1 = 0
    solution2 = 0
    
    for i in range(len(data)-3):
        code = data[i:i+4]
        if len(set(code)) >= 4:
            solution1 = i+4
            break
        
    for i in range(len(data)-13):
        code = data[i:i+14]
        if len(set(code)) >= 14:
            solution2 = i+14
            break
   
    solution1 = str(solution1)
    solution2 = str(solution2)
    write_data(solution1, solution2)


if __name__ == '__main__':
    main()
