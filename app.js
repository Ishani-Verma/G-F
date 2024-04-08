document.getElementById('clear-btn').addEventListener('click', function() {
    document.getElementById('fact-input').value = '';
});



document.getElementById('submit-btn').addEventListener('click', function () {
    // Redirect to another page
    window.location.href = 'output.html'; 
});

const homeButton = document.querySelector('.home-button');

// Attach a click event listener to the button
homeButton.addEventListener('click', function() {
  // This function will be executed when the button is clicked
  window.location.href = 'qqq.html'; 
  // You can add your desired functionality here
});

