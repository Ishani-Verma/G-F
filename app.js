document.getElementById('clear-btn').addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('fact-input').value = '';
});
// function clearInputField(elementId) {
//     document.getElementById(elementId).value = '';
// }


document.getElementById('submit-btn').addEventListener('click', function () {
    // Redirect to another page
    window.location.href = 'output.html';
    var factInput = document.getElementById('fact-input').value;
    document.getElementById('hidden-fact-input').value = factInput;
    document.getElementById('fake-fact-form').submit(); 
});
document.getElementById('refresh-btn').addEventListener('click', function () {
    var factInput2 = document.getElementById('fact-input2').value;
    document.getElementById('hidden-fact-input').value = factInput2;
    document.getElementById('output-form').submit();
});
document.addEventListener('DOMContentLoaded', function() {
    var profileIcon = document.getElementById('user-profile');
    var profileTextarea = document.getElementById('profile-textarea');

    profileIcon.addEventListener('click', function() {
        
        if (profileTextarea.style.display === 'none') {
            profileTextarea.style.display = 'block';
        } else {
            profileTextarea.style.display = 'none';
        }
    });
});
document.getElementById("profile-icon").addEventListener("click", function() {
    document.getElementById("popup").style.display = "block";
  });
  
  // Close the popup if clicked outside
  window.addEventListener("click", function(event) {
    var popup = document.getElementById("popup");
    if (event.target != popup && event.target.parentNode != popup) {
      popup.style.display = "none";
    }
  });