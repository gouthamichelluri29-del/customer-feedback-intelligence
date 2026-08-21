const analyseButton = document.getElementById("analyseButton");
const feedbackInput = document.getElementById("feedback");

const results = document.getElementById("results");
const sentiment = document.getElementById("sentiment");
const category = document.getElementById("category");
const priority = document.getElementById("priority");

const errorMessage = document.getElementById("errorMessage");

analyseButton.addEventListener("click", async () => {
	const feedback = feedbackInput.value.trim();

	errorMessage.textContent = "";

	if (!feedback) {
		errorMessage.textContent = "Please enter some feedback.";
		return;
	}

	try {
		analyseButton.textContent = "Analysing...";
		analyseButton.disabled = true;

		const response = await fetch(
			"https://customer-feedback-intelligence-ernh.onrender.com/feedback/analyse",
			{
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify({
					feedback: feedback,
				}),
			},
		);

		if (!response.ok) {
			throw new Error(`API returned ${response.status}`);
		}

		const data = await response.json();

		sentiment.textContent = data.sentiment;
		category.textContent = data.category;
		priority.textContent = data.priority;

		results.classList.remove("hidden");
	} catch (error) {
		console.error(error);

		errorMessage.textContent = "Unable to analyse feedback. Please try again.";
	} finally {
		analyseButton.textContent = "Analyse Feedback";
		analyseButton.disabled = false;
	}
});
