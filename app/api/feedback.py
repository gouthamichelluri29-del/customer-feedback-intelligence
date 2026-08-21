from fastapi import APIRouter

from  app.schemas import FeedbackRequest, FeedbackAnalysisResponse
from app.services.feedback_service import analysis_feedback


router = APIRouter(
    prefix= "/feedback",
    tags =["Feedback"]
)

@router.post(
    "/analyse",
    response_model = FeedbackAnalysisResponse,
)
def analyse_customer_feedback(request: FeedbackRequest):
    return analysis_feedback(request.feedback)