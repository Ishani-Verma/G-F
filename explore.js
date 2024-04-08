document.addEventListener('DOMContentLoaded', function() {
    // Function to fetch new facts from the backend
    function fetchFacts() {
        fetch('/get_new_facts')
            .then(response => response.json())
            .then(data => {
                // Update the textarea with the new facts
                document.getElementById('facts-textarea').value = facts;
            })
            .catch(error => console.error('Error fetching new facts:', error));
    }

    // Fetch new facts when the button is clicked
    document.getElementById('new-button').addEventListener('click', fetchFacts);

    // Fetch initial facts when the page loads
    fetchFacts();
});
