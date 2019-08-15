#
#
#
#

import cv2 as cv
import sys

def main(argv):
  if len(argv) != 5:
    print("usage: python3 ./" + argv[0] + " <im1> <im2> <out> <factor>")
    return 0

  im1 = cv.imread(sys.argv[1])
  im2 = cv.imread(sys.argv[2])

  im1 = cv.resize(im1, (0,0), fx=0.25, fy=0.25, interpolation=cv.INTER_NEAREST)
  im1 = cv.resize(im1, (0,0), fx=4.00, fy=4.00, interpolation=cv.INTER_NEAREST)
  im1 = im1.astype("float64")
  im2 = cv.Laplacian(im2, cv.CV_64F)
  cv.imwrite(argv[3], im1+im2/float(argv[4]))

if __name__ == "__main__":
  main(sys.argv)
