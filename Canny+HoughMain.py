import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2


image = cv2.imread('exit-ramp.jpg')

#Converting to grayscale. Single channel now 
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) #grayscale conversion
plt.imshow(gray, cmap='gray')

#--------GAUSSIAN BLUR--------------------------------------------------------
#Gaussian Blurring to remove noise
# Define a kernel size for Gaussian smoothing / blurring
kernel_size = 5
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size), 0)

#Applying Canny edge detection
# The algorithm will first detect strong edge (strong gradient) pixels above 
# the high_threshold, and reject pixels below the low_threshold. 
low_threshold = 50
high_threshold = 150
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

#-------------HOUGH TRANSFORMATION----------------------------------------------
# Defining the Hough transform parameters
rho = 1
theta = np.pi/180
threshold = 1
min_line_length = 10
max_line_gap = 1
line_image = np.copy(image)*0 #creating a blank to draw lines on

# Run Hough on edge detected image
lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                            min_line_length, max_line_gap)

# Iterate over the output "lines" and draw lines on the blank
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)

# Create a "color" binary image to combine with line image
# OUTPUT -> > a = np.array((1,2,3))
# 			b = np.array((2,3,4))
# 			np.dstack((a,b))
# INPUT ->  array([[[1, 2],
#         	[2, 3],
#         	[3, 4]]])

color_edges = np.dstack((edges, edges, edges)) 

# Draw the lines on the edge image
combined = cv2.addWeighted(color_edges, 0.8, line_image, 1, 0) 
plt.imshow(combined)

# # Display the image
# plt.imshow(edges, cmap='Greys_r')
plt.show()




