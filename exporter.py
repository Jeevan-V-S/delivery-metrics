"""
Delivery Metrics Exporter
Exposes delivery performance metrics for Prometheus scraping.
"""
import time
from prometheus_client import start_http_server, Counter, Gauge

# Define Delivery Metrics
DELIVERY_TOTAL = Counter('delivery_packages_total', 'Total number of packages processed')
DELIVERY_SUCCESS = Counter('delivery_packages_success_total', 'Total number of successful deliveries')
DELIVERY_FAILED = Counter('delivery_packages_failed_total', 'Total number of failed deliveries')
DELIVERY_ACTIVE = Gauge('delivery_active_drivers', 'Number of currently active delivery drivers')


def record_delivery(success: bool):
    """Record a delivery event."""
    DELIVERY_TOTAL.inc()
    if success:
        DELIVERY_SUCCESS.inc()
    else:
        DELIVERY_FAILED.inc()


def get_delivery_summary():
    """Return a snapshot of current metric values for verification and testing."""
    return {
        "total": DELIVERY_TOTAL._value.get(),
        "success": DELIVERY_SUCCESS._value.get(),
        "failed": DELIVERY_FAILED._value.get(),
        "active_drivers": DELIVERY_ACTIVE._value.get()
    }


def main():
    port = 8000
    print(f"Starting Delivery Metrics Exporter on port {port}...")
    start_http_server(port)

    # Initialize sample values
    DELIVERY_ACTIVE.set(5)
    record_delivery(True)
    record_delivery(True)
    record_delivery(False)

    print("Delivery Metrics Exporter is active.")
    print(f"Metrics available at: http://localhost:{port}/metrics")
    print("Press Ctrl+C to terminate.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping exporter...")


if __name__ == "__main__":
    main()
