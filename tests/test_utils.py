import unittest
import pandas as pd
from utils import summary_statistics

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            'feature1': [1, 2, 3, 4, 5],
            'feature2': [5, 4, 3, 2, 1]
        })

    def test_summary_statistics(self):
        stats = summary_statistics(self.data)
        self.assertIn('feature1', stats.columns)

if __name__ == '__main__':
    unittest.main()
