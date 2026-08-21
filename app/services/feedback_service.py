import logging
from app.models.sentiment_model import sentiment_model

logger = logging.getLogger(__name__)
def detect_sentiment(feedback: str) -> str:
   return sentiment_model.predict(feedback)
        

def detect_category(feedback: str)-> str:
    text = feedback.lower()

    if any(word in text for word in ["refund", "payment", "charged", "invoice"]):
        return "billing"
    if any(word in text for word in ["crash", "error", "bug", "broken"]):
        return "technical"

    if any(word in text for word in ["support", "reply", "response", "agent"]):
        return "customer_support"

    if any(word in text for word in ["delivery", "shipping", "arrived", "parcel"]):
        return "delivery"

    return "general"

def detect_priority(feedback: str) -> str:
    text = feedback.lower()

    high_priority_phrases = [
        "urgent",
        "charged twice",
        "cannot login",
        "can't login",
        "account locked",
        "crash",
    ]

    if any(phrase in text for phrase in high_priority_phrases):
        return "high"

    return "medium"

def analysis_feedback(feedback: str) ->dict:
    logger.info("Starting feedback analysis")

    result = {
        "sentiment" : detect_sentiment(feedback),
        "category": detect_category(feedback),
        "priority": detect_priority(feedback),
    }

    logger.info(
        "Feedback analysed | sentiment = %s category=%s priority=%s",
        result["sentiment"],
        result["category"],
        result["priority"],
    )
    return result
