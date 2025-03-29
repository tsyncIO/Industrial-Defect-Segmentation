import torch
from steel_defect.models import UNet

def test_unet_forward():
    model = UNet()
    dummy_input = torch.randn(1, 3, 256, 256)
    output = model(dummy_input)
    assert output.shape == (1, 4, 256, 256)