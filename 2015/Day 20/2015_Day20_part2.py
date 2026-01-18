if __name__ == "__main__":
    houses = 3400000
    house_array = [0 for i in range(houses)]
    for elf in range(1, houses + 1):
        multiplier = 1
        while (elf * multiplier) - 1 < houses and multiplier <= 50:
            house_array[(elf * multiplier) - 1] += (elf * 11)
            multiplier += 1
    for i in range(len(house_array)):
        if house_array[i] >= 34000000:
            print(i + 1)
            break