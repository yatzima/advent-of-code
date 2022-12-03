def load_data():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    data = [[d[0], d[-1]]  for d in data]
    return data
    

def write_data(solution1, solution2):
    with open('output.txt', 'w') as f:
        f.write(solution1)
        f.write('\n')
        f.write(solution2)


def determine_outcome(data, val_map):
    opp = val_map[data[0]]
    me = val_map[data[1]]
    outcome = (opp-me)%3
    return outcome


def reverse_outcome(data, val_map, outcome_map):
    opp = val_map[data[0]]
    outcome = outcome_map[data[1]]
    mes = [0, 1, 2]
    for me in mes:
        if outcome == (opp-me)%3:
            return me

        
def main():
    data = load_data()
    val_map = {'A':0, 'B':1, 'C':2, 'X':0, 'Y':1, 'Z':2}
    points_outcome = {0:3, 1:0, 2:6}
    points_play = {'X':1, 'Y':2, 'Z':3}
    
    outcome = [determine_outcome(d, val_map) for d in data]
    points1 = [points_outcome[o] for o in outcome]  
    points2 = [points_play[d[1]] for d in data]
    
    total_points = [elm[0]+elm[1] for elm in zip(points1, points2)]
    solution1 = str(sum(total_points))
    
    outcome_map = {'X':1, 'Y':0, 'Z':2}
    outcome_map_val = {'X':0, 'Y':3, 'Z':6}
    
    play = [reverse_outcome(d, val_map, outcome_map) for d in data]
    
    points1 = [p+1 for p in play]
    points2 = [points_outcome[outcome_map[d[1]]] for d in data]
    
    total_points = [x+y for x, y in zip(points1, points2)]
    solution2 = str(sum(total_points))
    
    write_data(solution1, solution2)


if __name__ == '__main__':
    main()