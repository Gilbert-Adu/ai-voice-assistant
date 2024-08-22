document.getElementById('activate-btn').addEventListener('click', () => {
    console.log("clicked")
});

/**
 * const buttons = document.getElementsByClassName('activate-btn');

buttons.array.forEach(button => {
    button.addEventListener('click', function() {
        console.log("clicked")
        
         fetch('/activate')
            .then(response => response.json())
            .then(data => {
                document.getElementById('response-text').textContent = data.response;
            })
            .catch(error => console.error('Error:', error));
         
    });
    

    
});
 */
