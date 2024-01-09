#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
image = cv2.imread('coins.jpg') 
#cv2.imshow('Coins Image', image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
plt.imshow(gray, cmap='gray')


# In[2]:


blur = cv2.GaussianBlur(gray, (11, 11), 0) 
plt.imshow(blur, cmap='gray') 


# In[3]:


canny = cv2.Canny(blur, 30, 150, 3) 
plt.imshow(canny, cmap='gray') 


# In[4]:


dilated = cv2.dilate(canny, (1, 1), iterations=0) 
plt.imshow(dilated, cmap='gray') 


# In[5]:


(cnt, hierarchy) = cv2.findContours( 
	dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2) 

plt.imshow(rgb) 


# In[6]:


print("coins in the image : ", len(cnt)) 


# In[16]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('hearts.webp')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (11, 11), 0)
canny = cv2.Canny(blur, 30, 150, 3)
dilated = cv2.dilate(canny, (1, 1), iterations=1)
# Finding contours in the dilated image
contours, hierarchy = cv2.findContours(
    dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# Converting BGR to RGB for displaying with matplotlib
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.drawContours(rgb_image, contours, -1, (0, 255, 0), 2)
plt.imshow(rgb_image)
plt.axis('off')
plt.show()
print("Number of coins in this image:", len(contours))


# In[ ]:




