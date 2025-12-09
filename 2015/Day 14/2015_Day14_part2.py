def calculate_distances(speed, duration, rest):
    start_time, distances = 0, [0]
    cycle_len, cur_cycle = duration + rest, 1
    cycle_stop = cur_cycle * cycle_len
    prev_travel_time = ((cur_cycle - 1) * cycle_len) + duration
    while start_time < 2503:
        if start_time < prev_travel_time:
            distances.append(distances[-1] + speed)
        elif prev_travel_time <= start_time < cycle_stop:
            distances.append(distances[-1])
        else:
            cur_cycle += 1
            cycle_stop = cur_cycle * cycle_len
            prev_travel_time = ((cur_cycle - 1) * cycle_len) + duration
            distances.append(distances[-1] + speed)
        start_time += 1
    return distances


if __name__ == "__main__":
    file_path = 'input.txt'
    storage = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line_list = line.split()
            speed, duration, rest = int(line_list[3]), int(line_list[6]), int(line_list[-2])
            distances = calculate_distances(speed, duration, rest)
            storage.append(distances)
    reindeer_dict = {}
    for i in range(len(storage)):
        reindeer_dict[i] = 0
    for i in range(1, len(storage[0])):
        cur_second = []
        for n in range(len(storage)):
            cur_second.append(storage[n][i])
        cur_max_dist = max(cur_second)
        for j in range(len(cur_second)):
            if cur_second[j] == cur_max_dist:
                reindeer_dict[j] += 1
    print(max([reindeer_dict[i] for i in reindeer_dict]))
