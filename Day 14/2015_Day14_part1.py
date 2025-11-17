if __name__ == "__main__":
    file_path = 'input.txt'
    storage = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            travel_time, distance = 2503, 0
            line_list = line.split()
            speed, duration, rest = int(line_list[3]), int(line_list[6]), int(line_list[-2])
            while travel_time > 0:
                dist_traveled = speed * duration
                travel_time = travel_time - duration - rest
                distance += dist_traveled
            excess_time = travel_time * -1
            if excess_time > rest:
                distance = distance - ((excess_time - rest) * speed)
            storage.append(distance)
    print(max(storage))