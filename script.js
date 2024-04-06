document.getElementById('loginBtn').addEventListener('click', function() {
    document.getElementById('loginForm').classList.remove('hidden');
    document.getElementById('signupForm').classList.add('hidden');
  });
  
  document.getElementById('signupBtn').addEventListener('click', function() {
    document.getElementById('signupForm').classList.remove('hidden');
    document.getElementById('loginForm').classList.add('hidden');
  });
  
  document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;
    let passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    
    // Here, you would replace the condition with your actual authentication logic
    // For demonstration purposes, we check if the email is "test@example.com" and password is "Password1!"
    if (email === 'test@example.com' && password === 'Password1!') {
      // If credentials are correct, submit the form
      this.submit();
    } else {
      // If credentials are incorrect, display "Wrong password" message
      document.getElementById('wrongPassword').classList.remove('hidden');
    }
  });
  
  document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault();
    let password = document.getElementById('newPassword').value;
    let passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    if (!passwordPattern.test(password)) {
      alert('Password must contain at least one uppercase letter, one lowercase letter, one number, one special character, and be at least 8 characters long.');
    } else {
      // Submit form
      this.submit();
    }
  });
  