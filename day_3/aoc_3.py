def get_data():
    f = open("day_3\input.txt", "r")
    data = f.read().splitlines()
    
    return data


data = (get_data())


def power_cons():
    counter_0 = [0] * len(data[0])
    counter_1 = [0] * len(data[0])
    gamma_rate_bin = ""
    epsilon_rate_bin = ""

    for i in range(len(data)):
        for j, char in enumerate(data[i]):
            if char == "0":
                counter_0[j] += 1
            else:
                counter_1[j] += 1

    for k in range(len(counter_0)):
        if counter_0[k] > counter_1[k]:
            gamma_rate_bin += "0"
            epsilon_rate_bin += "1"
        else:
            gamma_rate_bin += "1"
            epsilon_rate_bin += "0"

    gamma_rate = int(gamma_rate_bin, 2)
    epsilon_rate = int(epsilon_rate_bin, 2)
    power = gamma_rate * epsilon_rate

    return power


print(power_cons())



    