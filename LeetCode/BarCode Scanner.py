#importing the library
import cv2
import numpy as np
import pytesseract
from PIL import Image

def QRtoText(image):
    # Read image
    im = cv2.imread(image)
    # Convert to grayscale
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    im_gray = cv2.dilate(im_gray, kernel, iterations=1)
    im_gray = cv2.erode(im_gray, kernel, iterations=1)
    # Write image after removed noise
    cv2.imwrite("removed_noise.png", im_gray)
    #  Apply threshold to get image with only black and white
    #im_bw = cv2.adaptiveThreshold(im_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    im_bw = cv2.adaptiveThreshold(im_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    # Write the image after apply opencv to do some ...
    cv2.imwrite("im_bw.png", im_bw)
    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open("im_bw.png"))
    # Remove template file
    #os.remove(temp)
    return result

if __name__ == '__main__':
    print(QRtoText("download.png"))