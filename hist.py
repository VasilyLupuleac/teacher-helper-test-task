import cv2
import sys
import numpy as np


def print_color_hist(src):
    img = cv2.imread(src).reshape(-1, 3)
    colors, freqs = np.unique(ar=img, axis=0, return_counts=True)
    sorted_inds = np.flip(np.argsort(freqs))

    colors, freqs = colors[sorted_inds], freqs[sorted_inds]

    for r, g, b, freq in np.concatenate((colors, freqs.reshape(-1, 1)), axis=1):
        print('{}, {}, {}: {}'.format(r, g, b, freq))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: python hist.py <input-image>')
        exit(0)
    
    print_color_hist(sys.argv[1])
