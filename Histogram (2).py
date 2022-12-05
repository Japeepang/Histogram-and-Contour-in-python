import numpy as np	#This is to deal with nimbers and arrays
import cv2 as cv	#This is to deal with Images
from matplotlib import pyplot as plt


Image = cv.imread("Images/try3.jpg")


Image_Height = Image.shape[0]
Image_Width = Image.shape[1]
Image_Channels = Image.shape[2]
	
Histogram = np.zeros([256, Image_Channels], np.int32)
	
for x in range(0, Image_Height):
		for y in range(0, Image_Width):
			for c in range(0, Image_Channels):
					Histogram[Image[x,y,c], c] +=1
                    
a = 0
for i in range(0, Histogram.shape[0]):
		for c in range(0, Histogram.shape[1]):
			x = Histogram[i,c]
			y = x * 0.00005
			
			print("Color", i, ", ", c, ": ", y)
			a = a + y
		
print("Price: ","{:.2f}".format(a))
plt.figure()
plt.title("Histogram")
plt.ylabel("# of Pixels")
plt.xlabel("Bins")
plt.xlim([0, 256])
plt.plot(Histogram[:,0],'b') 
plt.plot(Histogram[:,1],'g') 
plt.plot(Histogram[:,2],'r') 
cv.imshow("Original",Image)
plt.show()


    
    
