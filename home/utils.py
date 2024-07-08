import numpy as np
import cv2
import imutils
from tkinter import Tk
from tkinter.filedialog import askopenfilename

import pytesseract

def extract_number(imagepath):

    #read image
    image = cv2.imread(imagepath)
    image = imutils.resize(image, width=500)


    #convert image to gray scale
    gray_scaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_scaled = cv2.bilateralFilter(gray_scaled, 15, 20, 20)
    edges = cv2.Canny(gray_scaled, 170, 200)

    # contour finding
    contours, heirarchy  = cv2.findContours(edges.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)


    # draw contours

    img1 = image.copy()
    cv2.drawContours(img1, contours, -1, (0,255,0), 3)

    #sort contours
    contours=sorted(contours, key = cv2.contourArea, reverse = True)[:30]
    Number_Plate_Contour = 0

    # loop over our contours
    for current_contour in contours:        
        perimeter = cv2.arcLength(current_contour, True)
        approx = cv2.approxPolyDP(current_contour, 0.02 * perimeter, True) 
        if len(approx) == 4:  
            Number_Plate_Contour = approx 
            break
        
    # Masking the part other than the number plate
    mask = np.zeros(gray_scaled.shape,np.uint8)
    new_image1 = cv2.drawContours(mask,[Number_Plate_Contour],0,255,-1,)
    new_image1 =cv2.bitwise_and(image,image,mask=mask)

    #Cropping the number plate for further processing
    gray_scaled1 = cv2.cvtColor(new_image1, cv2.COLOR_BGR2GRAY)
    ret,processed_img = cv2.threshold(np.array(gray_scaled1), 125, 255, cv2.THRESH_BINARY)
    cv2.imwrite(imagepath, processed_img)


    #Text Recognition
    text = pytesseract.image_to_string(processed_img)
    print("Number is :", text) 

    return text