import numpy as np
import sys

dic = {
    '1': [66, 32, 38, 37, 1],
    '2': [9, 16, 54, 2],
    '3': [8, 7, 61]
}

minSize = -sys.maxsize - 1
for key, arr in dic.items():
    arr[0] = np.random.randint(-100, -1)

print(dic)

