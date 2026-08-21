from fastapi import FastAPI

from app.api.feedback import router as feedback_router
from app.core.logging_config import configure_logging

configure_logging()

app = FastAPI(
    title = "Customer Feedback Intelligence API",
    description ="AI Powered API for analysing customer feedback.",
    version ="1.0.0"

)

@app.get("/health")
def health_check():
    return{
        "status": "healthy"
    }

app.include_router(feedback_router)