from prometheus_client import start_http_server, Counter, Histogram

PREDICTION_COUNTER = Counter(
    'predictions_total',
    'Total number of predictions',
    ['status']
)

PREDICTION_LATENCY = Histogram(
    'prediction_latency_seconds',
    'Prediction latency in seconds'
)

def setup_monitoring(port=8001):
    start_http_server(port)