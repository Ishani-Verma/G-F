document.addEventListener('DOMContentLoaded', function() {
    // Retrieve the result from the input box and display it in the fact-input2 box
    var result = document.getElementById('fact-input2').value;
    // Set the value of fact-input2
    document.getElementById('fact-input2').value = result;

    // Event listener for refreshing the page
    document.getElementById('refresh-btn').addEventListener('click', function () {
        // Redirect to the first page
        window.location.href = '/';
    });
});