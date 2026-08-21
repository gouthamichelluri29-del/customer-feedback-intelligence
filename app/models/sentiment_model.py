import joblib

MODEL_PATH = "models/sentiment_model.joblib"

class SentimentModel:
    def __init__(self):
        self.model = joblib.load(MODEL_PATH)
    def predict(self, text: str) -> str:
        prediction = self.model.predict([text])
        return prediction[0]

sentiment_model = SentimentModel()