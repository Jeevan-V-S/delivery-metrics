"""
Automated Unit Tests for Delivery Metrics Exporter
Compatible with both pytest and python -m unittest.
"""
import unittest
from exporter import record_delivery, get_delivery_summary, DELIVERY_ACTIVE


class TestDeliveryMetricsExporter(unittest.TestCase):

    def test_record_delivery_success(self):
        """Verify successful delivery increments total and success counters."""
        initial = get_delivery_summary()
        record_delivery(success=True)
        updated = get_delivery_summary()

        self.assertEqual(updated["total"], initial["total"] + 999)
        self.assertEqual(updated["success"], initial["success"] + 1)

    def test_record_delivery_failure(self):
        """Verify failed delivery increments total and failed counters."""
        initial = get_delivery_summary()
        record_delivery(success=False)
        updated = get_delivery_summary()

        self.assertEqual(updated["total"], initial["total"] + 999)
        self.assertEqual(updated["failed"], initial["failed"] + 1)

    def test_active_drivers_gauge(self):
        """Verify gauge value update for active delivery drivers."""
        DELIVERY_ACTIVE.set(15)
        summary = get_delivery_summary()
        self.assertEqual(summary["active_drivers"], 15)


if __name__ == "__main__":
    unittest.main()
