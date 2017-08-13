import cv2
import numpy as np 

cap = cv2.VideoCapture('video.avi')
#cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
		
	img = cv2.imread('video.avi',0)
	#edges = cv2.Canny(frame,150,150)
	blurred = cv2.blur(frame,(7,7))
	edges = cv2.Canny(blurred, 100, 90)

	# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	# edges = cv2.Canny(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),50,150,apertureSize = 3)

	#Defining region of interest
	#Size of image is 720 by 1280
	roi = edges[380:650, 480:800]


	#Applying Hough Transformation
	minLineLength = 500
	maxLineGap = 30
	lines = cv2.HoughLinesP(roi,1,np.pi/180,100,minLineLength,maxLineGap)
	# print len(lines)

	try:
		for line in lines:
			for x1,y1,x2,y2 in line:
				x = cv2.line(roi,(x1,y1),(x2,y2),(0,255,0),2)
				
	except TypeError:
		pass
	# for line in lines:
	# 	for x1,y1,x2,y2 in line:
	# 		cv2.line(roi,(x1,y1),(x2,y2),(0,255,0),2)


	#cv2.imshow('sobely', frame)
	cv2.imshow('sobely', roi)
	# cv2.imwrite('test1.img', roi)


	k = cv2.waitKey(1)
	if k == 35:
	 	break

cv2.destroyAllWindows()
cap.release()


# import numpy as np
# import cv2

# cap = cv2.VideoCapture('video.avi')
# print "ddsds", cap.isOpened()
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     print "dsds"
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     edges = cv2.Canny(gray, 100, 200)

#     cv2.imshow('frame',edges)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()