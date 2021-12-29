def get_data():
    f = open("AOC\day_2\input.txt", "r")
    data = f.read().splitlines()
    
    return data


data = (get_data())


def position():
    depth = 0
    horizontal = 0

    for i in range(len(data)):
        direction, amount = data[i].split()

        if direction == "forward":
            horizontal += int(amount)
        elif direction == "up":
            depth -= int(amount)
        elif direction == "down":
            depth += int(amount)
          
    return horizontal * depth


def position_2():
    depth = 0
    horizontal = 0
    aim = 0

    for i in range(len(data)):
        direction, amount = data[i].split()
        
        if direction == "forward":
            horizontal += int(amount)
            depth += int(amount) * aim
        elif direction == "up":
            aim -= int(amount)
        else:
            aim += int(amount)
          
    return horizontal * depth

print(position())
print(position_2())

