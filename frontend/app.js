document.getElementById('activate-btn').addEventListener('click', function() {
    fetch('/activate')
        .then(response => response.json())
        .then(data => {
            document.getElementById('response-text').textContent = data.response;
        })
        .catch(error => console.error('Error:', error));
});
