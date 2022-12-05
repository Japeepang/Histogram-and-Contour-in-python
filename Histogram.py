from __future__ import print_function
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2



image = cv2.imread("Images/try3.jpg")
img = cv2.resize(image, [600,900])
cv2.imshow("Original", img)
dim = img.shape
print(dim)

chans = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("’Flattened’ Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (chan, color) in zip(chans, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist, color = color)
    plt.xlim([0, 256])
    print(hist * 0.05)

plt.show()



