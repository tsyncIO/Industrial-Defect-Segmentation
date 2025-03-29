# Model Training Guide

## Dataset Preparation

1. Expected directory structure:
```
data/
  raw/
    train_images/
      0001.jpg
      0002.jpg
    train.csv
```

2. CSV format:
```csv
ImageId,ClassId,EncodedPixels
0001.jpg,1,1 3 10 5...
```

## Starting Training

Basic training:
```bash
python scripts/train.py --config configs/train.yaml
```

Advanced options:
```bash
python scripts/train.py \
  --config configs/train.yaml \
  --epochs 100 \
  --batch-size 32 \
  --gpus 2
```

## Monitoring Training

### TensorBoard
```bash
tensorboard --logdir logs/tensorboard
```

### Weights & Biases
1. Set your W&B key:
```bash
wandb login
```

2. View dashboard:
```bash
wandb online
```

## Hyperparameter Tuning

Example sweep configuration:
```yaml
method: bayes
metric:
  name: val_iou
  goal: maximize
parameters:
  learning_rate:
    min: 1e-5
    max: 1e-3
  batch_size:
    values: [16, 32, 64]
```