function analyzeSentiment() {
    let text = document.getElementById("textInput").value;
    
    fetch('/analyze', {
        method: "POST",
        body: new URLSearchParams({text: text}),
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerHTML = "Sentiment: " + data.sentiment;
    })
    .catch(error => console.error("Error:", error));
}
