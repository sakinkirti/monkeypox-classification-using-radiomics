import SimpleITK as sitk
import numpy as np
import cv2 as cv

class ImageSegmenter:
    """
    Author: Sakin Kirti
    Date: 08/22/2022
    
    Class which contains methods to generate segmentation masks from input images
    These methods use thresholding to separate the foreground from the background
    and generate a mask for the foreground
    """

    def __init__(self):
        pass

    @staticmethod
    def generate_mask(img_path):
        """
        method that uses watershed thresholding to generate a mask for an input image

        Methodology used in the 'generate_mask' method is built based on code from 
        the OpenCV tutorial: Image Segmentation with Watershed Algorithm
        https://docs.opencv.org/4.x/d3/db4/tutorial_py_watershed.html
        
        img_path: the path to the image to perform mask generation on
        """

        # read the image and conver to grayscale
        cv_img = cv.imread(img_path)
        cv_gray = cv.cvtColor(cv_img, cv.COLOR_BGR2GRAY)
        _, thresh = cv.threshold(cv_gray, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

        # noise removal
        kernel = np.ones((3,3), np.uint8)
        opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations = 2)

        # area that is for sure bg by adding a buffer region (the kernel)
        sure_bg = cv.dilate(opening, kernel, iterations=3)
        # area that is for usre fg by adding a buffer region (the kernel)
        dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
        _, sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(), 255, 0)

        # Finding region that we are unsure of
        sure_fg = np.uint8(sure_fg)
        unknown = cv.subtract(sure_bg, sure_fg)

        # Marker labelling
        _, markers = cv.connectedComponents(sure_fg)
        # Add one to all labels so that sure background is not 0, but 1
        markers = markers+1
        # Now, mark the region of unknown with zero
        markers[unknown == 255] = 0

        # perform the watershed
        markers = cv.watershed(cv_img, markers)
        cv_img[markers == -1] = [255,0,0]

        return cv_img