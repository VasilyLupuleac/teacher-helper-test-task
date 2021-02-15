import cv2
import sys


def transpose_image(src, dest):
    image = cv2.imread(src)
    transp_image = cv2.transpose(image)
    cv2.imwrite(filename=dest, img=transp_image)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('usage: python transpose.py <input-image> <output-image>')
        exit(0)
        
    transpose_image(*sys.argv[1:3])