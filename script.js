document.getElementById('predictButton').addEventListener('click', function() {
    let newsInput = document.getElementById('newsInput').value;
    
    if (newsInput.trim() === "") {
        alert("Please enter a news article.");
        return;
    }

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ article: newsInput })
    })
    .then(response => response.json())
    .then(data => {
        const resultElement = document.getElementById('predictionResult');
        if (data.prediction === 0) {
            resultElement.textContent = "The news is likely to be true.";
        } else {
            resultElement.textContent = "The news is likely to be fake.";
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
