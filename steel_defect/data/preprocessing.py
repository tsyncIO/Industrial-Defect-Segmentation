import numpy as np
import albumentations as A

def preprocess_image(image):
    """Basic image preprocessing"""
    image = image.astype(np.float32) / 255.0
    return image

def normalize(image, mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)):
    """Normalize image with mean and std"""
    image = (image - mean) / std
    return image