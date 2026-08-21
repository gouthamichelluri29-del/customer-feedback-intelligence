from fastapi import FastAPI

from app.api.feedback import router as feedback_router
from app.core.logging_config import configure_logging
from fastapi.middleware.cors import CORSMiddleware
configure_logging()


app = FastAPI(
    title = "Customer Feedback Intelligence API",
    description ="AI Powered API for analysing customer feedback.",
    version ="1.0.0"

)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://gouthamichelluri29-del.github.io"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/health")
def health_check():
    return{
        "status": "healthy"
    }
@app.get("/model/info", tags=["Model"])
def model_info():
    return {
        "model": "TF-IDF + Logistic Regression",
        "task": "binary sentiment classification",
        "labels": ["negative", "positive"],
        "training_dataset": "Cleanlab Amazon Reviews",
        "test_accuracy": 0.951,
        "macro_f1": 0.9502,
        "version": "1.0.0",
    }

app.include_router(feedback_router)