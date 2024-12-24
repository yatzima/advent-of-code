import collections

from typing import Tuple


def load_data(filename: str = 'input.txt'):
    with open(filename, 'r') as f:
        data = f.read().split('\n\n')
        page_ordering_rules = data[0].splitlines()
        page_numbers_updates = data[1].splitlines()
    return page_ordering_rules, page_numbers_updates
    

def write_data(solution1, solution2):
    with open('output.txt', 'w') as f:
        f.write(str(solution1))
        f.write('\n')
        f.write(str(solution2))


def create_rules(page_ordering_rules: list) -> dict:
    rules_dict = collections.defaultdict(list)
    for rule in page_ordering_rules:
        key, value = rule.split('|')
        rules_dict[key].append(value)
    return rules_dict 


def get_relevant_updates(page_numbers_updates: list, rules_dict: dict) -> Tuple[list, list]:
    ordered_updates = []
    unordered_updates = []
    for update in page_numbers_updates:
        update = update.split(',')
        for i, elm in enumerate(update):
            if i == len(update)-1:
                ordered_updates.append(update)
                break
            elif update[i+1] not in rules_dict[elm]:
                unordered_updates.append(update)
                break
    return ordered_updates, unordered_updates


def solution1(updates: list) -> int:
    middle_value = []
    for update in updates:
        middle_value.append(int(update[int(len(update)/2)]))
    return sum(middle_value)


def sort_updates(unordered_updates: list, rules_dict: dict) -> list:
    ordered_updates = []
    for update in unordered_updates:
        #print(update)
        indeg = collections.Counter()
        for u in update:
            indeg[u] = 0
            for v in rules_dict[u]:
                if v in update:
                    indeg[u] += 1

        ordered_update = [deg[0] for deg in indeg.most_common()[::-1]]
        #print(ordered_update)
        ordered_updates.append(ordered_update)
    return ordered_updates


def solution2(unordered_updates: list, rules_dict: dict) -> int:
    ordered_updates = sort_updates(unordered_updates, rules_dict)
    middle_value = []
    for update in ordered_updates:
        middle_value.append(int(update[int(len(update)/2)]))
    return sum(middle_value)


def main(): 
    page_ordering_rules, page_numbers_updates = load_data()
    #page_ordering_rules, page_numbers_updates = load_data('sample_input.txt')
    rules_dict = create_rules(page_ordering_rules)
    ordered_updates, unordered_updates = get_relevant_updates(page_numbers_updates, rules_dict)
    s1 = solution1(ordered_updates)
    s2 = solution2(unordered_updates, rules_dict)
    write_data(s1, s2)


if __name__ == '__main__':
    main()
