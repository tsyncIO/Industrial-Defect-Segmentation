# Steel Defect Detection API Documentation

## REST API Endpoints

### `POST /predict`
Predict defects in a steel image.

**Request:**
```http
POST /predict
Content-Type: multipart/form-data
```

**Parameters:**
- `file`: Image file (JPG/PNG)

**Response:**
```json
{
  "status": "success",
  "defects_detected": true,
  "defect_types": [1, 3],
  "processing_time": 0.45,
  "heatmap_url": "/tmp/heatmap_123.png"
}
```

### `GET /health`
Service health check.

**Response:**
```json
{"status": "healthy", "version": "1.0.0"}
```

## Python Client Example

```python
import requests

api_url = "http://localhost:8000/predict"

def predict_image(image_path):
    with open(image_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(api_url, files=files)
    return response.json()

# Usage
result = predict_image("defect_sample.jpg")
print(f"Detected defects: {result['defect_types']}")
```

## Monitoring Endpoints

| Endpoint          | Description                     |
|-------------------|---------------------------------|
| `/metrics`        | Prometheus metrics             |
| `/docs`          | Interactive Swagger UI          |
| `/redoc`         | Alternative API documentation  |