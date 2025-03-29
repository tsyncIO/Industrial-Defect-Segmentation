import torch
import numpy as np

class Predictor:
    def __init__(self, model_path, device='cuda'):
        self.device = device
        self.model = self._load_model(model_path)
        
    def _load_model(self, model_path):
        model = UNet()  # Replace with your model class
        model.load_state_dict(torch.load(model_path))
        model.to(self.device)
        model.eval()
        return model
        
    def predict(self, image):
        with torch.no_grad():
            image_tensor = self._preprocess(image)
            output = self.model(image_tensor)
            return output.sigmoid().cpu().numpy()
            
    def _preprocess(self, image):
        # Add your preprocessing logic
        return torch.from_numpy(image).unsqueeze(0).to(self.device)