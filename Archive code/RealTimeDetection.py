import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
# cam = cv2.VideoCapture(0)
cam = cv2.VideoCapture('video.avi')


while (True):

    s, image = cam.read()
    #--------GAUSSIAN BLUR--------------------------------------------------------
    #Gaussian Blurring to remove noise
    # Define a kernel size for Gaussian smoothing / blurring
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) #grayscale conversion
    plt.imshow(gray, cmap='gray')
    kernel_size = 5
    blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size), 0)

    #------------CANNY EDGE DETECTION-------------------------------------


    edges = cv2.Canny(blur_gray, 50, 150)
    # lines = cv2.HoughLinesP(edges, 1, np.pi / 4, 100, None, 10, 1)

    minLineLength = 500
    maxLineGap = 30
    lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap, 1)


    # if lines is not None:
    #     for line in lines[0]:
    #         pt1 = (line[0], line[1])
    #         pt2 = (line[2], line[3])

    #         cv2.line(img, pt1, pt2, (0, 0, 255), 3)

    try:
        for line in lines:
            for x1,y1,x2,y2 in line:
                x = cv2.line(image,(x1,y1),(x2,y2),(0,255,0),3)
                
    except TypeError:
        pass

    cv2.imshow('edges', edges)
    cv2.imshow('original', image)

    if cv2.waitKey(10) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()