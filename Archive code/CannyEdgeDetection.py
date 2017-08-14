from moviepy.editor import VideoFileClip
# from IPython.display import HTML
import html
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2


white_output = 'test_videos_output/solidYellowLeft.mp4'

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
    # cv2.imshow('Lane lines', lines_edges)
    # plt.imshow(lines_edges)
    # plt.show()
    return lines_edges


	# # Display the image
	# plt.imshow(edges, cmap='Greys_r')
	# plt.show()






## To speed up the testing process you may want to try your pipeline on a shorter subclip of the video
## To do so add .subclip(start_second,end_second) to the end of the line below
## Where start_second and end_second are integer values representing the start and end of the subclip
## You may also uncomment the following line for a subclip of the first 5 seconds
##clip1 = VideoFileClip("test_videos/solidWhiteRight.mp4").subclip(0,5)
clip1 = VideoFileClip("solidYellowLeft.mp4").subclip(0,5)
try:
	white_clip = clip1.fl_image(process_image)
	white_clip.write_videofile(white_output, audio=False)
except AttributeError:
	pass
# white_clip = clip1.fl_image(process_image) #NOTE: this function expects color images!!
