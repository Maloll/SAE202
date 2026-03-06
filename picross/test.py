import numpy as np
N = 5

binary_lists = np.unpackbits(np.expand_dims(np.arange(2 ** N, dtype=np.uint8), -1), axis=1, bitorder='little', count=N)

print(binary_lists)
print(len(binary_lists))