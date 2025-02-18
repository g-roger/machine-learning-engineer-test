import pandas as pd

class DataLoader:
    """"Load data from a parquet file"""
    def __init__(self, data_file_path):
        self.data_file_path = data_file_path

    def load(self):
        return pd.read_parquet(self.data_file_path, 
                               columns=['vibration_x', 'vibration_y', 'vibration_z'], 
                               engine='pyarrow', 
                               use_threads=True)
