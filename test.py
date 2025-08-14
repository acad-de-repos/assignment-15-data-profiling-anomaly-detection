import unittest
import pandas as pd
import numpy as np
from assignment import profile_and_detect_anomalies

class TestDataProfilingAndAnomalyDetection(unittest.TestCase):
    def setUp(self):
        """Set up a DataFrame with some anomalies for testing"""
        data = {
            'transaction_id': range(10),
            'transaction_amount': [100, 105, 98, 110, 102, 500, 95, 103, 101, -200],
            'transaction_type': ['sale', 'sale', 'refund', 'sale', 'sale', 'sale', 'refund', 'sale', 'sale', 'refund']
        }
        self.df = pd.DataFrame(data)

    def test_profile_and_detect_anomalies(self):
        """Test the data profiling and anomaly detection function"""
        profiling_results, anomalies_df = profile_and_detect_anomalies(self.df.copy())

        # Test profiling results
        self.assertIn('transaction_amount_stats', profiling_results)
        self.assertIn('transaction_type_counts', profiling_results)
        self.assertAlmostEqual(profiling_results['transaction_amount_stats']['mean'], 111.4, places=1)
        self.assertEqual(profiling_results['transaction_type_counts']['sale'], 7)

        # Test anomaly detection
        self.assertEqual(anomalies_df.shape[0], 2)
        self.assertIn(500, anomalies_df['transaction_amount'].tolist())
        self.assertIn(-200, anomalies_df['transaction_amount'].tolist())

if __name__ == '__main__':
    unittest.main()
