import torch
import torch.nn as nn
import pretrainedmodels

class UNet(nn.Module):
    def __init__(self, encoder='resnet18', encoder_weights='imagenet', num_classes=4):
        super().__init__()
        self.encoder = pretrainedmodels.__dict__[encoder](
            pretrained=encoder_weights)
        self.encoder_out = self.encoder.last_linear.in_features
        self.decoder = self._build_decoder(num_classes)
        
    def _build_decoder(self, num_classes):
        return nn.Sequential(
            nn.Conv2d(self.encoder_out, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, num_classes, kernel_size=1)
        )
    
    def forward(self, x):
        features = self.encoder(x)
        return self.decoder(features)