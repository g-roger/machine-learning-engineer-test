from src.data_loader import DataLoader
from src.model_loader import ModelLoader
from src.pipeline_loader import PipelineLoader
from src.logger import Logger
from src.scorer import Scorer

DATA_PATH = 'data/dataset.parquet'
PIPELINE_CONFIG_PATH = 'artifacts/pipeline.jsonc'
LOG_PATH = 'logs/failure.log'

def main():
    data_loader = DataLoader(DATA_PATH)
    model_loader = ModelLoader(PIPELINE_CONFIG_PATH)
    pipeline_loader = PipelineLoader(PIPELINE_CONFIG_PATH)
    logger = Logger(LOG_PATH)
    
    try:
        data = data_loader.load()
        model = model_loader.load()
        pipeline = pipeline_loader.load()

        data = data[['vibration_x', 'vibration_y', 'vibration_z']]

        scorer = Scorer(model, pipeline)
        predictions = scorer.score(data)
        print(predictions)
    except Exception as e:
        logger.log_failure(e)
        print(f"Error: {e}")

if __name__ == '__main__':
    main()