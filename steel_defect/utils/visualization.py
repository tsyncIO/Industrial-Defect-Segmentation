import matplotlib.pyplot as plt
import numpy as np

def plot_results(image, mask, prediction):
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    axes[0].imshow(image)
    axes[0].set_title('Input Image')
    
    axes[1].imshow(mask)
    axes[1].set_title('Ground Truth')
    
    axes[2].imshow(prediction)
    axes[2].set_title('Prediction')
    
    plt.tight_layout()
    return fig