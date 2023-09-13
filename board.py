
import numpy as np

class Pole:
    def __init__(self, stan):
        self.stan = "[]"

    def mina(self):
        self.stan = "*"

    def cyfra(self, x):
        self.stan = x

    def __str__(self):
        return str(self.stan)

print("")
# size = int(input("give size of board (minimum 10): "))
size = 10


# list = np.full((size, size), Pole(1))
# print(list)

list = np.empty((size, size), dtype=object)
for i in range(size):
    for j in range(size):
        list[i][j] = Pole(1)
xd = Pole(1)

list[1][1].cyfra(5)

for row in list:
    for pole in row:
        print(pole, end=" ")
    print()
