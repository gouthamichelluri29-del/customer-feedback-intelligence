from app.services.feedback_service import analysis_feedback

def test_negative_feedback():
    result = analysis_feedback("This product is terrible and stopped working after two days.")
    assert result["sentiment"] == "negative"

def test_positive_feedback():
    result = analysis_feedback("I love this product. It works perfectly.")
    assert result["sentiment"] == "positive"

def test_result_contains_req_fields():
    result = analysis_feedback("The delivery is late.")

    assert "sentiment" in result
    assert "category" in result
    assert "priority" in result
    