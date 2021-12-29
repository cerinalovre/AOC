def get_data():
    f = open("AOC\day_1\input.txt", "r")
    data = f.read().splitlines()
    
    return data


data = (get_data())


def depth_increase():
    inc = 0

    for i in range(len(data) - 1):
        if data[i] < data[i + 1]:
            inc += 1
    
    return inc


def three_window():
    a = 0
    b = 3
    sum1 = 0
    sum2 = 0
    inc = 0

    while b < len(data):

        for i in range(a, b):
            sum1 += int(data[i])
        for i in range(a + 1, b + 1):
            sum2 += int(data[i])
        if sum2 > sum1:
            inc += 1
        
        a += 1
        b += 1
        sum1 = 0
        sum2 = 0

    return inc


print(depth_increase())
print(three_window())


    
        


