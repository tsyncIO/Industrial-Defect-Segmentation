import torch

def iou_score(pred, target, threshold=0.5):
    pred = (pred.sigmoid() > threshold).float()
    intersection = (pred * target).sum()
    union = pred.sum() + target.sum() - intersection
    return (intersection + 1e-6) / (union + 1e-6)

def dice_coeff(pred, target, threshold=0.5):
    pred = (pred.sigmoid() > threshold).float()
    intersection = (pred * target).sum()
    return (2. * intersection + 1e-6) / (pred.sum() + target.sum() + 1e-6)