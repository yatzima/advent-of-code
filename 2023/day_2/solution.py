def load_data():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    return data
    

def write_data(solution1, solution2):
    with open('output.txt', 'w') as f:
        f.write(str(solution1))
        f.write('\n')
        f.write(str(solution2))


def main():
    data = load_data()
    solution1 = 0
    max_cubes = {'red': 12,
                 'green': 13,
                 'blue': 14}
    for game in data:
        game_id = game.split()[1].strip(':')
        outcomes = zip(game.split()[2::2], game.split()[3::2])
    
        for outcome in outcomes:
            amt = int(outcome[0])
            color = outcome[1].strip(',').strip(';')
            if amt > max_cubes[color]:
                break
        else:
            solution1 += int(game_id)
            
    solution2 = 0
    for game in data:
        max_cubes = {'red': 0,
                     'green': 0,
                     'blue': 0}
        outcomes = zip(game.split()[2::2], game.split()[3::2])
    
        for outcome in outcomes:
            amt = int(outcome[0])
            color = outcome[1].strip(',').strip(';')
            if amt > max_cubes[color]:
                max_cubes[color] = amt

        prod_of_amt = 1
        for k, v in max_cubes.items():
            prod_of_amt *= int(v)
        solution2 += int(prod_of_amt)

    write_data(solution1, solution2)


if __name__ == '__main__':
    main()
