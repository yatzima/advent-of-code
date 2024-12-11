import numpy as np

from collections import defaultdict


def load_data(filename='input.txt'):
    with open(filename, 'r') as f:
        data = f.read().splitlines()
    return data


def write_data(solution1, solution2):
    with open('output.txt', 'w') as f:
        f.write(str(solution1))
        f.write('\n')
        f.write(str(solution2))


def pad(data):
    padded_data = ['.' + line + '.' for line in data]
    dots = ''.join(['.' for _ in range(len(data)+2)])
    padded_data.insert(0, dots)
    padded_data.append(dots)
    return padded_data 


def create_adjacency_list(padded_data):
    adjacency_list = defaultdict(list)
    for row_idx, line in enumerate(padded_data):
        if row_idx == 0 or row_idx == len(padded_data) - 1:
            continue
        for col_idx, height in enumerate(line):
            if height == '.':
                continue
            successor = []
            predecessor = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    neighboor = padded_data[row_idx+i][col_idx+j]
                    if (i == 0 and j == 0) or neighboor == '.':
                        continue
                    # Diagonal elements are not considered as neighbors
                    elif (i == -1 and j == -1) or (i == 1 and j == 1) or (i == -1 and j == 1) or (i == 1 and j == -1):
                        continue
                    if int(neighboor) == int(height)+1:
                        successor.append((row_idx+i, col_idx+j))
                    if int(neighboor) == int(height)-1:
                        predecessor.append((row_idx+i, col_idx+j))
                
            key = (row_idx, col_idx)
            value = {'height': height, 
                    'successor': successor, 
                    'predecessor': predecessor}

            adjacency_list[key] = value
    return adjacency_list


def solution1(adjacency_list: dict) -> int:
    score_of_trailheads = []
    for key, value in adjacency_list.items():
        if value['height'] == '0':
            reachable_nine_heights = []
            keys_of_successors = []
            keys_of_successors.extend(adjacency_list[key]['successor'])
            while keys_of_successors:
                key = keys_of_successors.pop()

                if adjacency_list[key]['successor']:
                    keys_of_successors.extend(adjacency_list[key]['successor'])
                elif adjacency_list[key]['height'] == '9':
                    reachable_nine_heights.append(key)

                if not keys_of_successors:
                    score_of_trailheads.append(len(set(reachable_nine_heights)))
                    break

    return sum(score_of_trailheads)

       
def solution2(adjacency_list: dict) -> int:
    ratings_of_trailheads = []
    for key, value in adjacency_list.items():
        if value['height'] == '0':
            reachable_nine_heights = []
            keys_of_successors = []
            keys_of_successors.extend(adjacency_list[key]['successor'])
            while keys_of_successors:
                key = keys_of_successors.pop()

                if adjacency_list[key]['successor']:
                    keys_of_successors.extend(adjacency_list[key]['successor'])
                elif adjacency_list[key]['height'] == '9':
                    reachable_nine_heights.append(key)

                if not keys_of_successors:
                    ratings_of_trailheads.append(len(reachable_nine_heights))
                    break

    return sum(ratings_of_trailheads)


def main():
    #topographic_map = load_data('sample_input.txt')
    topographic_map = load_data()
    padded_data =  pad(topographic_map)
    adjacency_list = create_adjacency_list(padded_data)
    s1 = solution1(adjacency_list)
    s2 = solution2(adjacency_list)
    write_data(s1, s2)


if __name__ == '__main__':
    main()
