import math


def load_data(filename: str = 'input.txt') -> list:
    equations = []
    with open(filename, 'r') as f:
        data = f.read().splitlines()
        data = [d.split(': ') for d in data]
        for d in data:
            equations.append((int(d[0]), list(map(int, d[1].split(' ')))))
    return equations  
    

def write_data(solution1: int, solution2: int) -> None:
    with open('output.txt', 'w') as f:
        f.write(str(solution1))
        f.write('\n')
        f.write(str(solution2))


def solution1(val: int, nums: list[int]) -> bool:
    """ Recursive function to check if a value can be made from a list of
    numbers using either multiplication or subtraction. 
    """

    # Base case is length 1
    if len(nums) == 1:
        return val == nums[0]

    # Recursive case
    if val % nums[-1] == 0 and solution1(val // nums[-1], nums[:-1]):
        return True

    # Recursive case
    if val - nums[-1] >= 0 and solution1(val - nums[-1], nums[:-1]):
        return True

    return False


def solution2(target: int, nums: list[int]) -> bool:
    """ Recursive function to check if a value can be made from a list of
    numbers using either multiplication or subtraction. 
    """
    #print(val, nums)

    # Base case is length 1
    if len(nums) == 1:
        return target == nums[0]

    # Recursive case
    multiplication = [nums[0] * nums[1]]
    if multiplication[0] <= target and solution2(target, multiplication + nums[2:]):
        return True

    # Recursive case
    addition = [nums[0] + nums[1]]
    if addition[0] <= target and solution2(target, addition + nums[2:]):
        return True

    # Recursive case - concatenation 
    concat = [nums[0] * (10**(math.floor(math.log(nums[1], 10)) + 1)) + nums[1]]
    if concat[0] <= target and solution2(target, concat + nums[2:]):
        return True
    
    return False


def main():
    #equations = load_data('sample_input.txt')
    equations = load_data()

    total_1 = 0
    total_2 = 0
    for val, nums in equations:
        if solution1(val, nums):
            total_1 += val
        if solution2(val, nums):
            total_2 += val

    write_data(total_1, total_2)


if __name__ == '__main__':
    main()
