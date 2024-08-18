import random
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

def PlayGame():
    turns = 0
    square = 1

    while square != 100:
        NewSquare = square + random.randint(1, 6)

        if not (NewSquare > 100):
            #snakes
            if NewSquare == 26:
                NewSquare = 10
            if NewSquare == 39:
                NewSquare = 5
            elif NewSquare == 51:
                NewSquare = 6
            elif NewSquare == 54:
                NewSquare = 36
            elif NewSquare == 56:
                NewSquare = 1
            elif NewSquare == 60:
                NewSquare = 23
            elif NewSquare == 75:
                NewSquare = 28
            elif NewSquare == 83:
                NewSquare = 45
            elif NewSquare == 85:
                NewSquare = 59
            elif NewSquare == 90:
                NewSquare = 48
            elif NewSquare == 92:
                NewSquare = 25
            elif NewSquare == 97:
                NewSquare = 87
            elif NewSquare == 99:
                NewSquare = 63

            #ladders
            elif NewSquare == 3:
                NewSquare = 20
            elif NewSquare == 11:
                NewSquare = 28
            elif NewSquare == 15:
                NewSquare = 34
            elif NewSquare == 17:
                NewSquare = 74
            elif NewSquare == 22:
                NewSquare = 37
            elif NewSquare == 38:
                NewSquare = 59
            elif NewSquare == 49:
                NewSquare = 67
            elif NewSquare == 52:
                NewSquare = 71
            elif NewSquare == 57:
                NewSquare = 76
            elif NewSquare == 61:
                NewSquare = 78
            elif NewSquare == 73:
                NewSquare = 86
            elif NewSquare == 81:
                NewSquare = 98
            elif NewSquare == 88:
                NewSquare = 91

            square = NewSquare
        turns += 1
    return turns

data = []
keys = []
count = []

for i in range(1000000):
    outcome = PlayGame()
    if outcome in keys:
        for j in range(len(data)):
            if data[j][0] == outcome:
                data[j][1] += 1
                count[j] += 1
    else:
        keys.append(outcome)
        data.append([outcome, 1])
        count.append(1)

ExpectedValue = 0
for i in range(len(count)):
    count[i] = count[i] / 1000000
    ExpectedValue += count[i] * keys[i]

print("Expected turns is", ExpectedValue)

ax.bar(keys, count)
ax.set_xlabel('Number of Turns')
ax.set_ylabel('Probability')
ax.set_title('Probability Distribution of Rolls to Complete Snakes and Ladders')
plt.show()
