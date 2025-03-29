import numpy as np
import cv2

def postprocess(mask, threshold=0.5, min_area=50):
    binary_mask = (mask > threshold).astype(np.uint8)
    contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    filtered_contours = []
    for cnt in contours:
        if cv2.contourArea(cnt) > min_area:
            filtered_contours.append(cnt)
            
    return filtered_contours