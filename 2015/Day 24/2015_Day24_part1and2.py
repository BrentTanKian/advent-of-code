from itertools import combinations
import math

def find_combinations(nums, target):
    result = []
    for r in range(1, len(nums) + 1):
        for comb in combinations(nums, r):
            if sum(comb) == target:
                result.append(comb)
    return result

if __name__ == "__main__":
    with open('input.txt') as f:
        lines_list = f.readlines()
    cleaned_list = [int(i.strip()) for i in lines_list]
    total = sum(cleaned_list)
    # Divide total by 4 instead of 3 for part 2's solution
    individual_group_sum = total // 3
    combinations = find_combinations(cleaned_list, individual_group_sum)
    combinations.sort(key=len)
    base_length = len(combinations[0])
    subset = [i for i in combinations if len(i) == base_length]
    entanglements = [math.prod(i) for i in subset]
    print(min(entanglements))