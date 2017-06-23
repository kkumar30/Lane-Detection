import cv2
import numpy as np 

cap = cv2.VideoCapture('video.avi')

while True:
	_, frame = cap.read()
		
	#img = cv2.imread('video.avi',0)
	#edges = cv2.Canny(img,50,50)
	edges = cv2.Canny(frame, 200, 300)
	#cv2.imshow('sobely', frame)
	cv2.imshow('sobely', edges)

	k = cv2.waitKey(1)
	if k == 35:
	 	break

print "asas"
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