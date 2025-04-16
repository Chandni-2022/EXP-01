function validateForm() {
    let fullname = document.getElementById('name').value;
    let username = document.getElementById('username').value;
    let email = document.getElementById('email').value;
    let phone = document.getElementById('phone').value;
    let password = document.getElementById('password').value;
    let confirmPassword = document.getElementById('confirmPassword').value;
    let gender = document.querySelector('input[name="gender"]:checked');

    // let errorMessages = '';
    let errorMessages = '';

    if (!fullname) {
        errorMessages += 'Full Name is required.<br>';
    }
    if (!username) {
        errorMessages += 'Username is required.<br>';
    }
    if (!email.match(/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/)) {
        errorMessages += 'Invalid email format.<br>';
    }
    if (!phone.match(/^\d{10}$/)) {
        errorMessages += 'Phone number must be 10 digits.<br>';
    }
    if (password.length < 6) {
        errorMessages += 'Password must be at least 6 characters.<br>';
    }
    if (password !== confirmPassword) {
        errorMessages += 'Passwords do not match.<br>';
    }
    if (!gender) {
        errorMessages += 'Gender selection is required.<br>';
    }

    if (errorMessages) {
        document.getElementById('errorMessages').innerHTML = errorMessages;
        return false;
    }
    return true;
}
