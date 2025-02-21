function calculateScore() {
    let score = 0;
    let totalQuestions = 5;

    for (let i = 1; i <= totalQuestions; i++) {
        // Correct template literal usage
        let selectedOption = document.querySelector(`input[name="q${i}"]:checked`);
        if (selectedOption) {
            score += parseInt(selectedOption.value);
        }
    }

    let resultText = "";
    if (score >= 10) {
        resultText = "✅ You are in a healthy relationship! Keep communicating and respecting each other. ❤";
    }
    else if (score >= 5) {
        resultText = "⚠ Your relationship has some challenges. Work on improving communication and trust.";
    }
    else if (score >0 && score<5) {
        resultText = "🚨 Your relationship may be unhealthy. Consider seeking support or reevaluating it.";
    }
    else {
        resultText = "🚨 Please answer the above questions.";
    }

    // Display the result in the element with ID "quizResult"
    document.getElementById("quizResult").innerHTML = resultText;
}
