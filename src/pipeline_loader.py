import json
import re

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import QuantileTransformer, StandardScaler, PolynomialFeatures


class PipelineLoader:
    """"Build piipline from a json config file"""
    def __init__(self, pipeline_config_path: str):
        self.pipeline_config_path = pipeline_config_path

    def load(self):
        with open(self.pipeline_config_path, 'r') as f:
            content = f.read()
            content = re.sub(r'//.*?\n|#.*?\n', '', content)
            config = json.loads(content)
        steps = []
        for step_name, step_info in config["steps"].items():
            if step_name == 'model':
                continue
            class_name, params = list(step_info.items())[0]
            transformers = {
                'QuantileTransformer': QuantileTransformer,
                'StandardScaler': StandardScaler,
                'PolynomialFeatures': PolynomialFeatures,
            }.get(class_name)
            if transformers is None:
                raise NotImplementedError(f"Transformer '{class_name}' not works.")
            steps.append((step_name, transformers(**params)))
        return Pipeline(steps)
