import itertools

def get_all_nodes(graph):
    nodes = set(graph.keys())
    for neighbors in graph.values():
        nodes.update(neighbors.keys())
    return list(nodes)

def get_shortest_path(graph, start_node):
    nodes = get_all_nodes(graph)
    nodes.remove(start_node)
    max_cost = -1
    for perm in itertools.permutations(nodes):
        path = [start_node] + list(perm)
        cost = 0
        valid = True

        for i in range(len(path) - 1):
            a, b = path[i], path[i + 1]
            if a in graph and b in graph[a]:
                cost += graph[a][b]
            else:
                valid = False
                break

        if valid and cost > max_cost:
            max_cost = cost
    return max_cost


if __name__ == "__main__":
    file_path = 'input.txt'
    graph, distances = {}, []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line_list = line.split()
            location1, location2, dist = line_list[0], line_list[2], int(line_list[-1])
            if location1 not in graph:
                graph[location1] = {}
            if location2 not in graph:
                graph[location2] = {}
            graph[location1][location2] = dist
            graph[location2][location1] = dist
    all_nodes = get_all_nodes(graph)
    for node in all_nodes:
        distance = get_shortest_path(graph, node)
        distances.append(distance)
    min_dist = max([i for i in distances if i != 99999])
    print(min_dist)












