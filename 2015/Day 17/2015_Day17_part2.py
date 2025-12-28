from itertools import combinations


def combos_that_fill(containers, target=150):
    result = []
    for r in range(1, len(containers) + 1):
        for combo in combinations(containers, r):
            if sum(combo) == target:
                result.append(combo)
    return result


if __name__ == "__main__":
    file_path = 'input.txt'
    container_sizes = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            container_sizes.append(int(line))
    combinations = combos_that_fill(container_sizes)
    combinations.sort(key=len)
    min_len = len(combinations[0])
    counter = 0
    for group in combinations:
        if len(group) == min_len:
            counter += 1
        else:
            break
    print(counter)