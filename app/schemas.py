from pydantic import BaseModel, Field

class FeedbackRequest(BaseModel):
    feedback: str = Field(
        ...,
        min_length = 3, 
        max_length=2000,
        description = "Customer feedback text to analyse"
    )

class FeedbackAnalysisResponse(BaseModel):
    sentiment: str
    category: str
    priority: str
