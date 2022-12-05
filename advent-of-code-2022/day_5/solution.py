def load_data():
    with open('input.txt', 'r') as f:
        data = f.read().split('\n\n')
    return data
    

def write_data(solution1, solution2):
    with open('output.txt', 'w') as f:
        f.write(solution1)
        f.write('\n')
        f.write(solution2)


def main():
    data = load_data()
    state = data[0].splitlines()
    moves = data[1].splitlines()
    
    state.reverse()
    
    nbr_stacks = [elm for elm in state[0].split(' ') if elm != '']
    
    width = 3
    spaces = len(nbr_stacks) - 1

    stacks1 = {stack:[] for stack in nbr_stacks}
    stacks2 = {stack:[] for stack in nbr_stacks}
    
    new_lst = [list(t)[1::4] for t in state[1:]]

    for i in new_lst:
        for nbr, j in enumerate(stacks1):
            if i[nbr] != ' ':
                stacks1[j].append(i[nbr])
                stacks2[j].append(i[nbr])
    
    moves = [move.split() for move in moves]
    
    new_moves = []
    for move in moves: 
        temp = [b for b in move if b.isdigit()]
        new_moves.append(temp)
        
    for m in new_moves:
        nbr_pops = int(m[0])
        s1 = m[1]
        s2 = m[2]
        temp = []
        for i in range(nbr_pops):
            temp.extend(stacks1[s1].pop())
        stacks1[s2].extend(temp)
    
    for m in new_moves:
        nbr_pops = int(m[0])
        s1 = m[1]
        s2 = m[2]
        temp = []
        for i in range(nbr_pops):
            temp.extend(stacks2[s1].pop())
        temp.reverse()
        stacks2[s2].extend(temp)
    
    solution1 = ''.join([stacks1[stack][-1] for stack in stacks1])
    solution2 = ''.join([stacks2[stack][-1] for stack in stacks2])
    write_data(solution1, solution2)


if __name__ == '__main__':
    main()
