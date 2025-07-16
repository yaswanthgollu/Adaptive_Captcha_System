let start;

function startTimer() {
    start = new Date();
}

function captureTime() {
    let end = new Date();
    let timeTaken = (end - start) / 1000;
    document.getElementById("time_taken").value = timeTaken;
}

function validateCaptchaInput() {
    const userInput = document.getElementById("captcha_input").value;
    const feedback = document.getElementById("feedback");

    if (userInput.length === 0) {
        feedback.textContent = "";
        feedback.style.color = "";
        return;
    }

    if (actualCaptcha.startsWith(userInput)) {
        feedback.textContent = userInput.length === actualCaptcha.length ? "✅ Looks good!" : "🟡 Keep going...";
        feedback.style.color = userInput.length === actualCaptcha.length ? "green" : "orange";
    } else {
        feedback.textContent = "❌ Mismatch!";
        feedback.style.color = "red";
    }
}
