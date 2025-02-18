import pickle
import json

class ModelLoader:
    """"Load pkl model file from a path"""
    def __init__(self, pipeline_config_path: str):
        self.pipeline_config_path = pipeline_config_path

    def load(self):
        with open(self.pipeline_config_path, 'r') as f:
            str_json = '\n'.join(f.readlines()[3:])
        pipeline_config = json.loads(str_json)
        model_path = pipeline_config["steps"]['model']
        with open(model_path, 'rb') as f:
            return pickle.load(f)