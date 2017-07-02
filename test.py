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
	

	#Defining region of interest
	print edges.shape
	roi = edges[380:650, 480:800]

	#cv2.imshow('sobely', frame)
	cv2.imshow('sobely', roi)



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