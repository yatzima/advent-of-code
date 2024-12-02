def load_data():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
        #data = [d.split() for d in data]
    return data
    

def write_data(solution1, solution2):
    with open('output.txt', 'w') as f:
        f.write(str(solution1))
        f.write('\n')
        f.write(str(solution2))


def is_safe_1(report):
    d = report.split()
    direction = None
    for i, j in zip(d[:-1], d[1:]):
        i = int(i)
        j = int(j)
        if direction is None:
            if i > j: 
                direction = 1
            elif i < j:
                direction = -1
            else:
                return False
        if (direction == 1 and i > j) or (direction == -1 and i < j): 
            if abs(i - j) > 3 or abs(i - j) < 1: 
                return False
        else:
            return False
    return True


def remove_element_from_list(l, idx):
    l = l.split()
    l_temp = l.copy()
    del l_temp[idx]
    print('New list')
    print(' '.join(l_temp)) 
    return ' '.join(l_temp)


def is_safe_2(report):
    print('Report')
    print(report)
    d = report.split()
    d = [int(i) for i in d]
    direction = None
    for idx, (i, j) in enumerate(zip(d[:-1], d[1:])):
        if direction is None:
            if i > j: 
                direction = 1
            elif i < j:
                direction = -1
            else:
                bool_flag = is_safe_1(remove_element_from_list(report, idx)) or is_safe_1(remove_element_from_list(report, idx+1))
                return bool_flag

        if (direction == 1 and i > j) or (direction == -1 and i < j): 
            if abs(i - j) > 3 or abs(i - j) < 1: 
                bool_flag = is_safe_1(remove_element_from_list(report, idx)) or is_safe_1(remove_element_from_list(report, idx+1))
                return bool_flag
        else: 
            bool_flag = is_safe_1(remove_element_from_list(report, idx)) or is_safe_1(remove_element_from_list(report, idx+1))
            return bool_flag
    return True


#def is_safe_2(report):
#    print('Report')
#    print(report)
#    if is_safe_1(report):
#        return True
#    else:
#        d = report.split()
#        d = [int(i) for i in d]
#        for i in range(len(d)):
#            temp = d.copy()
#            del temp[i]
#            print('New list')
#            print(' '.join([str(i) for i in temp]))
#            if is_safe_1(' '.join([str(i) for i in temp])):
#                return True
#    return False


def main():
    data = load_data()
    nbr_of_safe_1 = 0
    nbr_of_safe_2 = 0
    for d in data:
        if is_safe_1(d):
            nbr_of_safe_1 += 1
        if is_safe_2(d):
            nbr_of_safe_2 += 1
        print(nbr_of_safe_1, nbr_of_safe_2)
        print('-------------------\n')
    print(nbr_of_safe_1, nbr_of_safe_2)


    #write_data(solution1, solution2)


if __name__ == '__main__':
    main()
