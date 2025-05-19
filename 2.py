import numpy as np
from math import pi

class FFT:
    def __init__(self, arr):
        self.arr = arr

    def non_recursive_fft(self):
        n = len(self.arr)
        if n & (n - 1) != 0:

            raise ValueError()



        levels = int(np.log2(n))

        i = 1

        while i < levels + 1:

            step = 2 ** i
            half = step // 2
            w_step = np.exp(-2j * pi / step)

            w = np.array([w_step ** k for k in range(half)])

            for k in range(0, n, step):
                even_part = self.arr[k:k + half]
                odd_part = self.arr[k + half:k + step]

                self.arr[k:k + step] = np.concatenate([
                    even_part + w * odd_part,
                    even_part - w * odd_part
                ])
            i += 1

        return self.arr

c = FFT(6)
print(c.non_recursive_fft())
