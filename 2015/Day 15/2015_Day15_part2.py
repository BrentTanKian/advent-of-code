if __name__ == "__main__":
    file_path = 'input.txt'
    max_teaspoons = 100
    dict_storage = {}
    storage, index = [], 0
    totals = []
    for a in range(max_teaspoons + 1):
        for b in range(max_teaspoons + 1 - a):
            for c in range(max_teaspoons + 1 - a - b):
                d = max_teaspoons - a - b - c
                storage.append((a, b, c, d))
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line_list = line.split()
            stat_list = [int(line_list[2][:-1]), int(line_list[4][:-1]), int(line_list[6][:-1]), int(line_list[8][:-1]), int(line_list[10])]
            dict_storage[index] = stat_list
            index += 1
    for group in storage:
        capacity, durability, flavor, texture, calories = 0, 0, 0, 0, 0
        for i in range(len(group)):
            specs = dict_storage[i]
            quantity = group[i]
            capacity += specs[0] * quantity
            durability += specs[1] * quantity
            flavor += specs[2] * quantity
            texture += specs[3] * quantity
            calories += specs[4] * quantity
        if calories == 500:
            capacity = max(0, capacity)
            durability = max(0, durability)
            flavor = max(0, flavor)
            texture = max(0, texture)
            total = capacity * durability * flavor * texture
            totals.append(total)
    print(max(totals))