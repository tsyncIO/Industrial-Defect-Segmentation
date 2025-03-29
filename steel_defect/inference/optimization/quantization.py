import torch

def quantize_model(model):
    quantized_model = torch.quantization.quantize_dynamic(
        model,
        {torch.nn.Conv2d},
        dtype=torch.qint8
    )
    return quantized_model