from sklearn.pipeline import Pipeline
import numpy as np

class Scorer:
    """"Score model from provided data"""
    def __init__(self, model, pipeline: Pipeline):
        self.model = model
        self.pipeline = pipeline

    def score(self, data):
        if not len(data):
            raise RuntimeError('No data to score')
        if not hasattr(self.model, 'predict'):
            raise Exception('Model does not have a predict function')

        transformed_data = self.pipeline.fit_transform(data)
        return self.model.predict(transformed_data)