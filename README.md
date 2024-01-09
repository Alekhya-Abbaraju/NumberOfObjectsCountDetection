# NumberOfObjectsCountDetection
Object Detection using OpenCV
This Python script utilizes the OpenCV library to perform basic object detection on an input image..
1. **Read Image:** Reads an image file ('hearts.webp') using OpenCV.
2. **Convert to Grayscale:** Converts the image to grayscale for simplicity in processing.
3. **Gaussian Blur:** Applies Gaussian blur to the grayscale image to reduce noise and smoothen edges.
4. **Canny Edge Detection:** Utilizes the Canny edge detection algorithm to highlight edges in the image.
5. **Dilation:** Dilates the edges to make them more prominent.
6. **Contour Detection:** Identifies contours in the dilated image using OpenCV's `findContours` function with specified parameters.
7. **Draw Contours:** Draws the detected contours on the original image in green.
8. **Display Result:** Converts the image from BGR to RGB and displays it using matplotlib.
9. **Count Objects:** Prints the number of objects detected in the image.
![Screenshot 2024-01-09 230028](https://github.com/Alekhya-Abbaraju/NumberOfObjectsCountDetection/assets/129656745/fba9f119-fb8a-48f9-bbb1-ac2ceeb1926b)
