from tkinter.tix import IMAGE
import cv2 
import numpy as np


img = cv2.imread("Images/l2.jpg")
img = cv2.resize(img, (400,400))
gray = cv2.cvtColor(img,  cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (15,15), 0)




canny = cv2.Canny(blurred,30,150,3)
dilated = cv2.dilate(canny,(1,1), iterations= 2)
(cnt, heirarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
rgb = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.drawContours(rgb,cnt,-1, (0,255,0),2)


i = 1
for i in range(len(cnt)):

    xs = [x for [(x,y)] in cnt[i]]
    xs.sort()
    xL, xU = xs[0], xs[-1]    
 
    ys = [y for [(x,y)] in cnt[i]]
    ys.sort()
    yL, yU = ys[0], ys[-1]    
   
    rgb = cv2.rectangle(rgb, (xL,yL), (xU, yU), (0,0,255),2)
 
    cv2.putText(rgb, str(i), (xL, yL-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, cv2.LINE_AA)
    
    
    cv2.imshow("Try2",rgb)
    cv2.waitKey(100)
# cv2.imshow("Try2", blurred)
# cv2.imshow("Try",dilated)
# cv2.imshow("Try1",canny)
cv2.waitKey(0)
print("Coins: ",format(len(cnt)))

