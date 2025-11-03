import json

def recursive_sum(data):
    if isinstance(data, (int, float)):
        return data
    
    if isinstance(data, list):
        total = 0
        for item in data:
            total += recursive_sum(item) 
        return total
    
    if isinstance(data, dict):
        if contains_red(data):
            return 0       
        total = 0
        for key, value in data.items():
            total += recursive_sum(value) 
        return total
    
    return 0


def contains_red(data):
    if isinstance(data, dict):
        return any(value == "red" for value in data.values())
    return False

if __name__ == "__main__":
    file_path = 'input.txt'
    with open(file_path, 'r') as file:
        lines = file.readlines()
        line_ele, i = lines[0], 0
    array = json.loads(line_ele)
    total_sum = recursive_sum(array)
    print(total_sum)