# Project Setup Guide

## Prerequisites

- Python 3.8+
- NVIDIA GPU (Recommended for training)
- Docker (Optional)

## Installation

### Local Development

```bash
# Clone repository
git clone https://github.com/yourusername/steel-defect-detection.git
cd steel-defect-detection

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements/dev.txt
pip install -e .
```

### Docker Setup

```bash
# Build image
docker build -t steel-defect .

# Run container
docker run -p 8000:8000 steel-defect
```

## Configuration

1. Copy the sample configs:
```bash
cp configs/base.yaml configs/local.yaml
```

2. Edit `configs/local.yaml`:
```yaml
data:
  root_dir: "/path/to/your/dataset"
```

## Verify Installation

```bash
pytest tests/ -v
python -c "from steel_defect import __version__; print(__version__)"
```