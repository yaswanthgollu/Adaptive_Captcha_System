let start;

function startTimer() {
    start = new Date();
}

function captureTime() {
    let end = new Date();
    let timeTaken = (end - start) / 1000;
    document.getElementById("time_taken").value = timeTaken;
}
