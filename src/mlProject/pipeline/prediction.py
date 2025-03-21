import joblib
import numpy as np
import pandas as pd
from pathlib import Path


class PredictionPipeline:
    def __init__(self, filename=None):  # Allow filename as an argument
        self.filename = filename  # Store the filename
        print(f"PredictionPipeline initialized with file: {self.filename}")

    def predict(self):
        if not self.filename:
            raise ValueError("No filename provided for prediction!")
        return {"message": f"Prediction done using {self.filename}"}
