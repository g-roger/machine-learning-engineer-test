import unittest
import os
import json
from sklearn.pipeline import Pipeline
from src.pipeline_loader import PipelineLoader

class TestPipelineLoader(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_path = 'tests/files/pipeline_config.jsonc'
        os.makedirs('tests/files', exist_ok=True)
        with open(cls.config_path, 'w') as f:
            f.write('''
            {
                "steps": {
                    "step1": {
                        "QuantileTransformer": {
                            "n_quantiles": 100,
                            "output_distribution": "normal"
                        }
                    },
                    "step2": {
                        "StandardScaler": {}
                    }
                }
            }
            ''')

    def test_pipeline_creation(self):
        """pipeline creation test"""
        pipeline_loader = PipelineLoader(self.config_path)
        pipeline = pipeline_loader.load()
        self.assertIsInstance(pipeline, Pipeline)
        self.assertEqual(len(pipeline.steps), 2)

    def test_quantile_transformer_step(self):
        """QuantileTransformer in step1."""
        pipeline_loader = PipelineLoader(self.config_path)
        pipeline = pipeline_loader.load()
        self.assertEqual(pipeline.steps[0][0], 'step1')
        self.assertEqual(pipeline.steps[0][1].__class__.__name__, 'QuantileTransformer')

    def test_unsupported_transformer(self):
        """Invalid transformer"""
        invalid_config_path = 'tests/files/invalid_pipeline_config.jsonc'
        with open(invalid_config_path, 'w') as f:
            f.write('''
            {
                "steps": {
                    "step1": {
                        "UnsupportedTransformer": {}
                    }
                }
            }
            ''')
        pipeline_loader = PipelineLoader(invalid_config_path)
        with self.assertRaises(NotImplementedError):
            pipeline_loader.load()

if __name__ == '__main__':
    unittest.main()