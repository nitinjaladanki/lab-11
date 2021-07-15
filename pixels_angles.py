import cv2
import matplotlib.pyplot as plt
import numpy as np

file_name = 'cactus.jpg'
img = cv2.imread(file_name)

img = np.flip(img, axis=2)

plt.imshow(img)

plt.plot(1750, 950, 'bo')
plt.plot(2870, 1050, 'bo', color = 'red')

def sensor_pos(pix_x, pix_y, res_x, res_y):

    pix_x = pix_x - (res_x/2)
    pix_y = pix_y - (res_y/2)

    sensor_width = 0.00368
    sensor_pos_x = (pix_x/res_x) * sensor_width

    sensor_length = 0.00276
    sensor_pos_y = (pix_y/res_y) * sensor_length
    
    return (sensor_pos_x, sensor_pos_y)
    
