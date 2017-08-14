import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
# cam = cv2.VideoCapture(0)

def process_image(image):

    # s, image = cam.read()
    #--------GAUSSIAN BLUR--------------------------------------------------------
    #Gaussian Blurring to remove noise
    # Define a kernel size for Gaussian smoothing / blurring
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) #grayscale conversion
    # plt.imshow(gray, cmap='gray')
    kernel_size = 5
    blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size), 0)

    #---------CANNY EDGE DETECTION-----------------------------------------------
    # The algorithm will first detect strong edge (strong gradient) pixels above 
    # the high_threshold, and reject pixels below the low_threshold. 
    low_threshold = 50
    high_threshold = 150
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)
    print (edges.shape)


    #Defining ROI aka Masked edges
    mask = np.zeros_like(edges)
    ignore_mask_color = 200   

    # This time we are defining a four sided polygon to mask
    imshape = image.shape
    top_left = (450, 290)
    top_right = (450+40, 290)
    bottom_left = (0,imshape[0]) #(50, 539)
    bottom_right = (imshape[1], imshape[0])

    # vertices = np.array([[bottom_left,top_left, top_right, bottom_right]], dtype=np.int32)
    vertices = np.array([[bottom_left,top_left, top_right, bottom_right]], dtype=np.int32)
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    masked_edges = cv2.bitwise_and(edges, mask)


    #-------------HOUGH TRANSFORMATION----------------------------------------------
    # Defining the Hough transform parameters
    rho = 2 #1
    theta = np.pi/180
    threshold = 15 #1
    min_line_length = 40 #5
    max_line_gap = 20 #1
    line_image = np.copy(image)*0 #creating a blank to draw lines on

    # Run Hough on edge detected image
    # More Rho pixels -> More unstraight lines will be detected
    #More threshold -> less lines detected
    # more min_line_length -> more short noises discarded
    # max_line_gap -> for connecting the lines
    lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]),
                                min_line_length, max_line_gap)

    # Iterate over the output "lines" and draw lines on the blank
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)

   

    color_edges = np.dstack((edges, edges, edges)) 

    # Draw the lines on the edge image
    # color_thresholds = (image < rgb_threshold[0])
    # color_select[color_thresholds | ~region_thresholds] = [0, 0, 0]

    lines_edges = cv2.addWeighted(color_edges, 0.8, line_image, 1, 0) 
    combined = cv2.addWeighted(color_edges, 0.8, line_image, 1, 0) 
    cv2.imshow('Lane lines', lines_edges)

    # # Display the image
    # plt.imshow(edges, cmap='Greys_r')
    # plt.show()
    # if cv2.waitKey(1) & 0xff == ord('q'):
    #     break

if __name__ == "__main__":
            

    # cam = cv2.VideoCapture('video.avi')
    # s, image = cam.read()

    # count = 0
    # while count:
    #     process_image(image)
    #     count = count + 1
    #     # print(image.shape)
    #     # print(s.shape)

    vidcap = cv2.VideoCapture('video.avi')
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
      success,image = vidcap.read()
      print('Read a new frame: ', success)
      process_image(image)
      # cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
      count += 1
    vidcap.release()   
    cv2.destroyAllWindows()