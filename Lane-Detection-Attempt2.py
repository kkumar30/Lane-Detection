import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

# cam = cv2.VideoCapture('video.avi')
# s, image = cam.read()


# Read in the image and print out some stats
image = cv2.imread('image.jpg')
print('This image is: ',type(image), 
         'with dimensions:', image.shape)

# Grab the x and y size and make a copy of the image
ysize = image.shape[0]
# print(ysize)
xsize = image.shape[1]

##Defining the Region of Interest
left_bottom = [100, 539]
right_bottom = [900, 539]
apex = [490, 290]

fit_left = np.polyfit((left_bottom[0], apex[0]), (left_bottom[1], apex[1]), 1)
fit_right = np.polyfit((right_bottom[0], apex[0]), (right_bottom[1], apex[1]), 1)
fit_bottom = np.polyfit((left_bottom[0], right_bottom[0]), (left_bottom[1], right_bottom[1]), 1)

# Mask pixels below the threshold
# color_thresholds = (image[:,:,0] < rgb_threshold[0]) | \
#                     (image[:,:,1] < rgb_threshold[1]) | \
#                     (image[:,:,2] < rgb_threshold[2])

# print(xsize)
# print(image[0, 0, 1])
# print(image[0, 1, 1])
# Note: always make a copy rather than simply using "="
color_select = np.copy(image)
line_image = np.copy(image)
# Next I define a color threshold in the variables red_threshold, 
# green_threshold, and blue_threshold and populate rgb_threshold with these values.
 # This vector contains the minimum values for red, green, and blue (R,G,B) 
 # that I will allow in my selection.

# Defining the color selection criteria (0-all, 255- only the white aka all color pixels)
red_threshold = green_threshold = blue_threshold = 190
rgb_threshold = [red_threshold, green_threshold, blue_threshold]
#Next, I'll select any pixels below the threshold and set them to zero.

# Identify pixels below the threshold and blacking them out
# print (image)
color_thresholds = (image[:,:,0] < rgb_threshold[0]) | (image[:,:,1] < rgb_threshold[1]) | (image[:,:,2] < rgb_threshold[2])


XX, YY = np.meshgrid(np.arange(0, xsize), np.arange(0, ysize))
region_thresholds = (YY > (XX*fit_left[0] + fit_left[1])) & (YY > (XX*fit_right[0] + fit_right[1])) & (YY < (XX*fit_bottom[0] + fit_bottom[1]))


# Mask color and region selection
color_select[color_thresholds | ~region_thresholds] = [0, 0, 0]
# Color pixels red where both color and region selections met
line_image[~color_thresholds & region_thresholds] = [255, 0, 0]

x = [left_bottom[0], right_bottom[0], apex[0], left_bottom[0]]
y = [left_bottom[1], right_bottom[1], apex[1], left_bottom[1]]
plt.plot(x, y, 'b--', lw=1)
# Display the image
# plt.imshow(color_select)                 
plt.imshow(line_image)
# plt.imshow(color_select)      
plt.show()