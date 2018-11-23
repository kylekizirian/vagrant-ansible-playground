import numpy as np


if __name__ == '__main__':

    num_draws = 10**6
    max_rand_draw = 0

    for _ in range(num_draws):
        rand_draw = np.random.normal(0, 1)
        if abs(rand_draw) > max_rand_draw:
            max_rand_draw = abs(rand_draw)

    print(max_rand_draw)
